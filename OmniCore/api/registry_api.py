# coding: utf-8

"""
    OmniCore Model and State Management API

    This is an OmniCore Model and State Management server.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@korewireless.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from OmniCore.models.device_registry import DeviceRegistry
from OmniCore.models.info import Info
from OmniCore.models.list_device_registries import ListDeviceRegistries

from OmniCore.api_client import ApiClient
from OmniCore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RegistryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_registry(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry : Annotated[Optional[DeviceRegistry], Field(description="application/json")] = None, **kwargs) -> DeviceRegistry:  # noqa: E501
        """create_registry  # noqa: E501

        Create a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_registry(subscription_id, registry, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry: application/json
        :type registry: DeviceRegistry
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeviceRegistry
        """
        kwargs['_return_http_data_only'] = True
        return self.create_registry_with_http_info(subscription_id, registry, **kwargs)  # noqa: E501

    @validate_arguments
    def create_registry_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry : Annotated[Optional[DeviceRegistry], Field(description="application/json")] = None, **kwargs):  # noqa: E501
        """create_registry  # noqa: E501

        Create a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_registry_with_http_info(subscription_id, registry, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry: application/json
        :type registry: DeviceRegistry
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeviceRegistry, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'registry'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_registry" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['registry']:
            _body_params = _params['registry']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "DeviceRegistry",
            '400': "GenericErrorResponse",
            '404': "GenericErrorResponse",
            '500': "GenericErrorResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}/registries', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_registry(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], **kwargs) -> Info:  # noqa: E501
        """delete_registry  # noqa: E501

        Delete a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_registry(subscription_id, registry_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Info
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_registry_with_http_info(subscription_id, registry_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_registry_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], **kwargs):  # noqa: E501
        """delete_registry  # noqa: E501

        Delete a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_registry_with_http_info(subscription_id, registry_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Info, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'registry_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_registry" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']
        if _params['registry_id']:
            _path_params['registryId'] = _params['registry_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "Info",
            '400': "GenericErrorResponse",
            '404': "GenericErrorResponse",
            '500': "GenericErrorResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}/registries/{registryId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_registries(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], page_number : Annotated[Optional[StrictInt], Field(description="Page Number")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Page Size")] = None, **kwargs) -> ListDeviceRegistries:  # noqa: E501
        """get_registries  # noqa: E501

        Get all registries under a subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registries(subscription_id, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param page_number: Page Number
        :type page_number: int
        :param page_size: Page Size
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListDeviceRegistries
        """
        kwargs['_return_http_data_only'] = True
        return self.get_registries_with_http_info(subscription_id, page_number, page_size, **kwargs)  # noqa: E501

    @validate_arguments
    def get_registries_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], page_number : Annotated[Optional[StrictInt], Field(description="Page Number")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Page Size")] = None, **kwargs):  # noqa: E501
        """get_registries  # noqa: E501

        Get all registries under a subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registries_with_http_info(subscription_id, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param page_number: Page Number
        :type page_number: int
        :param page_size: Page Size
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListDeviceRegistries, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'page_number',
            'page_size'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_registries" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']

        # process the query parameters
        _query_params = []
        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('pageNumber', _params['page_number']))
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "ListDeviceRegistries",
            '400': "GenericErrorResponse",
            '404': "GenericErrorResponse",
            '500': "GenericErrorResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}/registries', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_registry(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], **kwargs) -> DeviceRegistry:  # noqa: E501
        """get_registry  # noqa: E501

        Get a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registry(subscription_id, registry_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeviceRegistry
        """
        kwargs['_return_http_data_only'] = True
        return self.get_registry_with_http_info(subscription_id, registry_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_registry_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], **kwargs):  # noqa: E501
        """get_registry  # noqa: E501

        Get a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registry_with_http_info(subscription_id, registry_id, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeviceRegistry, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'registry_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_registry" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']
        if _params['registry_id']:
            _path_params['registryId'] = _params['registry_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "DeviceRegistry",
            '400': "GenericErrorResponse",
            '404': "GenericErrorResponse",
            '500': "GenericErrorResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}/registries/{registryId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_registry(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], update_mask : Annotated[StrictStr, Field(..., description="values to be updated: eventNotificationConfigs,stateNotificationConfig.pubsub_topic_name,logNotificationConfig.pubsub_topic_name,mqttConfig.mqtt_enabled_state,httpConfig.http_enabled_state,logLevel,credentials")], registry : Annotated[Optional[DeviceRegistry], Field(description="application/json")] = None, **kwargs) -> DeviceRegistry:  # noqa: E501
        """update_registry  # noqa: E501

        Update a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_registry(subscription_id, registry_id, update_mask, registry, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param update_mask: values to be updated: eventNotificationConfigs,stateNotificationConfig.pubsub_topic_name,logNotificationConfig.pubsub_topic_name,mqttConfig.mqtt_enabled_state,httpConfig.http_enabled_state,logLevel,credentials (required)
        :type update_mask: str
        :param registry: application/json
        :type registry: DeviceRegistry
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeviceRegistry
        """
        kwargs['_return_http_data_only'] = True
        return self.update_registry_with_http_info(subscription_id, registry_id, update_mask, registry, **kwargs)  # noqa: E501

    @validate_arguments
    def update_registry_with_http_info(self, subscription_id : Annotated[StrictStr, Field(..., description="Subscription ID")], registry_id : Annotated[StrictStr, Field(..., description="Registry ID")], update_mask : Annotated[StrictStr, Field(..., description="values to be updated: eventNotificationConfigs,stateNotificationConfig.pubsub_topic_name,logNotificationConfig.pubsub_topic_name,mqttConfig.mqtt_enabled_state,httpConfig.http_enabled_state,logLevel,credentials")], registry : Annotated[Optional[DeviceRegistry], Field(description="application/json")] = None, **kwargs):  # noqa: E501
        """update_registry  # noqa: E501

        Update a registry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_registry_with_http_info(subscription_id, registry_id, update_mask, registry, async_req=True)
        >>> result = thread.get()

        :param subscription_id: Subscription ID (required)
        :type subscription_id: str
        :param registry_id: Registry ID (required)
        :type registry_id: str
        :param update_mask: values to be updated: eventNotificationConfigs,stateNotificationConfig.pubsub_topic_name,logNotificationConfig.pubsub_topic_name,mqttConfig.mqtt_enabled_state,httpConfig.http_enabled_state,logLevel,credentials (required)
        :type update_mask: str
        :param registry: application/json
        :type registry: DeviceRegistry
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeviceRegistry, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subscription_id',
            'registry_id',
            'update_mask',
            'registry'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_registry" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['subscription_id']:
            _path_params['subscriptionId'] = _params['subscription_id']
        if _params['registry_id']:
            _path_params['registryId'] = _params['registry_id']

        # process the query parameters
        _query_params = []
        if _params.get('update_mask') is not None:  # noqa: E501
            _query_params.append(('updateMask', _params['update_mask']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['registry']:
            _body_params = _params['registry']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "DeviceRegistry",
            '400': "GenericErrorResponse",
            '404': "GenericErrorResponse",
            '500': "GenericErrorResponse",
        }

        return self.api_client.call_api(
            '/subscriptions/{subscriptionId}/registries/{registryId}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
