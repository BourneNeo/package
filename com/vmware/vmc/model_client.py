# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2017 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.model.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import UnionValidator, HasFieldsOfValidator
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.rest import OperationRestMetadata

class OfferType(Enum):
    """
    

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    TERM = None
    """


    """
    ON_DEMAND = None
    """


    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`OfferType` instance.
        """
        Enum.__init__(string)

OfferType._set_values([
    OfferType('TERM'),
    OfferType('ON_DEMAND'),
])
OfferType._set_binding_type(type.EnumType(
    'com.vmware.vmc.model.offer_type',
    OfferType))




class AbstractEntity(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        VapiStruct.__init__(self)

AbstractEntity._set_binding_type(type.StructType(
    'com.vmware.vmc.model.abstract_entity', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
    },
    AbstractEntity,
    False,
    None))



class AccountLinkSddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_subnet_ids': 'customer_subnet_ids',
                            'connected_account_id': 'connected_account_id',
                            }

    def __init__(self,
                 customer_subnet_ids=None,
                 connected_account_id=None,
                ):
        """
        :type  customer_subnet_ids: :class:`list` of :class:`str` or ``None``
        :param customer_subnet_ids: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: The ID of the customer connected account to work with.
        """
        self.customer_subnet_ids = customer_subnet_ids
        self.connected_account_id = connected_account_id
        VapiStruct.__init__(self)

AccountLinkSddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.account_link_sddc_config', {
        'customer_subnet_ids': type.OptionalType(type.ListType(type.StringType())),
        'connected_account_id': type.OptionalType(type.StringType()),
    },
    AccountLinkSddcConfig,
    False,
    None))



class Agent(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "Agent"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'addresses': 'addresses',
                            'healthy': 'healthy',
                            'custom_properties': 'custom_properties',
                            'last_health_status_change': 'last_health_status_change',
                            'internal_ip': 'internal_ip',
                            'reserved_ip': 'reserved_ip',
                            'network_netmask': 'network_netmask',
                            'network_gateway': 'network_gateway',
                            'provider': 'provider',
                            'agent_url': 'agent_url',
                            'network_cidr': 'network_cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 addresses=None,
                 healthy=None,
                 custom_properties=None,
                 last_health_status_change=None,
                 internal_ip=None,
                 reserved_ip=None,
                 network_netmask=None,
                 network_gateway=None,
                 provider='Agent',
                 agent_url=None,
                 network_cidr=None,
                 id=None,
                ):
        """
        :type  addresses: :class:`list` of :class:`str` or ``None``
        :param addresses: 
        :type  healthy: :class:`bool` or ``None``
        :param healthy: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  last_health_status_change: :class:`long` or ``None``
        :param last_health_status_change: 
        :type  internal_ip: :class:`str` or ``None``
        :param internal_ip: 
        :type  reserved_ip: :class:`str` or ``None``
        :param reserved_ip: 
        :type  network_netmask: :class:`str` or ``None``
        :param network_netmask: 
        :type  network_gateway: :class:`str` or ``None``
        :param network_gateway: 
        :type  provider: :class:`str`
        :param provider: 
        :type  agent_url: :class:`str` or ``None``
        :param agent_url: 
        :type  network_cidr: :class:`str` or ``None``
        :param network_cidr: 
        :type  id: :class:`str` or ``None``
        :param id: 
        """
        self.addresses = addresses
        self.healthy = healthy
        self.custom_properties = custom_properties
        self.last_health_status_change = last_health_status_change
        self.internal_ip = internal_ip
        self.reserved_ip = reserved_ip
        self.network_netmask = network_netmask
        self.network_gateway = network_gateway
        self.provider = provider
        self.agent_url = agent_url
        self.network_cidr = network_cidr
        self.id = id
        VapiStruct.__init__(self)

Agent._set_binding_type(type.StructType(
    'com.vmware.vmc.model.agent', {
        'addresses': type.OptionalType(type.ListType(type.StringType())),
        'healthy': type.OptionalType(type.BooleanType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'last_health_status_change': type.OptionalType(type.IntegerType()),
        'internal_ip': type.OptionalType(type.StringType()),
        'reserved_ip': type.OptionalType(type.StringType()),
        'network_netmask': type.OptionalType(type.StringType()),
        'network_gateway': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'agent_url': type.OptionalType(type.StringType()),
        'network_cidr': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    Agent,
    False,
    None))



class AmiInfo(VapiStruct):
    """
    the AmiInfo used for deploying esx of the sddc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'id': 'id',
                            'name': 'name',
                            }

    def __init__(self,
                 region=None,
                 id=None,
                 name=None,
                ):
        """
        :type  region: :class:`str` or ``None``
        :param region: the region of the esx ami
        :type  id: :class:`str` or ``None``
        :param id: the ami id for the esx
        :type  name: :class:`str` or ``None``
        :param name: the name of the esx ami
        """
        self.region = region
        self.id = id
        self.name = name
        VapiStruct.__init__(self)

AmiInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.ami_info', {
        'region': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
    },
    AmiInfo,
    False,
    None))



class AwsAgent(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'instance_id': 'instance_id',
                            'key_pair': 'key_pair',
                            'addresses': 'addresses',
                            'healthy': 'healthy',
                            'custom_properties': 'custom_properties',
                            'last_health_status_change': 'last_health_status_change',
                            'internal_ip': 'internal_ip',
                            'reserved_ip': 'reserved_ip',
                            'network_netmask': 'network_netmask',
                            'network_gateway': 'network_gateway',
                            'provider': 'provider',
                            'agent_url': 'agent_url',
                            'network_cidr': 'network_cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 instance_id=None,
                 key_pair=None,
                 addresses=None,
                 healthy=None,
                 custom_properties=None,
                 last_health_status_change=None,
                 internal_ip=None,
                 reserved_ip=None,
                 network_netmask=None,
                 network_gateway=None,
                 provider='AWS',
                 agent_url=None,
                 network_cidr=None,
                 id=None,
                ):
        """
        :type  instance_id: :class:`str` or ``None``
        :param instance_id: 
        :type  key_pair: :class:`AwsKeyPair` or ``None``
        :param key_pair: 
        :type  addresses: :class:`list` of :class:`str` or ``None``
        :param addresses: 
        :type  healthy: :class:`bool` or ``None``
        :param healthy: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  last_health_status_change: :class:`long` or ``None``
        :param last_health_status_change: 
        :type  internal_ip: :class:`str` or ``None``
        :param internal_ip: 
        :type  reserved_ip: :class:`str` or ``None``
        :param reserved_ip: 
        :type  network_netmask: :class:`str` or ``None``
        :param network_netmask: 
        :type  network_gateway: :class:`str` or ``None``
        :param network_gateway: 
        :type  provider: :class:`str`
        :param provider: 
        :type  agent_url: :class:`str` or ``None``
        :param agent_url: 
        :type  network_cidr: :class:`str` or ``None``
        :param network_cidr: 
        :type  id: :class:`str` or ``None``
        :param id: 
        """
        self.instance_id = instance_id
        self.key_pair = key_pair
        self.addresses = addresses
        self.healthy = healthy
        self.custom_properties = custom_properties
        self.last_health_status_change = last_health_status_change
        self.internal_ip = internal_ip
        self.reserved_ip = reserved_ip
        self.network_netmask = network_netmask
        self.network_gateway = network_gateway
        self.provider = provider
        self.agent_url = agent_url
        self.network_cidr = network_cidr
        self.id = id
        VapiStruct.__init__(self)

AwsAgent._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_agent', {
        'instance_id': type.OptionalType(type.StringType()),
        'key_pair': type.OptionalType(type.ReferenceType(__name__, 'AwsKeyPair')),
        'addresses': type.OptionalType(type.ListType(type.StringType())),
        'healthy': type.OptionalType(type.BooleanType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'last_health_status_change': type.OptionalType(type.IntegerType()),
        'internal_ip': type.OptionalType(type.StringType()),
        'reserved_ip': type.OptionalType(type.StringType()),
        'network_netmask': type.OptionalType(type.StringType()),
        'network_gateway': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'agent_url': type.OptionalType(type.StringType()),
        'network_cidr': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    AwsAgent,
    False,
    None))



class AwsCloudProvider(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'regions': 'regions',
                            'provider': 'provider',
                            }

    def __init__(self,
                 regions=None,
                 provider='AWS',
                ):
        """
        :type  regions: :class:`list` of :class:`str` or ``None``
        :param regions: 
        :type  provider: :class:`str`
        :param provider: Name of the Cloud Provider
        """
        self.regions = regions
        self.provider = provider
        VapiStruct.__init__(self)

AwsCloudProvider._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_cloud_provider', {
        'regions': type.OptionalType(type.ListType(type.StringType())),
        'provider': type.StringType(),
    },
    AwsCloudProvider,
    False,
    None))



class AwsCompatibleSubnets(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_available_zones': 'customer_available_zones',
                            'vpc_map': 'vpc_map',
                            }

    def __init__(self,
                 customer_available_zones=None,
                 vpc_map=None,
                ):
        """
        :type  customer_available_zones: :class:`list` of :class:`str` or ``None``
        :param customer_available_zones: 
        :type  vpc_map: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param vpc_map: 
        """
        self.customer_available_zones = customer_available_zones
        self.vpc_map = vpc_map
        VapiStruct.__init__(self)

AwsCompatibleSubnets._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_compatible_subnets', {
        'customer_available_zones': type.OptionalType(type.ListType(type.StringType())),
        'vpc_map': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    AwsCompatibleSubnets,
    False,
    None))



class AwsCustomerConnectedAccount(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'policy_payer_arn': 'policy_payer_arn',
                            'account_number': 'account_number',
                            'policy_external_id': 'policy_external_id',
                            'region_to_az_to_shadow_mapping': 'region_to_az_to_shadow_mapping',
                            'org_id': 'org_id',
                            'cf_stack_name': 'cf_stack_name',
                            'policy_service_arn': 'policy_service_arn',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 policy_payer_arn=None,
                 account_number=None,
                 policy_external_id=None,
                 region_to_az_to_shadow_mapping=None,
                 org_id=None,
                 cf_stack_name=None,
                 policy_service_arn=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  policy_payer_arn: :class:`str` or ``None``
        :param policy_payer_arn: 
        :type  account_number: :class:`str` or ``None``
        :param account_number: 
        :type  policy_external_id: :class:`str` or ``None``
        :param policy_external_id: 
        :type  region_to_az_to_shadow_mapping: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param region_to_az_to_shadow_mapping: Provides a map of regions to availability zones from the shadow
            account's perspective
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  cf_stack_name: :class:`str` or ``None``
        :param cf_stack_name: 
        :type  policy_service_arn: :class:`str` or ``None``
        :param policy_service_arn: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.policy_payer_arn = policy_payer_arn
        self.account_number = account_number
        self.policy_external_id = policy_external_id
        self.region_to_az_to_shadow_mapping = region_to_az_to_shadow_mapping
        self.org_id = org_id
        self.cf_stack_name = cf_stack_name
        self.policy_service_arn = policy_service_arn
        VapiStruct.__init__(self)

AwsCustomerConnectedAccount._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_customer_connected_account', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'policy_payer_arn': type.OptionalType(type.StringType()),
        'account_number': type.OptionalType(type.StringType()),
        'policy_external_id': type.OptionalType(type.StringType()),
        'region_to_az_to_shadow_mapping': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'org_id': type.OptionalType(type.StringType()),
        'cf_stack_name': type.OptionalType(type.StringType()),
        'policy_service_arn': type.OptionalType(type.StringType()),
    },
    AwsCustomerConnectedAccount,
    False,
    None))



class AwsEsxHost(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'internal_public_ip_pool': 'internal_public_ip_pool',
                            'name': 'name',
                            'esx_id': 'esx_id',
                            'hostname': 'hostname',
                            'provider': 'provider',
                            'mac_address': 'mac_address',
                            'custom_properties': 'custom_properties',
                            'esx_state': 'esx_state',
                            }

    def __init__(self,
                 internal_public_ip_pool=None,
                 name=None,
                 esx_id=None,
                 hostname=None,
                 provider='AWS',
                 mac_address=None,
                 custom_properties=None,
                 esx_state=None,
                ):
        """
        :type  internal_public_ip_pool: :class:`list` of :class:`SddcPublicIp` or ``None``
        :param internal_public_ip_pool: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  esx_id: :class:`str` or ``None``
        :param esx_id: 
        :type  hostname: :class:`str` or ``None``
        :param hostname: 
        :type  provider: :class:`str`
        :param provider: 
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  esx_state: :class:`str` or ``None``
        :param esx_state: Possible values are: 
            
            * :attr:`EsxHost.ESX_STATE_DEPLOYING`
            * :attr:`EsxHost.ESX_STATE_PROVISIONED`
            * :attr:`EsxHost.ESX_STATE_READY`
            * :attr:`EsxHost.ESX_STATE_DELETING`
            * :attr:`EsxHost.ESX_STATE_DELETED`
            * :attr:`EsxHost.ESX_STATE_FAILED`
        """
        self.internal_public_ip_pool = internal_public_ip_pool
        self.name = name
        self.esx_id = esx_id
        self.hostname = hostname
        self.provider = provider
        self.mac_address = mac_address
        self.custom_properties = custom_properties
        self.esx_state = esx_state
        VapiStruct.__init__(self)

AwsEsxHost._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_esx_host', {
        'internal_public_ip_pool': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcPublicIp'))),
        'name': type.OptionalType(type.StringType()),
        'esx_id': type.OptionalType(type.StringType()),
        'hostname': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'mac_address': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'esx_state': type.OptionalType(type.StringType()),
    },
    AwsEsxHost,
    False,
    None))



class AwsKeyPair(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'key_name': 'key_name',
                            'key_fingerprint': 'key_fingerprint',
                            'key_material': 'key_material',
                            }

    def __init__(self,
                 key_name=None,
                 key_fingerprint=None,
                 key_material=None,
                ):
        """
        :type  key_name: :class:`str` or ``None``
        :param key_name: 
        :type  key_fingerprint: :class:`str` or ``None``
        :param key_fingerprint: 
        :type  key_material: :class:`str` or ``None``
        :param key_material: 
        """
        self.key_name = key_name
        self.key_fingerprint = key_fingerprint
        self.key_material = key_material
        VapiStruct.__init__(self)

AwsKeyPair._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_key_pair', {
        'key_name': type.OptionalType(type.StringType()),
        'key_fingerprint': type.OptionalType(type.StringType()),
        'key_material': type.OptionalType(type.StringType()),
    },
    AwsKeyPair,
    False,
    None))



class AwsOrgConfiguration(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='AWS',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`OrgConfiguration.PROVIDER_AWS`
            
             Discriminator for provider specific properties
        """
        self.provider = provider
        VapiStruct.__init__(self)

AwsOrgConfiguration._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_org_configuration', {
        'provider': type.StringType(),
    },
    AwsOrgConfiguration,
    False,
    None))



class AwsSddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'vpc_name': 'vpc_name',
                            'name': 'name',
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'vxlan_subnet': 'vxlan_subnet',
                            'vpc_cidr': 'vpc_cidr',
                            'provider': 'provider',
                            'sso_domain': 'sso_domain',
                            'num_hosts': 'num_hosts',
                            }

    def __init__(self,
                 region=None,
                 vpc_name=None,
                 name=None,
                 account_link_sddc_config=None,
                 vxlan_subnet=None,
                 vpc_cidr=None,
                 provider='AWS',
                 sso_domain=None,
                 num_hosts=None,
                ):
        """
        :type  region: :class:`str`
        :param region: 
        :type  vpc_name: :class:`str` or ``None``
        :param vpc_name: 
        :type  name: :class:`str`
        :param name: 
        :type  account_link_sddc_config: :class:`list` of :class:`AccountLinkSddcConfig` or ``None``
        :param account_link_sddc_config: A list of the SDDC linkg configurations to use.
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: AWS VPC IP range. Only prefix of 16 or 20 is currently supported.
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcConfig.PROVIDER_AWS`
            
            Determines what additional properties are available based on cloud
            provider.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users. If not specified,
            vmc.local will be used.
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        """
        self.region = region
        self.vpc_name = vpc_name
        self.name = name
        self.account_link_sddc_config = account_link_sddc_config
        self.vxlan_subnet = vxlan_subnet
        self.vpc_cidr = vpc_cidr
        self.provider = provider
        self.sso_domain = sso_domain
        self.num_hosts = num_hosts
        VapiStruct.__init__(self)

AwsSddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_config', {
        'region': type.StringType(),
        'vpc_name': type.OptionalType(type.StringType()),
        'name': type.StringType(),
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AccountLinkSddcConfig'))),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'vpc_cidr': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'sso_domain': type.OptionalType(type.StringType()),
        'num_hosts': type.IntegerType(),
    },
    AwsSddcConfig,
    False,
    None))



class AwsSddcConnection(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'cidr_block_subnet': 'cidr_block_subnet',
                            'connected_account_id': 'connected_account_id',
                            'eni_group': 'eni_group',
                            'subnet_id': 'subnet_id',
                            'org_id': 'org_id',
                            'sddc_id': 'sddc_id',
                            'cidr_block_vpc': 'cidr_block_vpc',
                            'subnet_availability_zone': 'subnet_availability_zone',
                            'vpc_id': 'vpc_id',
                            'customer_eni_infos': 'customer_eni_infos',
                            'default_route_table': 'default_route_table',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 cidr_block_subnet=None,
                 connected_account_id=None,
                 eni_group=None,
                 subnet_id=None,
                 org_id=None,
                 sddc_id=None,
                 cidr_block_vpc=None,
                 subnet_availability_zone=None,
                 vpc_id=None,
                 customer_eni_infos=None,
                 default_route_table=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  cidr_block_subnet: :class:`str` or ``None``
        :param cidr_block_subnet: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: 
        :type  eni_group: :class:`str` or ``None``
        :param eni_group: 
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: 
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  sddc_id: :class:`str` or ``None``
        :param sddc_id: 
        :type  cidr_block_vpc: :class:`str` or ``None``
        :param cidr_block_vpc: 
        :type  subnet_availability_zone: :class:`str` or ``None``
        :param subnet_availability_zone: 
        :type  vpc_id: :class:`str` or ``None``
        :param vpc_id: 
        :type  customer_eni_infos: :class:`list` of :class:`str` or ``None``
        :param customer_eni_infos: 
        :type  default_route_table: :class:`str` or ``None``
        :param default_route_table: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.cidr_block_subnet = cidr_block_subnet
        self.connected_account_id = connected_account_id
        self.eni_group = eni_group
        self.subnet_id = subnet_id
        self.org_id = org_id
        self.sddc_id = sddc_id
        self.cidr_block_vpc = cidr_block_vpc
        self.subnet_availability_zone = subnet_availability_zone
        self.vpc_id = vpc_id
        self.customer_eni_infos = customer_eni_infos
        self.default_route_table = default_route_table
        VapiStruct.__init__(self)

AwsSddcConnection._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_connection', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'cidr_block_subnet': type.OptionalType(type.StringType()),
        'connected_account_id': type.OptionalType(type.StringType()),
        'eni_group': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'org_id': type.OptionalType(type.StringType()),
        'sddc_id': type.OptionalType(type.StringType()),
        'cidr_block_vpc': type.OptionalType(type.StringType()),
        'subnet_availability_zone': type.OptionalType(type.StringType()),
        'vpc_id': type.OptionalType(type.StringType()),
        'customer_eni_infos': type.OptionalType(type.ListType(type.StringType())),
        'default_route_table': type.OptionalType(type.StringType()),
    },
    AwsSddcConnection,
    False,
    None))



class AwsSddcResourceConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "AWS"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'public_ip_pool': 'public_ip_pool',
                            'region': 'region',
                            'vpc_info': 'vpc_info',
                            'max_num_public_ip': 'max_num_public_ip',
                            'vpc_info_peered_agent': 'vpc_info_peered_agent',
                            'backup_restore_bucket': 'backup_restore_bucket',
                            'mgw_id': 'mgw_id',
                            'nsx_mgr_url': 'nsx_mgr_url',
                            'psc_management_ip': 'psc_management_ip',
                            'psc_url': 'psc_url',
                            'cgws': 'cgws',
                            'management_ds': 'management_ds',
                            'custom_properties': 'custom_properties',
                            'cloud_password': 'cloud_password',
                            'provider': 'provider',
                            'clusters': 'clusters',
                            'vc_management_ip': 'vc_management_ip',
                            'sddc_networks': 'sddc_networks',
                            'cloud_username': 'cloud_username',
                            'esx_hosts': 'esx_hosts',
                            'nsx_mgr_management_ip': 'nsx_mgr_management_ip',
                            'vc_instance_id': 'vc_instance_id',
                            'esx_cluster_id': 'esx_cluster_id',
                            'vc_public_ip': 'vc_public_ip',
                            'vc_url': 'vc_url',
                            'sddc_manifest': 'sddc_manifest',
                            'vxlan_subnet': 'vxlan_subnet',
                            'cloud_user_group': 'cloud_user_group',
                            'management_rp': 'management_rp',
                            'sso_domain': 'sso_domain',
                            'dns_with_management_vm_private_ip': 'dns_with_management_vm_private_ip',
                            }

    def __init__(self,
                 account_link_sddc_config=None,
                 public_ip_pool=None,
                 region=None,
                 vpc_info=None,
                 max_num_public_ip=None,
                 vpc_info_peered_agent=None,
                 backup_restore_bucket=None,
                 mgw_id=None,
                 nsx_mgr_url=None,
                 psc_management_ip=None,
                 psc_url=None,
                 cgws=None,
                 management_ds=None,
                 custom_properties=None,
                 cloud_password=None,
                 provider='AWS',
                 clusters=None,
                 vc_management_ip=None,
                 sddc_networks=None,
                 cloud_username=None,
                 esx_hosts=None,
                 nsx_mgr_management_ip=None,
                 vc_instance_id=None,
                 esx_cluster_id=None,
                 vc_public_ip=None,
                 vc_url=None,
                 sddc_manifest=None,
                 vxlan_subnet=None,
                 cloud_user_group=None,
                 management_rp=None,
                 sso_domain=None,
                 dns_with_management_vm_private_ip=None,
                ):
        """
        :type  account_link_sddc_config: :class:`list` of :class:`SddcLinkConfig` or ``None``
        :param account_link_sddc_config: 
        :type  public_ip_pool: :class:`list` of :class:`SddcPublicIp` or ``None``
        :param public_ip_pool: 
        :type  region: :class:`str` or ``None``
        :param region: 
        :type  vpc_info: :class:`VpcInfo` or ``None``
        :param vpc_info: 
        :type  max_num_public_ip: :class:`long` or ``None``
        :param max_num_public_ip: maximum number of public IP that user can allocate.
        :type  vpc_info_peered_agent: :class:`VpcInfo` or ``None``
        :param vpc_info_peered_agent: 
        :type  backup_restore_bucket: :class:`str` or ``None``
        :param backup_restore_bucket: 
        :type  mgw_id: :class:`str` or ``None``
        :param mgw_id: Management Gateway Id
        :type  nsx_mgr_url: :class:`str` or ``None``
        :param nsx_mgr_url: URL of the NSX Manager
        :type  psc_management_ip: :class:`str` or ``None``
        :param psc_management_ip: PSC internal management IP
        :type  psc_url: :class:`str` or ``None``
        :param psc_url: URL of the PSC server
        :type  cgws: :class:`list` of :class:`str` or ``None``
        :param cgws: 
        :type  management_ds: :class:`str` or ``None``
        :param management_ds: The ManagedObjectReference of the management Datastore
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  cloud_password: :class:`str` or ``None``
        :param cloud_password: Password for vCenter SDDC administrator
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcResourceConfig.PROVIDER_AWS`
            
             Discriminator for additional properties
        :type  clusters: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param clusters: List of clusters in the SDDC.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`Cluster`. When methods return a value of this class as a
            return value, the attribute will contain all the attributes defined
            in :class:`Cluster`.
        :type  vc_management_ip: :class:`str` or ``None``
        :param vc_management_ip: vCenter internal management IP
        :type  sddc_networks: :class:`list` of :class:`str` or ``None``
        :param sddc_networks: 
        :type  cloud_username: :class:`str` or ``None``
        :param cloud_username: Username for vCenter SDDC administrator
        :type  esx_hosts: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_hosts: 
        :type  nsx_mgr_management_ip: :class:`str` or ``None``
        :param nsx_mgr_management_ip: NSX Manager internal management IP
        :type  vc_instance_id: :class:`str` or ``None``
        :param vc_instance_id: unique id of the vCenter server
        :type  esx_cluster_id: :class:`str` or ``None``
        :param esx_cluster_id: Cluster Id to add ESX workflow
        :type  vc_public_ip: :class:`str` or ``None``
        :param vc_public_ip: vCenter public IP
        :type  vc_url: :class:`str` or ``None``
        :param vc_url: URL of the vCenter server
        :type  sddc_manifest: :class:`SddcManifest` or ``None``
        :param sddc_manifest: 
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  cloud_user_group: :class:`str` or ``None``
        :param cloud_user_group: Group name for vCenter SDDC administrator
        :type  management_rp: :class:`str` or ``None``
        :param management_rp: 
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users
        :type  dns_with_management_vm_private_ip: :class:`bool` or ``None``
        :param dns_with_management_vm_private_ip: if true, use the private IP addresses to register DNS records for
            the management VMs
        """
        self.account_link_sddc_config = account_link_sddc_config
        self.public_ip_pool = public_ip_pool
        self.region = region
        self.vpc_info = vpc_info
        self.max_num_public_ip = max_num_public_ip
        self.vpc_info_peered_agent = vpc_info_peered_agent
        self.backup_restore_bucket = backup_restore_bucket
        self.mgw_id = mgw_id
        self.nsx_mgr_url = nsx_mgr_url
        self.psc_management_ip = psc_management_ip
        self.psc_url = psc_url
        self.cgws = cgws
        self.management_ds = management_ds
        self.custom_properties = custom_properties
        self.cloud_password = cloud_password
        self.provider = provider
        self.clusters = clusters
        self.vc_management_ip = vc_management_ip
        self.sddc_networks = sddc_networks
        self.cloud_username = cloud_username
        self.esx_hosts = esx_hosts
        self.nsx_mgr_management_ip = nsx_mgr_management_ip
        self.vc_instance_id = vc_instance_id
        self.esx_cluster_id = esx_cluster_id
        self.vc_public_ip = vc_public_ip
        self.vc_url = vc_url
        self.sddc_manifest = sddc_manifest
        self.vxlan_subnet = vxlan_subnet
        self.cloud_user_group = cloud_user_group
        self.management_rp = management_rp
        self.sso_domain = sso_domain
        self.dns_with_management_vm_private_ip = dns_with_management_vm_private_ip
        VapiStruct.__init__(self)

AwsSddcResourceConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_sddc_resource_config', {
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcLinkConfig'))),
        'public_ip_pool': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'SddcPublicIp'))),
        'region': type.OptionalType(type.StringType()),
        'vpc_info': type.OptionalType(type.ReferenceType(__name__, 'VpcInfo')),
        'max_num_public_ip': type.OptionalType(type.IntegerType()),
        'vpc_info_peered_agent': type.OptionalType(type.ReferenceType(__name__, 'VpcInfo')),
        'backup_restore_bucket': type.OptionalType(type.StringType()),
        'mgw_id': type.OptionalType(type.StringType()),
        'nsx_mgr_url': type.OptionalType(type.StringType()),
        'psc_management_ip': type.OptionalType(type.StringType()),
        'psc_url': type.OptionalType(type.StringType()),
        'cgws': type.OptionalType(type.ListType(type.StringType())),
        'management_ds': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'cloud_password': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'clusters': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'Cluster')]))),
        'vc_management_ip': type.OptionalType(type.StringType()),
        'sddc_networks': type.OptionalType(type.ListType(type.StringType())),
        'cloud_username': type.OptionalType(type.StringType()),
        'esx_hosts': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'nsx_mgr_management_ip': type.OptionalType(type.StringType()),
        'vc_instance_id': type.OptionalType(type.StringType()),
        'esx_cluster_id': type.OptionalType(type.StringType()),
        'vc_public_ip': type.OptionalType(type.StringType()),
        'vc_url': type.OptionalType(type.StringType()),
        'sddc_manifest': type.OptionalType(type.ReferenceType(__name__, 'SddcManifest')),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'cloud_user_group': type.OptionalType(type.StringType()),
        'management_rp': type.OptionalType(type.StringType()),
        'sso_domain': type.OptionalType(type.StringType()),
        'dns_with_management_vm_private_ip': type.OptionalType(type.BooleanType()),
    },
    AwsSddcResourceConfig,
    False,
    None))



class AwsSubnet(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'connected_account_id': 'connected_account_id',
                            'region_name': 'region_name',
                            'availability_zone': 'availability_zone',
                            'subnet_id': 'subnet_id',
                            'subnet_cidr_block': 'subnet_cidr_block',
                            'is_compatible': 'is_compatible',
                            'vpc_id': 'vpc_id',
                            'vpc_cidr_block': 'vpc_cidr_block',
                            }

    def __init__(self,
                 connected_account_id=None,
                 region_name=None,
                 availability_zone=None,
                 subnet_id=None,
                 subnet_cidr_block=None,
                 is_compatible=None,
                 vpc_id=None,
                 vpc_cidr_block=None,
                ):
        """
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: The connected account ID this subnet is accessible through. This is
            an internal ID formatted as a UUID specific to Skyscraper.
        :type  region_name: :class:`str` or ``None``
        :param region_name: The region this subnet is in, usually in the form of country code,
            general location, and a number (ex. us-west-2).
        :type  availability_zone: :class:`str` or ``None``
        :param availability_zone: The availability zone this subnet is in, which should be the region
            name plus one extra letter (ex. us-west-2a).
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: The subnet ID in AWS, provided in the form 'subnet-######'.
        :type  subnet_cidr_block: :class:`str` or ``None``
        :param subnet_cidr_block: The CIDR block of the subnet, in the form of '#.#.#.#/#'.
        :type  is_compatible: :class:`bool` or ``None``
        :param is_compatible: Flag indicating whether this subnet is compatible. If true, this is
            a valid choice for the customer to deploy a SDDC in.
        :type  vpc_id: :class:`str` or ``None``
        :param vpc_id: The VPC ID the subnet resides in within AWS. Tends to be
            'vpc-#######'.
        :type  vpc_cidr_block: :class:`str` or ``None``
        :param vpc_cidr_block: The CIDR block of the VPC, in the form of '#.#.#.#/#'.
        """
        self.connected_account_id = connected_account_id
        self.region_name = region_name
        self.availability_zone = availability_zone
        self.subnet_id = subnet_id
        self.subnet_cidr_block = subnet_cidr_block
        self.is_compatible = is_compatible
        self.vpc_id = vpc_id
        self.vpc_cidr_block = vpc_cidr_block
        VapiStruct.__init__(self)

AwsSubnet._set_binding_type(type.StructType(
    'com.vmware.vmc.model.aws_subnet', {
        'connected_account_id': type.OptionalType(type.StringType()),
        'region_name': type.OptionalType(type.StringType()),
        'availability_zone': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'subnet_cidr_block': type.OptionalType(type.StringType()),
        'is_compatible': type.OptionalType(type.BooleanType()),
        'vpc_id': type.OptionalType(type.StringType()),
        'vpc_cidr_block': type.OptionalType(type.StringType()),
    },
    AwsSubnet,
    False,
    None))



class CloudProvider(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "CloudProvider"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='CloudProvider',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Name of the Cloud Provider
        """
        self.provider = provider
        VapiStruct.__init__(self)

CloudProvider._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cloud_provider', {
        'provider': type.StringType(),
    },
    CloudProvider,
    False,
    None))



class Cluster(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "Cluster"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    CLUSTER_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    CLUSTER_STATE_ADDING_HOSTS = "ADDING_HOSTS"
    """


    """
    CLUSTER_STATE_READY = "READY"
    """


    """
    CLUSTER_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'cluster_name': 'cluster_name',
                            'esx_host_list': 'esx_host_list',
                            'cluster_id': 'cluster_id',
                            'cluster_state': 'cluster_state',
                            }

    def __init__(self,
                 cluster_name=None,
                 esx_host_list=None,
                 cluster_id='Cluster',
                 cluster_state=None,
                ):
        """
        :type  cluster_name: :class:`str` or ``None``
        :param cluster_name: 
        :type  esx_host_list: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_host_list: 
        :type  cluster_id: :class:`str`
        :param cluster_id: 
        :type  cluster_state: :class:`str` or ``None``
        :param cluster_state: Possible values are: 
            
            * :attr:`Cluster.CLUSTER_STATE_DEPLOYING`
            * :attr:`Cluster.CLUSTER_STATE_ADDING_HOSTS`
            * :attr:`Cluster.CLUSTER_STATE_READY`
            * :attr:`Cluster.CLUSTER_STATE_FAILED`
        """
        self.cluster_name = cluster_name
        self.esx_host_list = esx_host_list
        self.cluster_id = cluster_id
        self.cluster_state = cluster_state
        VapiStruct.__init__(self)

Cluster._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cluster', {
        'cluster_name': type.OptionalType(type.StringType()),
        'esx_host_list': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'cluster_id': type.StringType(),
        'cluster_state': type.OptionalType(type.StringType()),
    },
    Cluster,
    False,
    None))



class ClusterConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'num_hosts': 'num_hosts',
                            }

    def __init__(self,
                 num_hosts=None,
                ):
        """
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        """
        self.num_hosts = num_hosts
        VapiStruct.__init__(self)

ClusterConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.cluster_config', {
        'num_hosts': type.IntegerType(),
    },
    ClusterConfig,
    False,
    None))



class ErrorResponse(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'path': 'path',
                            'retryable': 'retryable',
                            'error_code': 'error_code',
                            'error_messages': 'error_messages',
                            }

    def __init__(self,
                 status=None,
                 path=None,
                 retryable=None,
                 error_code=None,
                 error_messages=None,
                ):
        """
        :type  status: :class:`long`
        :param status: HTTP status code
        :type  path: :class:`str`
        :param path: Originating request URI
        :type  retryable: :class:`bool`
        :param retryable: If true, client should retry operation
        :type  error_code: :class:`str`
        :param error_code: unique error code
        :type  error_messages: :class:`list` of :class:`str`
        :param error_messages: localized error messages
        """
        self.status = status
        self.path = path
        self.retryable = retryable
        self.error_code = error_code
        self.error_messages = error_messages
        VapiStruct.__init__(self)

ErrorResponse._set_binding_type(type.StructType(
    'com.vmware.vmc.model.error_response', {
        'status': type.IntegerType(),
        'path': type.StringType(),
        'retryable': type.BooleanType(),
        'error_code': type.StringType(),
        'error_messages': type.ListType(type.StringType()),
    },
    ErrorResponse,
    False,
    None))



class EsxConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'num_hosts': 'num_hosts',
                            }

    def __init__(self,
                 num_hosts=None,
                ):
        """
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        """
        self.num_hosts = num_hosts
        VapiStruct.__init__(self)

EsxConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.esx_config', {
        'num_hosts': type.IntegerType(),
    },
    EsxConfig,
    False,
    None))



class EsxHost(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "EsxHost"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    ESX_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    ESX_STATE_PROVISIONED = "PROVISIONED"
    """


    """
    ESX_STATE_READY = "READY"
    """


    """
    ESX_STATE_DELETING = "DELETING"
    """


    """
    ESX_STATE_DELETED = "DELETED"
    """


    """
    ESX_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'esx_id': 'esx_id',
                            'hostname': 'hostname',
                            'provider': 'provider',
                            'mac_address': 'mac_address',
                            'custom_properties': 'custom_properties',
                            'esx_state': 'esx_state',
                            }

    def __init__(self,
                 name=None,
                 esx_id=None,
                 hostname=None,
                 provider='EsxHost',
                 mac_address=None,
                 custom_properties=None,
                 esx_state=None,
                ):
        """
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  esx_id: :class:`str` or ``None``
        :param esx_id: 
        :type  hostname: :class:`str` or ``None``
        :param hostname: 
        :type  provider: :class:`str`
        :param provider: 
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: 
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  esx_state: :class:`str` or ``None``
        :param esx_state: Possible values are: 
            
            * :attr:`EsxHost.ESX_STATE_DEPLOYING`
            * :attr:`EsxHost.ESX_STATE_PROVISIONED`
            * :attr:`EsxHost.ESX_STATE_READY`
            * :attr:`EsxHost.ESX_STATE_DELETING`
            * :attr:`EsxHost.ESX_STATE_DELETED`
            * :attr:`EsxHost.ESX_STATE_FAILED`
        """
        self.name = name
        self.esx_id = esx_id
        self.hostname = hostname
        self.provider = provider
        self.mac_address = mac_address
        self.custom_properties = custom_properties
        self.esx_state = esx_state
        VapiStruct.__init__(self)

EsxHost._set_binding_type(type.StructType(
    'com.vmware.vmc.model.esx_host', {
        'name': type.OptionalType(type.StringType()),
        'esx_id': type.OptionalType(type.StringType()),
        'hostname': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'mac_address': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'esx_state': type.OptionalType(type.StringType()),
    },
    EsxHost,
    False,
    None))



class GlcmBundle(VapiStruct):
    """
    the GlcmBundle used for deploying the sddc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            's3Bucket': 's3_bucket',
                            'id': 'id',
                            }

    def __init__(self,
                 s3_bucket=None,
                 id=None,
                ):
        """
        :type  s3_bucket: :class:`str` or ``None``
        :param s3_bucket: the glcmbundle's s3 bucket
        :type  id: :class:`str` or ``None``
        :param id: the glcmbundle's id
        """
        self.s3_bucket = s3_bucket
        self.id = id
        VapiStruct.__init__(self)

GlcmBundle._set_binding_type(type.StructType(
    'com.vmware.vmc.model.glcm_bundle', {
        's3Bucket': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
    },
    GlcmBundle,
    False,
    None))



class Metadata(VapiStruct):
    """
    metadata of the sddc manifest

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'timestamp': 'timestamp',
                            'cycle_id': 'cycle_id',
                            }

    def __init__(self,
                 timestamp=None,
                 cycle_id=None,
                ):
        """
        :type  timestamp: :class:`str` or ``None``
        :param timestamp: the timestamp for the bundle
        :type  cycle_id: :class:`str` or ``None``
        :param cycle_id: the cycle id
        """
        self.timestamp = timestamp
        self.cycle_id = cycle_id
        VapiStruct.__init__(self)

Metadata._set_binding_type(type.StructType(
    'com.vmware.vmc.model.metadata', {
        'timestamp': type.OptionalType(type.StringType()),
        'cycle_id': type.OptionalType(type.StringType()),
    },
    Metadata,
    False,
    None))



class OfferInstancesHolder(VapiStruct):
    """
    Holder for the offer instances.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'on_demand': 'on_demand',
                            'offers': 'offers',
                            }

    def __init__(self,
                 on_demand=None,
                 offers=None,
                ):
        """
        :type  on_demand: :class:`OnDemandOfferInstance`
        :param on_demand: 
        :type  offers: :class:`list` of :class:`TermOfferInstance`
        :param offers: 
        """
        self.on_demand = on_demand
        self.offers = offers
        VapiStruct.__init__(self)

OfferInstancesHolder._set_binding_type(type.StructType(
    'com.vmware.vmc.model.offer_instances_holder', {
        'on_demand': type.ReferenceType(__name__, 'OnDemandOfferInstance'),
        'offers': type.ListType(type.ReferenceType(__name__, 'TermOfferInstance')),
    },
    OfferInstancesHolder,
    False,
    None))



class OnDemandOfferInstance(VapiStruct):
    """
    Holder for the on-demand offer instance.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'product_type': 'product_type',
                            'name': 'name',
                            'currency': 'currency',
                            'region': 'region',
                            'unit_price': 'unit_price',
                            'monthly_cost': 'monthly_cost',
                            'version': 'version',
                            'description': 'description',
                            }

    def __init__(self,
                 product_type=None,
                 name=None,
                 currency=None,
                 region=None,
                 unit_price=None,
                 monthly_cost=None,
                 version=None,
                 description=None,
                ):
        """
        :type  product_type: :class:`str`
        :param product_type: 
        :type  name: :class:`str`
        :param name: 
        :type  currency: :class:`str`
        :param currency: 
        :type  region: :class:`str`
        :param region: 
        :type  unit_price: :class:`str`
        :param unit_price: 
        :type  monthly_cost: :class:`str`
        :param monthly_cost: 
        :type  version: :class:`str`
        :param version: 
        :type  description: :class:`str`
        :param description: 
        """
        self.product_type = product_type
        self.name = name
        self.currency = currency
        self.region = region
        self.unit_price = unit_price
        self.monthly_cost = monthly_cost
        self.version = version
        self.description = description
        VapiStruct.__init__(self)

OnDemandOfferInstance._set_binding_type(type.StructType(
    'com.vmware.vmc.model.on_demand_offer_instance', {
        'product_type': type.StringType(),
        'name': type.StringType(),
        'currency': type.StringType(),
        'region': type.StringType(),
        'unit_price': type.StringType(),
        'monthly_cost': type.StringType(),
        'version': type.StringType(),
        'description': type.StringType(),
    },
    OnDemandOfferInstance,
    False,
    None))



class OrgConfiguration(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "OrgConfiguration"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'provider': 'provider',
                            }

    def __init__(self,
                 provider='OrgConfiguration',
                ):
        """
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`OrgConfiguration.PROVIDER_AWS`
            
             Discriminator for provider specific properties
        """
        self.provider = provider
        VapiStruct.__init__(self)

OrgConfiguration._set_binding_type(type.StructType(
    'com.vmware.vmc.model.org_configuration', {
        'provider': type.StringType(),
    },
    OrgConfiguration,
    False,
    None))



class OrgProperties(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'values': 'values',
                            }

    def __init__(self,
                 values=None,
                ):
        """
        :type  values: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param values: A map of string properties to values.
        """
        self.values = values
        VapiStruct.__init__(self)

OrgProperties._set_binding_type(type.StructType(
    'com.vmware.vmc.model.org_properties', {
        'values': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
    },
    OrgProperties,
    False,
    None))



class Organization(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SLA_CUSTOMER = "CUSTOMER"
    """


    """
    SLA_THIRD_PARTY_PARTNER = "THIRD_PARTY_PARTNER"
    """


    """
    SLA_SECOND_PARTY_PARTNER = "SECOND_PARTY_PARTNER"
    """


    """
    SLA_INTERNAL_CUSTOMER = "INTERNAL_CUSTOMER"
    """


    """
    SLA_VMC_INTERNAL = "VMC_INTERNAL"
    """


    """
    PROJECT_STATE_CREATED = "CREATED"
    """


    """
    PROJECT_STATE_DELETED = "DELETED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'display_name': 'display_name',
                            'name': 'name',
                            'sla': 'sla',
                            'project_state': 'project_state',
                            'properties': 'properties',
                            'cloud_configurations': 'cloud_configurations',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 display_name=None,
                 name=None,
                 sla=None,
                 project_state=None,
                 properties=None,
                 cloud_configurations=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  display_name: :class:`str` or ``None``
        :param display_name: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  sla: :class:`str` or ``None``
        :param sla: Possible values are: 
            
            * :attr:`Organization.SLA_CUSTOMER`
            * :attr:`Organization.SLA_THIRD_PARTY_PARTNER`
            * :attr:`Organization.SLA_SECOND_PARTY_PARTNER`
            * :attr:`Organization.SLA_INTERNAL_CUSTOMER`
            * :attr:`Organization.SLA_VMC_INTERNAL`
            
             SLA to be associated with the org
        :type  project_state: :class:`str` or ``None``
        :param project_state: Possible values are: 
            
            * :attr:`Organization.PROJECT_STATE_CREATED`
            * :attr:`Organization.PROJECT_STATE_DELETED`
        :type  properties: :class:`OrgProperties` or ``None``
        :param properties: 
        :type  cloud_configurations: (:class:`dict` of :class:`str` and :class:`AwsOrgConfiguration`) or ``None``
        :param cloud_configurations: A Map of provider to OrgConfiguration Model.
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.display_name = display_name
        self.name = name
        self.sla = sla
        self.project_state = project_state
        self.properties = properties
        self.cloud_configurations = cloud_configurations
        VapiStruct.__init__(self)

Organization._set_binding_type(type.StructType(
    'com.vmware.vmc.model.organization', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'display_name': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'sla': type.OptionalType(type.StringType()),
        'project_state': type.OptionalType(type.StringType()),
        'properties': type.OptionalType(type.ReferenceType(__name__, 'OrgProperties')),
        'cloud_configurations': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'AwsOrgConfiguration'))),
    },
    Organization,
    False,
    None))



class PopAmiInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    TYPE_CENTOS = "CENTOS"
    """


    """
    TYPE_POP = "POP"
    """


    """



    _canonical_to_pep_names = {
                            'region': 'region',
                            'id': 'id',
                            'name': 'name',
                            'type': 'type',
                            }

    def __init__(self,
                 region=None,
                 id=None,
                 name=None,
                 type=None,
                ):
        """
        :type  region: :class:`str` or ``None``
        :param region: the region of the esx ami
        :type  id: :class:`str` or ``None``
        :param id: the ami id for the esx
        :type  name: :class:`str` or ``None``
        :param name: the name of the esx ami
        :type  type: :class:`str` or ``None``
        :param type: Possible values are: 
            
            * :attr:`PopAmiInfo.TYPE_CENTOS`
            * :attr:`PopAmiInfo.TYPE_POP`
            
             PoP AMI type. CENTOS: a Centos AMI; POP: a PoP AMI.
        """
        self.region = region
        self.id = id
        self.name = name
        self.type = type
        VapiStruct.__init__(self)

PopAmiInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_ami_info', {
        'region': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'type': type.OptionalType(type.StringType()),
    },
    PopAmiInfo,
    False,
    None))



class PopInfo(VapiStruct):
    """
    Present a SDDC PoP information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ami_infos': 'ami_infos',
                            'created_at': 'created_at',
                            'id': 'id',
                            'service_infos': 'service_infos',
                            }

    def __init__(self,
                 ami_infos=None,
                 created_at=None,
                 id=None,
                 service_infos=None,
                ):
        """
        :type  ami_infos: :class:`dict` of :class:`str` and :class:`PopAmiInfo`
        :param ami_infos: A map of [region name of PoP / PoP-AMI]:[PopAmiInfo].
        :type  created_at: :class:`datetime.datetime` or ``None``
        :param created_at: The PopInfo (or PoP AMI) created time. Using ISO 8601 date-time
            pattern. format: date-time
        :type  id: :class:`str` or ``None``
        :param id: UUID of the PopInfo format: UUID
        :type  service_infos: (:class:`dict` of :class:`str` and :class:`PopServiceInfo`) or ``None``
        :param service_infos: A map of [service type]:[PopServiceInfo]
        """
        self.ami_infos = ami_infos
        self.created_at = created_at
        self.id = id
        self.service_infos = service_infos
        VapiStruct.__init__(self)

PopInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_info', {
        'ami_infos': type.MapType(type.StringType(), type.ReferenceType(__name__, 'PopAmiInfo')),
        'created_at': type.OptionalType(type.DateTimeType()),
        'id': type.OptionalType(type.StringType()),
        'service_infos': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'PopServiceInfo'))),
    },
    PopInfo,
    False,
    None))



class PopServiceInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SERVICE_OS = "OS"
    """


    """
    SERVICE_AGENT = "AGENT"
    """


    """
    SERVICE_GLCM = "GLCM"
    """


    """
    SERVICE_S3_ADAPTER = "S3_ADAPTER"
    """


    """
    SERVICE_JRE = "JRE"
    """


    """
    SERVICE_DOCKER = "DOCKER"
    """


    """
    SERVICE_AIDE = "AIDE"
    """


    """
    SERVICE_RTS = "RTS"
    """


    """
    SERVICE_FM_MANAGEMENT = "FM_MANAGEMENT"
    """


    """
    SERVICE_FM_LOG_COLLECTOR = "FM_LOG_COLLECTOR"
    """


    """
    SERVICE_FM_METRICS_COLLECTOR = "FM_METRICS_COLLECTOR"
    """


    """
    SERVICE_BRE = "BRE"
    """


    """
    SERVICE_BRF = "BRF"
    """


    """
    SERVICE_REVERSE_PROXY = "REVERSE_PROXY"
    """


    """
    SERVICE_FORWARD_PROXY = "FORWARD_PROXY"
    """


    """
    SERVICE_DNS = "DNS"
    """


    """
    SERVICE_NTP = "NTP"
    """


    """
    SERVICE_LOGZ_LOG_COLLECTOR = "LOGZ_LOG_COLLECTOR"
    """


    """



    _canonical_to_pep_names = {
                            'cln': 'cln',
                            'version': 'version',
                            'build': 'build',
                            'service': 'service',
                            }

    def __init__(self,
                 cln=None,
                 version=None,
                 build=None,
                 service=None,
                ):
        """
        :type  cln: :class:`str` or ``None``
        :param cln: The service change set number.
        :type  version: :class:`str` or ``None``
        :param version: The service API version.
        :type  build: :class:`str` or ``None``
        :param build: The service build number.
        :type  service: :class:`str`
        :param service: Possible values are: 
            
            * :attr:`PopServiceInfo.SERVICE_OS`
            * :attr:`PopServiceInfo.SERVICE_AGENT`
            * :attr:`PopServiceInfo.SERVICE_GLCM`
            * :attr:`PopServiceInfo.SERVICE_S3_ADAPTER`
            * :attr:`PopServiceInfo.SERVICE_JRE`
            * :attr:`PopServiceInfo.SERVICE_DOCKER`
            * :attr:`PopServiceInfo.SERVICE_AIDE`
            * :attr:`PopServiceInfo.SERVICE_RTS`
            * :attr:`PopServiceInfo.SERVICE_FM_MANAGEMENT`
            * :attr:`PopServiceInfo.SERVICE_FM_LOG_COLLECTOR`
            * :attr:`PopServiceInfo.SERVICE_FM_METRICS_COLLECTOR`
            * :attr:`PopServiceInfo.SERVICE_BRE`
            * :attr:`PopServiceInfo.SERVICE_BRF`
            * :attr:`PopServiceInfo.SERVICE_REVERSE_PROXY`
            * :attr:`PopServiceInfo.SERVICE_FORWARD_PROXY`
            * :attr:`PopServiceInfo.SERVICE_DNS`
            * :attr:`PopServiceInfo.SERVICE_NTP`
            * :attr:`PopServiceInfo.SERVICE_LOGZ_LOG_COLLECTOR`
            
             An enum of PoP related services (including os platform and JRE).
        """
        self.cln = cln
        self.version = version
        self.build = build
        self.service = service
        VapiStruct.__init__(self)

PopServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.pop_service_info', {
        'cln': type.OptionalType(type.StringType()),
        'version': type.OptionalType(type.StringType()),
        'build': type.OptionalType(type.StringType()),
        'service': type.StringType(),
    },
    PopServiceInfo,
    False,
    None))



class Sddc(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    SDDC_STATE_DEPLOYING = "DEPLOYING"
    """


    """
    SDDC_STATE_READY = "READY"
    """


    """
    SDDC_STATE_DELETING = "DELETING"
    """


    """
    SDDC_STATE_DELETION_FAILED = "DELETION_FAILED"
    """


    """
    SDDC_STATE_DELETED = "DELETED"
    """


    """
    SDDC_STATE_FAILED = "FAILED"
    """


    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'resource_config': 'resource_config',
                            'org_id': 'org_id',
                            'name': 'name',
                            'sddc_state': 'sddc_state',
                            'provider': 'provider',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 resource_config=None,
                 org_id=None,
                 name=None,
                 sddc_state=None,
                 provider=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  resource_config: :class:`AwsSddcResourceConfig` or ``None``
        :param resource_config: 
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  name: :class:`str` or ``None``
        :param name: name for SDDC
        :type  sddc_state: :class:`str` or ``None``
        :param sddc_state: Possible values are: 
            
            * :attr:`Sddc.SDDC_STATE_DEPLOYING`
            * :attr:`Sddc.SDDC_STATE_READY`
            * :attr:`Sddc.SDDC_STATE_DELETING`
            * :attr:`Sddc.SDDC_STATE_DELETION_FAILED`
            * :attr:`Sddc.SDDC_STATE_DELETED`
            * :attr:`Sddc.SDDC_STATE_FAILED`
        :type  provider: :class:`str` or ``None``
        :param provider: Possible values are: 
            
            * :attr:`Sddc.PROVIDER_AWS`
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.resource_config = resource_config
        self.org_id = org_id
        self.name = name
        self.sddc_state = sddc_state
        self.provider = provider
        VapiStruct.__init__(self)

Sddc._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'resource_config': type.OptionalType(type.ReferenceType(__name__, 'AwsSddcResourceConfig')),
        'org_id': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'sddc_state': type.OptionalType(type.StringType()),
        'provider': type.OptionalType(type.StringType()),
    },
    Sddc,
    False,
    None))



class SddcAllocatePublicIpSpec(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'count': 'count',
                            'private_ips': 'private_ips',
                            'names': 'names',
                            }

    def __init__(self,
                 count=None,
                 private_ips=None,
                 names=None,
                ):
        """
        :type  count: :class:`long`
        :param count: 
        :type  private_ips: :class:`list` of :class:`str` or ``None``
        :param private_ips: List of workload VM private IPs to be assigned the public IP just
            allocated.
        :type  names: :class:`list` of :class:`str` or ``None``
        :param names: List of names for the workload VM public IP assignment.
        """
        self.count = count
        self.private_ips = private_ips
        self.names = names
        VapiStruct.__init__(self)

SddcAllocatePublicIpSpec._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_allocate_public_ip_spec', {
        'count': type.IntegerType(),
        'private_ips': type.OptionalType(type.ListType(type.StringType())),
        'names': type.OptionalType(type.ListType(type.StringType())),
    },
    SddcAllocatePublicIpSpec,
    False,
    None))



class SddcConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "SddcConfig"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'name': 'name',
                            'account_link_sddc_config': 'account_link_sddc_config',
                            'vxlan_subnet': 'vxlan_subnet',
                            'vpc_cidr': 'vpc_cidr',
                            'provider': 'provider',
                            'sso_domain': 'sso_domain',
                            'num_hosts': 'num_hosts',
                            }

    def __init__(self,
                 name=None,
                 account_link_sddc_config=None,
                 vxlan_subnet=None,
                 vpc_cidr=None,
                 provider='SddcConfig',
                 sso_domain=None,
                 num_hosts=None,
                ):
        """
        :type  name: :class:`str`
        :param name: 
        :type  account_link_sddc_config: :class:`list` of :class:`AccountLinkSddcConfig` or ``None``
        :param account_link_sddc_config: A list of the SDDC linkg configurations to use.
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: AWS VPC IP range. Only prefix of 16 or 20 is currently supported.
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcConfig.PROVIDER_AWS`
            
            Determines what additional properties are available based on cloud
            provider.
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users. If not specified,
            vmc.local will be used.
        :type  num_hosts: :class:`long`
        :param num_hosts: 
        """
        self.name = name
        self.account_link_sddc_config = account_link_sddc_config
        self.vxlan_subnet = vxlan_subnet
        self.vpc_cidr = vpc_cidr
        self.provider = provider
        self.sso_domain = sso_domain
        self.num_hosts = num_hosts
        VapiStruct.__init__(self)

SddcConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_config', {
        'name': type.StringType(),
        'account_link_sddc_config': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AccountLinkSddcConfig'))),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'vpc_cidr': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'sso_domain': type.OptionalType(type.StringType()),
        'num_hosts': type.IntegerType(),
    },
    SddcConfig,
    False,
    None))



class SddcLinkConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'customer_subnet_ids': 'customer_subnet_ids',
                            'connected_account_id': 'connected_account_id',
                            }

    def __init__(self,
                 customer_subnet_ids=None,
                 connected_account_id=None,
                ):
        """
        :type  customer_subnet_ids: :class:`list` of :class:`str` or ``None``
        :param customer_subnet_ids: 
        :type  connected_account_id: :class:`str` or ``None``
        :param connected_account_id: Determines which connected customer account to link to
        """
        self.customer_subnet_ids = customer_subnet_ids
        self.connected_account_id = connected_account_id
        VapiStruct.__init__(self)

SddcLinkConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_link_config', {
        'customer_subnet_ids': type.OptionalType(type.ListType(type.StringType())),
        'connected_account_id': type.OptionalType(type.StringType()),
    },
    SddcLinkConfig,
    False,
    None))



class SddcManifest(VapiStruct):
    """
    Describes software components of the installed SDDC

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vmc_version': 'vmc_version',
                            'glcm_bundle': 'glcm_bundle',
                            'pop_info': 'pop_info',
                            'vmc_internal_version': 'vmc_internal_version',
                            'esx_ami': 'esx_ami',
                            'metadata': 'metadata',
                            }

    def __init__(self,
                 vmc_version=None,
                 glcm_bundle=None,
                 pop_info=None,
                 vmc_internal_version=None,
                 esx_ami=None,
                 metadata=None,
                ):
        """
        :type  vmc_version: :class:`str` or ``None``
        :param vmc_version: the vmcVersion of the sddc for display
        :type  glcm_bundle: :class:`GlcmBundle` or ``None``
        :param glcm_bundle: 
        :type  pop_info: :class:`PopInfo` or ``None``
        :param pop_info: 
        :type  vmc_internal_version: :class:`str` or ``None``
        :param vmc_internal_version: the vmcInternalVersion of the sddc for internal use
        :type  esx_ami: :class:`AmiInfo` or ``None``
        :param esx_ami: 
        :type  metadata: :class:`Metadata` or ``None``
        :param metadata: 
        """
        self.vmc_version = vmc_version
        self.glcm_bundle = glcm_bundle
        self.pop_info = pop_info
        self.vmc_internal_version = vmc_internal_version
        self.esx_ami = esx_ami
        self.metadata = metadata
        VapiStruct.__init__(self)

SddcManifest._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_manifest', {
        'vmc_version': type.OptionalType(type.StringType()),
        'glcm_bundle': type.OptionalType(type.ReferenceType(__name__, 'GlcmBundle')),
        'pop_info': type.OptionalType(type.ReferenceType(__name__, 'PopInfo')),
        'vmc_internal_version': type.OptionalType(type.StringType()),
        'esx_ami': type.OptionalType(type.ReferenceType(__name__, 'AmiInfo')),
        'metadata': type.OptionalType(type.ReferenceType(__name__, 'Metadata')),
    },
    SddcManifest,
    False,
    None))



class SddcPublicIp(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'public_ip': 'public_ip',
                            'name': 'name',
                            'allocation_id': 'allocation_id',
                            'dnat_rule_id': 'dnat_rule_id',
                            'associated_private_ip': 'associated_private_ip',
                            'snat_rule_id': 'snat_rule_id',
                            }

    def __init__(self,
                 public_ip=None,
                 name=None,
                 allocation_id=None,
                 dnat_rule_id=None,
                 associated_private_ip=None,
                 snat_rule_id=None,
                ):
        """
        :type  public_ip: :class:`str`
        :param public_ip: 
        :type  name: :class:`str` or ``None``
        :param name: 
        :type  allocation_id: :class:`str` or ``None``
        :param allocation_id: 
        :type  dnat_rule_id: :class:`str` or ``None``
        :param dnat_rule_id: 
        :type  associated_private_ip: :class:`str` or ``None``
        :param associated_private_ip: 
        :type  snat_rule_id: :class:`str` or ``None``
        :param snat_rule_id: 
        """
        self.public_ip = public_ip
        self.name = name
        self.allocation_id = allocation_id
        self.dnat_rule_id = dnat_rule_id
        self.associated_private_ip = associated_private_ip
        self.snat_rule_id = snat_rule_id
        VapiStruct.__init__(self)

SddcPublicIp._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_public_ip', {
        'public_ip': type.StringType(),
        'name': type.OptionalType(type.StringType()),
        'allocation_id': type.OptionalType(type.StringType()),
        'dnat_rule_id': type.OptionalType(type.StringType()),
        'associated_private_ip': type.OptionalType(type.StringType()),
        'snat_rule_id': type.OptionalType(type.StringType()),
    },
    SddcPublicIp,
    False,
    None))



class SddcResourceConfig(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    _TYPE_IDENTIFIER = "SddcResourceConfig"
    """
    Identifier denoting this class, when it is used in polymorphic context. 

    This value should be assigned to the attribute which is used to discriminate
    the actual type used in the polymorphic context.

    """
    PROVIDER_AWS = "AWS"
    """


    """



    _canonical_to_pep_names = {
                            'mgw_id': 'mgw_id',
                            'nsx_mgr_url': 'nsx_mgr_url',
                            'psc_management_ip': 'psc_management_ip',
                            'psc_url': 'psc_url',
                            'cgws': 'cgws',
                            'management_ds': 'management_ds',
                            'custom_properties': 'custom_properties',
                            'cloud_password': 'cloud_password',
                            'provider': 'provider',
                            'clusters': 'clusters',
                            'vc_management_ip': 'vc_management_ip',
                            'sddc_networks': 'sddc_networks',
                            'cloud_username': 'cloud_username',
                            'esx_hosts': 'esx_hosts',
                            'nsx_mgr_management_ip': 'nsx_mgr_management_ip',
                            'vc_instance_id': 'vc_instance_id',
                            'esx_cluster_id': 'esx_cluster_id',
                            'vc_public_ip': 'vc_public_ip',
                            'vc_url': 'vc_url',
                            'sddc_manifest': 'sddc_manifest',
                            'vxlan_subnet': 'vxlan_subnet',
                            'cloud_user_group': 'cloud_user_group',
                            'management_rp': 'management_rp',
                            'sso_domain': 'sso_domain',
                            'dns_with_management_vm_private_ip': 'dns_with_management_vm_private_ip',
                            }

    def __init__(self,
                 mgw_id=None,
                 nsx_mgr_url=None,
                 psc_management_ip=None,
                 psc_url=None,
                 cgws=None,
                 management_ds=None,
                 custom_properties=None,
                 cloud_password=None,
                 provider='SddcResourceConfig',
                 clusters=None,
                 vc_management_ip=None,
                 sddc_networks=None,
                 cloud_username=None,
                 esx_hosts=None,
                 nsx_mgr_management_ip=None,
                 vc_instance_id=None,
                 esx_cluster_id=None,
                 vc_public_ip=None,
                 vc_url=None,
                 sddc_manifest=None,
                 vxlan_subnet=None,
                 cloud_user_group=None,
                 management_rp=None,
                 sso_domain=None,
                 dns_with_management_vm_private_ip=None,
                ):
        """
        :type  mgw_id: :class:`str` or ``None``
        :param mgw_id: Management Gateway Id
        :type  nsx_mgr_url: :class:`str` or ``None``
        :param nsx_mgr_url: URL of the NSX Manager
        :type  psc_management_ip: :class:`str` or ``None``
        :param psc_management_ip: PSC internal management IP
        :type  psc_url: :class:`str` or ``None``
        :param psc_url: URL of the PSC server
        :type  cgws: :class:`list` of :class:`str` or ``None``
        :param cgws: 
        :type  management_ds: :class:`str` or ``None``
        :param management_ds: The ManagedObjectReference of the management Datastore
        :type  custom_properties: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
        :param custom_properties: 
        :type  cloud_password: :class:`str` or ``None``
        :param cloud_password: Password for vCenter SDDC administrator
        :type  provider: :class:`str`
        :param provider: Possible values are: 
            
            * :attr:`SddcResourceConfig.PROVIDER_AWS`
            
             Discriminator for additional properties
        :type  clusters: :class:`list` of :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param clusters: List of clusters in the SDDC.
            When clients pass a value of this class as a parameter, the
            attribute must contain all the attributes defined in
            :class:`Cluster`. When methods return a value of this class as a
            return value, the attribute will contain all the attributes defined
            in :class:`Cluster`.
        :type  vc_management_ip: :class:`str` or ``None``
        :param vc_management_ip: vCenter internal management IP
        :type  sddc_networks: :class:`list` of :class:`str` or ``None``
        :param sddc_networks: 
        :type  cloud_username: :class:`str` or ``None``
        :param cloud_username: Username for vCenter SDDC administrator
        :type  esx_hosts: :class:`list` of :class:`AwsEsxHost` or ``None``
        :param esx_hosts: 
        :type  nsx_mgr_management_ip: :class:`str` or ``None``
        :param nsx_mgr_management_ip: NSX Manager internal management IP
        :type  vc_instance_id: :class:`str` or ``None``
        :param vc_instance_id: unique id of the vCenter server
        :type  esx_cluster_id: :class:`str` or ``None``
        :param esx_cluster_id: Cluster Id to add ESX workflow
        :type  vc_public_ip: :class:`str` or ``None``
        :param vc_public_ip: vCenter public IP
        :type  vc_url: :class:`str` or ``None``
        :param vc_url: URL of the vCenter server
        :type  sddc_manifest: :class:`SddcManifest` or ``None``
        :param sddc_manifest: 
        :type  vxlan_subnet: :class:`str` or ``None``
        :param vxlan_subnet: VXLAN IP subnet
        :type  cloud_user_group: :class:`str` or ``None``
        :param cloud_user_group: Group name for vCenter SDDC administrator
        :type  management_rp: :class:`str` or ``None``
        :param management_rp: 
        :type  sso_domain: :class:`str` or ``None``
        :param sso_domain: The SSO domain name to use for vSphere users
        :type  dns_with_management_vm_private_ip: :class:`bool` or ``None``
        :param dns_with_management_vm_private_ip: if true, use the private IP addresses to register DNS records for
            the management VMs
        """
        self.mgw_id = mgw_id
        self.nsx_mgr_url = nsx_mgr_url
        self.psc_management_ip = psc_management_ip
        self.psc_url = psc_url
        self.cgws = cgws
        self.management_ds = management_ds
        self.custom_properties = custom_properties
        self.cloud_password = cloud_password
        self.provider = provider
        self.clusters = clusters
        self.vc_management_ip = vc_management_ip
        self.sddc_networks = sddc_networks
        self.cloud_username = cloud_username
        self.esx_hosts = esx_hosts
        self.nsx_mgr_management_ip = nsx_mgr_management_ip
        self.vc_instance_id = vc_instance_id
        self.esx_cluster_id = esx_cluster_id
        self.vc_public_ip = vc_public_ip
        self.vc_url = vc_url
        self.sddc_manifest = sddc_manifest
        self.vxlan_subnet = vxlan_subnet
        self.cloud_user_group = cloud_user_group
        self.management_rp = management_rp
        self.sso_domain = sso_domain
        self.dns_with_management_vm_private_ip = dns_with_management_vm_private_ip
        VapiStruct.__init__(self)

SddcResourceConfig._set_binding_type(type.StructType(
    'com.vmware.vmc.model.sddc_resource_config', {
        'mgw_id': type.OptionalType(type.StringType()),
        'nsx_mgr_url': type.OptionalType(type.StringType()),
        'psc_management_ip': type.OptionalType(type.StringType()),
        'psc_url': type.OptionalType(type.StringType()),
        'cgws': type.OptionalType(type.ListType(type.StringType())),
        'management_ds': type.OptionalType(type.StringType()),
        'custom_properties': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
        'cloud_password': type.OptionalType(type.StringType()),
        'provider': type.StringType(),
        'clusters': type.OptionalType(type.ListType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType(__name__, 'Cluster')]))),
        'vc_management_ip': type.OptionalType(type.StringType()),
        'sddc_networks': type.OptionalType(type.ListType(type.StringType())),
        'cloud_username': type.OptionalType(type.StringType()),
        'esx_hosts': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AwsEsxHost'))),
        'nsx_mgr_management_ip': type.OptionalType(type.StringType()),
        'vc_instance_id': type.OptionalType(type.StringType()),
        'esx_cluster_id': type.OptionalType(type.StringType()),
        'vc_public_ip': type.OptionalType(type.StringType()),
        'vc_url': type.OptionalType(type.StringType()),
        'sddc_manifest': type.OptionalType(type.ReferenceType(__name__, 'SddcManifest')),
        'vxlan_subnet': type.OptionalType(type.StringType()),
        'cloud_user_group': type.OptionalType(type.StringType()),
        'management_rp': type.OptionalType(type.StringType()),
        'sso_domain': type.OptionalType(type.StringType()),
        'dns_with_management_vm_private_ip': type.OptionalType(type.BooleanType()),
    },
    SddcResourceConfig,
    False,
    None))



class SubscriptionDetails(VapiStruct):
    """
    details of a subscription

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_CREATED = "CREATED"
    """


    """
    STATUS_ACTIVATED = "ACTIVATED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """
    STATUS_CANCELLED = "CANCELLED"
    """


    """
    STATUS_EXPIRED = "EXPIRED"
    """


    """
    STATUS_PENDING_PROVISIONING = "PENDING_PROVISIONING"
    """


    """



    _canonical_to_pep_names = {
                            'status': 'status',
                            'anniversary_billing_date': 'anniversary_billing_date',
                            'end_date': 'end_date',
                            'auto_renewed_allowed': 'auto_renewed_allowed',
                            'description': 'description',
                            'commitment_term': 'commitment_term',
                            'csp_subscription_id': 'csp_subscription_id',
                            'billing_subscription_id': 'billing_subscription_id',
                            'commitment_term_uom': 'commitment_term_uom',
                            'offer_version': 'offer_version',
                            'region': 'region',
                            'offer_name': 'offer_name',
                            'offer_type': 'offer_type',
                            'start_date': 'start_date',
                            'quantity': 'quantity',
                            }

    def __init__(self,
                 status=None,
                 anniversary_billing_date=None,
                 end_date=None,
                 auto_renewed_allowed=None,
                 description=None,
                 commitment_term=None,
                 csp_subscription_id=None,
                 billing_subscription_id=None,
                 commitment_term_uom=None,
                 offer_version=None,
                 region=None,
                 offer_name=None,
                 offer_type=None,
                 start_date=None,
                 quantity=None,
                ):
        """
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`SubscriptionDetails.STATUS_CREATED`
            * :attr:`SubscriptionDetails.STATUS_ACTIVATED`
            * :attr:`SubscriptionDetails.STATUS_FAILED`
            * :attr:`SubscriptionDetails.STATUS_CANCELLED`
            * :attr:`SubscriptionDetails.STATUS_EXPIRED`
            * :attr:`SubscriptionDetails.STATUS_PENDING_PROVISIONING`
        :type  anniversary_billing_date: :class:`str` or ``None``
        :param anniversary_billing_date: 
        :type  end_date: :class:`str` or ``None``
        :param end_date: 
        :type  auto_renewed_allowed: :class:`str` or ``None``
        :param auto_renewed_allowed: 
        :type  description: :class:`str` or ``None``
        :param description: 
        :type  commitment_term: :class:`str` or ``None``
        :param commitment_term: 
        :type  csp_subscription_id: :class:`str` or ``None``
        :param csp_subscription_id: 
        :type  billing_subscription_id: :class:`str` or ``None``
        :param billing_subscription_id: 
        :type  commitment_term_uom: :class:`str` or ``None``
        :param commitment_term_uom: unit of measurment for commitment term
        :type  offer_version: :class:`str` or ``None``
        :param offer_version: 
        :type  region: :class:`str` or ``None``
        :param region: 
        :type  offer_name: :class:`str` or ``None``
        :param offer_name: 
        :type  offer_type: :class:`OfferType` or ``None``
        :param offer_type: 
        :type  start_date: :class:`str` or ``None``
        :param start_date: 
        :type  quantity: :class:`str` or ``None``
        :param quantity: 
        """
        self.status = status
        self.anniversary_billing_date = anniversary_billing_date
        self.end_date = end_date
        self.auto_renewed_allowed = auto_renewed_allowed
        self.description = description
        self.commitment_term = commitment_term
        self.csp_subscription_id = csp_subscription_id
        self.billing_subscription_id = billing_subscription_id
        self.commitment_term_uom = commitment_term_uom
        self.offer_version = offer_version
        self.region = region
        self.offer_name = offer_name
        self.offer_type = offer_type
        self.start_date = start_date
        self.quantity = quantity
        VapiStruct.__init__(self)

SubscriptionDetails._set_binding_type(type.StructType(
    'com.vmware.vmc.model.subscription_details', {
        'status': type.OptionalType(type.StringType()),
        'anniversary_billing_date': type.OptionalType(type.StringType()),
        'end_date': type.OptionalType(type.StringType()),
        'auto_renewed_allowed': type.OptionalType(type.StringType()),
        'description': type.OptionalType(type.StringType()),
        'commitment_term': type.OptionalType(type.StringType()),
        'csp_subscription_id': type.OptionalType(type.StringType()),
        'billing_subscription_id': type.OptionalType(type.StringType()),
        'commitment_term_uom': type.OptionalType(type.StringType()),
        'offer_version': type.OptionalType(type.StringType()),
        'region': type.OptionalType(type.StringType()),
        'offer_name': type.OptionalType(type.StringType()),
        'offer_type': type.OptionalType(type.ReferenceType(__name__, 'OfferType')),
        'start_date': type.OptionalType(type.StringType()),
        'quantity': type.OptionalType(type.StringType()),
    },
    SubscriptionDetails,
    False,
    None))



class SubscriptionRequest(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'offer_version': 'offer_version',
                            'product_type': 'product_type',
                            'region': 'region',
                            'commitment_term': 'commitment_term',
                            'offer_name': 'offer_name',
                            'quantity': 'quantity',
                            }

    def __init__(self,
                 offer_version=None,
                 product_type=None,
                 region=None,
                 commitment_term=None,
                 offer_name=None,
                 quantity=None,
                ):
        """
        :type  offer_version: :class:`str`
        :param offer_version: 
        :type  product_type: :class:`str`
        :param product_type: 
        :type  region: :class:`str`
        :param region: 
        :type  commitment_term: :class:`str`
        :param commitment_term: 
        :type  offer_name: :class:`str`
        :param offer_name: 
        :type  quantity: :class:`long`
        :param quantity: 
        """
        self.offer_version = offer_version
        self.product_type = product_type
        self.region = region
        self.commitment_term = commitment_term
        self.offer_name = offer_name
        self.quantity = quantity
        VapiStruct.__init__(self)

SubscriptionRequest._set_binding_type(type.StructType(
    'com.vmware.vmc.model.subscription_request', {
        'offer_version': type.StringType(),
        'product_type': type.StringType(),
        'region': type.StringType(),
        'commitment_term': type.StringType(),
        'offer_name': type.StringType(),
        'quantity': type.IntegerType(),
    },
    SubscriptionRequest,
    False,
    None))



class Task(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_STARTED = "STARTED"
    """


    """
    STATUS_CANCELING = "CANCELING"
    """


    """
    STATUS_FINISHED = "FINISHED"
    """


    """
    STATUS_FAILED = "FAILED"
    """


    """
    STATUS_CANCELED = "CANCELED"
    """


    """



    _canonical_to_pep_names = {
                            'updated': 'updated',
                            'user_id': 'user_id',
                            'updated_by_user_id': 'updated_by_user_id',
                            'created': 'created',
                            'version': 'version',
                            'updated_by_user_name': 'updated_by_user_name',
                            'user_name': 'user_name',
                            'id': 'id',
                            'status': 'status',
                            'recorded_features': 'recorded_features',
                            'resource_id': 'resource_id',
                            'start_time': 'start_time',
                            'retries': 'retries',
                            'task_type': 'task_type',
                            'task_progress_phases': 'task_progress_phases',
                            'error_message': 'error_message',
                            'org_id': 'org_id',
                            'progress_percent': 'progress_percent',
                            'estimated_remaining_minutes': 'estimated_remaining_minutes',
                            'params': 'params',
                            'end_time': 'end_time',
                            'phase_in_progress': 'phase_in_progress',
                            'task_version': 'task_version',
                            'resource_type': 'resource_type',
                            'sub_status': 'sub_status',
                            }

    def __init__(self,
                 updated=None,
                 user_id=None,
                 updated_by_user_id=None,
                 created=None,
                 version=None,
                 updated_by_user_name=None,
                 user_name=None,
                 id=None,
                 status=None,
                 recorded_features=None,
                 resource_id=None,
                 start_time=None,
                 retries=None,
                 task_type=None,
                 task_progress_phases=None,
                 error_message=None,
                 org_id=None,
                 progress_percent=None,
                 estimated_remaining_minutes=None,
                 params=None,
                 end_time=None,
                 phase_in_progress=None,
                 task_version=None,
                 resource_type=None,
                 sub_status=None,
                ):
        """
        :type  updated: :class:`datetime.datetime`
        :param updated: 
        :type  user_id: :class:`str`
        :param user_id: User id that last updated this record
        :type  updated_by_user_id: :class:`str`
        :param updated_by_user_id: User id that last updated this record
        :type  created: :class:`datetime.datetime`
        :param created: 
        :type  version: :class:`long`
        :param version: Version of this entity format: int32
        :type  updated_by_user_name: :class:`str`
        :param updated_by_user_name: User name that last updated this record
        :type  user_name: :class:`str`
        :param user_name: User name that last updated this record
        :type  id: :class:`str`
        :param id: Unique ID for this entity
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`Task.STATUS_STARTED`
            * :attr:`Task.STATUS_CANCELING`
            * :attr:`Task.STATUS_FINISHED`
            * :attr:`Task.STATUS_FAILED`
            * :attr:`Task.STATUS_CANCELED`
        :type  recorded_features: :class:`TaskRecordedFeatures` or ``None``
        :param recorded_features: 
        :type  resource_id: :class:`str` or ``None``
        :param resource_id: UUID of resources task is acting upon
        :type  start_time: :class:`str` or ``None``
        :param start_time: 
        :type  retries: :class:`long` or ``None``
        :param retries: 
        :type  task_type: :class:`str` or ``None``
        :param task_type: 
        :type  task_progress_phases: :class:`list` of :class:`TaskProgressPhase` or ``None``
        :param task_progress_phases: Task progress phases involved in current task execution
        :type  error_message: :class:`str` or ``None``
        :param error_message: 
        :type  org_id: :class:`str` or ``None``
        :param org_id: 
        :type  progress_percent: :class:`long` or ``None``
        :param progress_percent: Estimated progress percentage the task executed format: int32
        :type  estimated_remaining_minutes: :class:`long` or ``None``
        :param estimated_remaining_minutes: Estimated remaining time in minute of the task execution, < 0 means
            no estimation for the task. format: int32
        :type  params: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param params: 
        :type  end_time: :class:`datetime.datetime` or ``None``
        :param end_time: 
        :type  phase_in_progress: :class:`str` or ``None``
        :param phase_in_progress: The current in progress phase ID in the task execution, if none in
            progress, empty string returned.
        :type  task_version: :class:`str` or ``None``
        :param task_version: 
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Type of resource being acted upon
        :type  sub_status: :class:`str` or ``None``
        :param sub_status: 
        """
        self.updated = updated
        self.user_id = user_id
        self.updated_by_user_id = updated_by_user_id
        self.created = created
        self.version = version
        self.updated_by_user_name = updated_by_user_name
        self.user_name = user_name
        self.id = id
        self.status = status
        self.recorded_features = recorded_features
        self.resource_id = resource_id
        self.start_time = start_time
        self.retries = retries
        self.task_type = task_type
        self.task_progress_phases = task_progress_phases
        self.error_message = error_message
        self.org_id = org_id
        self.progress_percent = progress_percent
        self.estimated_remaining_minutes = estimated_remaining_minutes
        self.params = params
        self.end_time = end_time
        self.phase_in_progress = phase_in_progress
        self.task_version = task_version
        self.resource_type = resource_type
        self.sub_status = sub_status
        VapiStruct.__init__(self)

Task._set_binding_type(type.StructType(
    'com.vmware.vmc.model.task', {
        'updated': type.DateTimeType(),
        'user_id': type.StringType(),
        'updated_by_user_id': type.StringType(),
        'created': type.DateTimeType(),
        'version': type.IntegerType(),
        'updated_by_user_name': type.StringType(),
        'user_name': type.StringType(),
        'id': type.StringType(),
        'status': type.OptionalType(type.StringType()),
        'recorded_features': type.OptionalType(type.ReferenceType(__name__, 'TaskRecordedFeatures')),
        'resource_id': type.OptionalType(type.StringType()),
        'start_time': type.OptionalType(type.StringType()),
        'retries': type.OptionalType(type.IntegerType()),
        'task_type': type.OptionalType(type.StringType()),
        'task_progress_phases': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'TaskProgressPhase'))),
        'error_message': type.OptionalType(type.StringType()),
        'org_id': type.OptionalType(type.StringType()),
        'progress_percent': type.OptionalType(type.IntegerType()),
        'estimated_remaining_minutes': type.OptionalType(type.IntegerType()),
        'params': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'end_time': type.OptionalType(type.DateTimeType()),
        'phase_in_progress': type.OptionalType(type.StringType()),
        'task_version': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
        'sub_status': type.OptionalType(type.StringType()),
    },
    Task,
    False,
    None))



class TaskProgressPhase(VapiStruct):
    """
    A task progress can be (but does NOT have to be) divided to more meaningful
    progress phases.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'id': 'id',
                            'name': 'name',
                            'progress_percent': 'progress_percent',
                            }

    def __init__(self,
                 id=None,
                 name=None,
                 progress_percent=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of the task progress phase
        :type  name: :class:`str`
        :param name: The display name of the task progress phase
        :type  progress_percent: :class:`long`
        :param progress_percent: The percentage of the phase that has completed format: int32
        """
        self.id = id
        self.name = name
        self.progress_percent = progress_percent
        VapiStruct.__init__(self)

TaskProgressPhase._set_binding_type(type.StructType(
    'com.vmware.vmc.model.task_progress_phase', {
        'id': type.StringType(),
        'name': type.StringType(),
        'progress_percent': type.IntegerType(),
    },
    TaskProgressPhase,
    False,
    None))



class TaskRecordedFeatures(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'values': 'values',
                            }

    def __init__(self,
                 values=None,
                ):
        """
        :type  values: (:class:`dict` of :class:`str` and :class:`bool`) or ``None``
        :param values: A map of string properties to boolean values. This structure holds
            the feature state
        """
        self.values = values
        VapiStruct.__init__(self)

TaskRecordedFeatures._set_binding_type(type.StructType(
    'com.vmware.vmc.model.task_recorded_features', {
        'values': type.OptionalType(type.MapType(type.StringType(), type.BooleanType())),
    },
    TaskRecordedFeatures,
    False,
    None))



class TermOfferInstance(VapiStruct):
    """
    Holder for the term offer instances.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'product_type': 'product_type',
                            'name': 'name',
                            'region': 'region',
                            'commitment_term': 'commitment_term',
                            'unit_price': 'unit_price',
                            'currency': 'currency',
                            'version': 'version',
                            'description': 'description',
                            }

    def __init__(self,
                 product_type=None,
                 name=None,
                 region=None,
                 commitment_term=None,
                 unit_price=None,
                 currency=None,
                 version=None,
                 description=None,
                ):
        """
        :type  product_type: :class:`str`
        :param product_type: 
        :type  name: :class:`str`
        :param name: 
        :type  region: :class:`str`
        :param region: 
        :type  commitment_term: :class:`long`
        :param commitment_term: 
        :type  unit_price: :class:`str`
        :param unit_price: 
        :type  currency: :class:`str`
        :param currency: 
        :type  version: :class:`str`
        :param version: 
        :type  description: :class:`str`
        :param description: 
        """
        self.product_type = product_type
        self.name = name
        self.region = region
        self.commitment_term = commitment_term
        self.unit_price = unit_price
        self.currency = currency
        self.version = version
        self.description = description
        VapiStruct.__init__(self)

TermOfferInstance._set_binding_type(type.StructType(
    'com.vmware.vmc.model.term_offer_instance', {
        'product_type': type.StringType(),
        'name': type.StringType(),
        'region': type.StringType(),
        'commitment_term': type.IntegerType(),
        'unit_price': type.StringType(),
        'currency': type.StringType(),
        'version': type.StringType(),
        'description': type.StringType(),
    },
    TermOfferInstance,
    False,
    None))



class VpcInfo(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'vpc_cidr': 'vpc_cidr',
                            'vm_security_group_id': 'vm_security_group_id',
                            'route_table_id': 'route_table_id',
                            'edge_subnet_id': 'edge_subnet_id',
                            'id': 'id',
                            'api_association_id': 'api_association_id',
                            'private_subnet_id': 'private_subnet_id',
                            'api_subnet_id': 'api_subnet_id',
                            'esx_security_group_id': 'esx_security_group_id',
                            'subnet_id': 'subnet_id',
                            'internet_gateway_id': 'internet_gateway_id',
                            'security_group_id': 'security_group_id',
                            'association_id': 'association_id',
                            'vgw_route_table_id': 'vgw_route_table_id',
                            'edge_association_id': 'edge_association_id',
                            'vif_ids': 'vif_ids',
                            'peering_connection_id': 'peering_connection_id',
                            }

    def __init__(self,
                 vpc_cidr=None,
                 vm_security_group_id=None,
                 route_table_id=None,
                 edge_subnet_id=None,
                 id=None,
                 api_association_id=None,
                 private_subnet_id=None,
                 api_subnet_id=None,
                 esx_security_group_id=None,
                 subnet_id=None,
                 internet_gateway_id=None,
                 security_group_id=None,
                 association_id=None,
                 vgw_route_table_id=None,
                 edge_association_id=None,
                 vif_ids=None,
                 peering_connection_id=None,
                ):
        """
        :type  vpc_cidr: :class:`str` or ``None``
        :param vpc_cidr: 
        :type  vm_security_group_id: :class:`str` or ``None``
        :param vm_security_group_id: 
        :type  route_table_id: :class:`str` or ``None``
        :param route_table_id: 
        :type  edge_subnet_id: :class:`str` or ``None``
        :param edge_subnet_id: Id of the NSX edge associated with this VPC
        :type  id: :class:`str` or ``None``
        :param id: 
        :type  api_association_id: :class:`str` or ``None``
        :param api_association_id: Id of the association between subnet and route-table
        :type  private_subnet_id: :class:`str` or ``None``
        :param private_subnet_id: 
        :type  api_subnet_id: :class:`str` or ``None``
        :param api_subnet_id: Id associated with this VPC
        :type  esx_security_group_id: :class:`str` or ``None``
        :param esx_security_group_id: 
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: 
        :type  internet_gateway_id: :class:`str` or ``None``
        :param internet_gateway_id: 
        :type  security_group_id: :class:`str` or ``None``
        :param security_group_id: 
        :type  association_id: :class:`str` or ``None``
        :param association_id: 
        :type  vgw_route_table_id: :class:`str` or ``None``
        :param vgw_route_table_id: Route table which contains the route to VGW
        :type  edge_association_id: :class:`str` or ``None``
        :param edge_association_id: Id of the association between edge subnet and route-table
        :type  vif_ids: :class:`list` of :class:`str` or ``None``
        :param vif_ids: 
        :type  peering_connection_id: :class:`str` or ``None``
        :param peering_connection_id: 
        """
        self.vpc_cidr = vpc_cidr
        self.vm_security_group_id = vm_security_group_id
        self.route_table_id = route_table_id
        self.edge_subnet_id = edge_subnet_id
        self.id = id
        self.api_association_id = api_association_id
        self.private_subnet_id = private_subnet_id
        self.api_subnet_id = api_subnet_id
        self.esx_security_group_id = esx_security_group_id
        self.subnet_id = subnet_id
        self.internet_gateway_id = internet_gateway_id
        self.security_group_id = security_group_id
        self.association_id = association_id
        self.vgw_route_table_id = vgw_route_table_id
        self.edge_association_id = edge_association_id
        self.vif_ids = vif_ids
        self.peering_connection_id = peering_connection_id
        VapiStruct.__init__(self)

VpcInfo._set_binding_type(type.StructType(
    'com.vmware.vmc.model.vpc_info', {
        'vpc_cidr': type.OptionalType(type.StringType()),
        'vm_security_group_id': type.OptionalType(type.StringType()),
        'route_table_id': type.OptionalType(type.StringType()),
        'edge_subnet_id': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'api_association_id': type.OptionalType(type.StringType()),
        'private_subnet_id': type.OptionalType(type.StringType()),
        'api_subnet_id': type.OptionalType(type.StringType()),
        'esx_security_group_id': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'internet_gateway_id': type.OptionalType(type.StringType()),
        'security_group_id': type.OptionalType(type.StringType()),
        'association_id': type.OptionalType(type.StringType()),
        'vgw_route_table_id': type.OptionalType(type.StringType()),
        'edge_association_id': type.OptionalType(type.StringType()),
        'vif_ids': type.OptionalType(type.ListType(type.StringType())),
        'peering_connection_id': type.OptionalType(type.StringType()),
    },
    VpcInfo,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

