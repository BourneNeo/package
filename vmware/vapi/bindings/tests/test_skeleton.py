"""
Unit tests for binding skeleton helper classes
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest

from vmware.vapi.bindings.skeleton import (
    ApiInterfaceSkeleton, VapiInterface)
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.type import (
    ListType, StructType, ErrorType, StringType, BooleanType, OptionalType,
    DynamicStructType)
from vmware.vapi.data.value import (
    StringValue, StructValue, BooleanValue, IntegerValue, OptionalValue)
from vmware.vapi.core import (
    InterfaceIdentifier,
    ExecutionContext,
    MethodResult)
from vmware.vapi.provider.local import LocalProvider
from vmware.vapi.stdlib.provider.factories import MessageFactory, ErrorFactory
from vmware.vapi.protocol.client.local_connector import LocalConnector
from vmware.vapi.stdlib.client.factories import StubConfigurationFactory
from vmware.vapi.stdlib.client.introspection import make_introspection_error_def
from com.vmware.vapi.std.introspection_client import Service, Operation

interface_name = 'mock_interface'
method_name = 'echo'
interface_id = InterfaceIdentifier(interface_name)
messages = {
    'mock.not_found': 'not found',
}
message_factory = MessageFactory(messages)


class MockImpl(VapiInterface):
    def __init__(self, error_types=None):
        VapiInterface.__init__(self, MockSkeleton, error_types=error_types)

    def echo(self, **kwargs):
        message = kwargs.get('message')
        throw = kwargs.get('throw')
        if throw:
            msg = message_factory.get_message('mock.not_found')
            raise ErrorFactory.new_not_found(messages=[msg])
        return message


class MockSkeleton(ApiInterfaceSkeleton):
    def __init__(self, impl, error_types):
        operations = {}
        input_type = StructType(method_name, {'message': StringType(),
                      'throw': BooleanType()})
        localizable_message_type = StructType(
            'com.vmware.vapi.std.localizable_message',
            {
                'id': StringType(),
                'default_message': StringType(),
                'args': ListType(StringType())
            })
        messages_list_type = ListType(localizable_message_type)
        data_optional_type = OptionalType(
            DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct))
        error = ErrorType('com.vmware.vapi.std.errors.not_found',
                          {
                              'messages': messages_list_type,
                              'data': data_optional_type
                          })
        operations[method_name] = {
            'input_type': input_type,
            'output_type': StringType(),
            'errors': [error],
            'input_validator_list': [],
            'output_validator_list': []
        }
        ApiInterfaceSkeleton.__init__(self,
                                      iface_name=interface_name,
                                      impl=impl,
                                      operations=operations,
                                      error_types=error_types)


class TestApiInterfaceSkeleton(unittest.TestCase):

    def setUp(self):
        self.provider = LocalProvider()
        self.provider.add_interface(MockImpl())
        connector = LocalConnector(self.provider)
        stub_config = StubConfigurationFactory.new_std_configuration(connector)
        self.service = Service(stub_config)
        self.operation = Operation(stub_config)

    def test_services(self):
        expected_services = sorted([
            'com.vmware.vapi.std.introspection.service',
            'com.vmware.vapi.std.introspection.provider',
            'mock_interface',
            'com.vmware.vapi.std.introspection.operation'
        ])
        actual_services = sorted(self.service.list())
        self.assertEqual(actual_services, expected_services)

    def test_service_info(self):
        info = self.service.get(id='mock_interface')
        self.assertEqual(info.operations, set([method_name]))

    def test_operation_info(self):
        actual_info = self.operation.get(service_id=interface_name,
                                         operation_id=method_name)
        input_def = Operation.DataDefinition(
            type=Operation.DataDefinition.DataType.STRUCTURE,
            name=method_name,
            fields={
                'message': Operation.DataDefinition(
                    type=Operation.DataDefinition.DataType.STRING
                ),
                'throw': Operation.DataDefinition(
                    type=Operation.DataDefinition.DataType.BOOLEAN
                )
            }
        )
        output_def = Operation.DataDefinition(
            type=Operation.DataDefinition.DataType.STRING)
        error_defs = [
            make_introspection_error_def('com.vmware.vapi.std.errors.not_found'),
            make_introspection_error_def('com.vmware.vapi.std.errors.unexpected_input'),
            make_introspection_error_def('com.vmware.vapi.std.errors.internal_server_error'),
            make_introspection_error_def('com.vmware.vapi.std.errors.invalid_argument'),
            make_introspection_error_def('com.vmware.vapi.std.errors.operation_not_found'),
        ]
        expected_info = Operation.Info(input_definition=input_def,
                                       output_definition=output_def,
                                       error_definitions=error_defs)
        self.assertEqual(actual_info.input_definition,
                         expected_info.input_definition)
        self.assertEqual(actual_info.output_definition,
                         expected_info.output_definition)
        actual_errors = [error.name for error in actual_info.error_definitions]
        expected_errors = [error.name for error in expected_info.error_definitions]
        self.assertEqual(sorted(actual_errors), sorted(expected_errors))

    def test_invoke(self):
        ctx = ExecutionContext()
        input_ = StructValue(method_name)
        input_.set_field('message', StringValue('hello'))
        input_.set_field('throw', BooleanValue(False))
        actual_method_result = self.provider.invoke(interface_name,
                                                    method_name,
                                                    input_,
                                                    ctx)
        expected_method_result = MethodResult(output=StringValue('hello'))
        self.assertEqual(actual_method_result.output,
                         expected_method_result.output)
        self.assertEqual(actual_method_result.error,
                         expected_method_result.error)

    def test_invoke_invalid_arg(self):
        ctx = ExecutionContext()
        input_ = StructValue(method_name)
        input_.set_field('message', IntegerValue(10))
        input_.set_field('throw', BooleanValue(False))
        actual_method_result = self.provider.invoke(interface_name,
                                                    method_name,
                                                    input_,
                                                    ctx)
        self.assertFalse(actual_method_result.success())

    def test_invoke_error(self):
        ctx = ExecutionContext()
        input_ = StructValue(method_name)
        input_.set_field('message', IntegerValue(10))
        input_.set_field('throw', BooleanValue(True))
        actual_method_result = self.provider.invoke(interface_name,
                                                    method_name,
                                                    input_,
                                                    ctx)
        self.assertFalse(actual_method_result.success())

    def test_check_for_unknown_fields(self):
        struct_type = StructType(
            'test',
            {
                'name': StringType()
            }
        )
        struct_value = StructValue(
            name='test',
            values={
                'name': StringValue('hello')
            }
        )
        self.assertIsNone(
            ApiInterfaceSkeleton.check_for_unknown_fields(
                struct_type, struct_value))

    def test_check_for_unknown_fields_2(self):
        optional_struct_type = OptionalType(StructType(
            'test',
            {
                'name': StringType()
            }
        ))
        optional_struct_value = OptionalValue(StructValue(
            name='test',
            values={
                'name': StringValue('hello')
            }
        ))
        self.assertIsNone(
            ApiInterfaceSkeleton.check_for_unknown_fields(
                optional_struct_type,
                optional_struct_value))

    def test_check_for_unknown_fields_invalid_1(self):
        struct_type = StructType(
            'test',
            {
                'name': StringType()
            }
        )
        struct_value = StructValue(
            name='test',
            values={
                'name': StringValue('hello'),
                'address': StringValue('hello')
            }
        )
        self.assertIsNotNone(
            ApiInterfaceSkeleton.check_for_unknown_fields(
                struct_type, struct_value))

    def test_check_for_unknown_fields_invalid_2(self):
        info_type = StructType(
            'info',
            {
                'basic': StructType(
                    'basic',
                    {
                        'name': StringType()
                    }
                ),
                'address': StructType(
                    'address',
                    {
                        'city': StringType()
                    }
                ),
            }
        )
        info_value = StructValue(
            name='info',
            values={
                'basic': StructValue(
                    name='basic',
                    values={
                        'name': 'foo',
                        'extra': 'bar' # extra field
                    }
                ),
                'address': StructValue(
                    name='address',
                    values={
                        'city': 'foo'
                    }
                )
            }
        )
        self.assertIsNotNone(
            ApiInterfaceSkeleton.check_for_unknown_fields(
                info_type, info_value))

    def test_check_for_unknown_fields_invalid_3(self):
        list_info_type = ListType(StructType(
            'info',
            {
                'basic': StructType(
                    'basic',
                    {
                        'name': StringType()
                    }
                ),
                'address': StructType(
                    'address',
                    {
                        'city': StringType()
                    }
                ),
            }
        ))
        list_info_value = [
            StructValue(
                name='info',
                values={
                    'basic': StructValue(
                        name='basic',
                        values={
                            'name': 'foo',
                        }
                    ),
                    'address': StructValue(
                        name='address',
                        values={
                            'city': 'foo'
                        }
                    )
                }
            ),
            StructValue(
                name='info',
                values={
                    'basic': StructValue(
                        name='basic',
                        values={
                            'name': 'foo',
                            'extra': 'bar' # extra field in 2nd element of the list
                        }
                    ),
                    'address': StructValue(
                        name='address',
                        values={
                            'city': 'foo'
                        }
                    )
                }
            )
        ]
        self.assertIsNotNone(
            ApiInterfaceSkeleton.check_for_unknown_fields(
                list_info_type, list_info_value))


if __name__ == "__main__":
    unittest.main()
