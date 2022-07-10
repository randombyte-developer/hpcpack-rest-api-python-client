# coding: utf-8

"""
    HPC Pack REST API 2019

    This is the API spec for Microsoft HPC Pack 2019.  # noqa: E501

    OpenAPI spec version: 2020-01-01.6.0
    Contact: hpcpack@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class NodeMetric(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'node_name': 'str',
        'metrics': 'dict(str, float)'
    }

    attribute_map = {
        'node_name': 'NodeName',
        'metrics': 'Metrics'
    }

    def __init__(self, node_name=None, metrics=None, _configuration=None):  # noqa: E501
        """NodeMetric - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_name = None
        self._metrics = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if metrics is not None:
            self.metrics = metrics

    @property
    def node_name(self):
        """Gets the node_name of this NodeMetric.  # noqa: E501


        :return: The node_name of this NodeMetric.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this NodeMetric.


        :param node_name: The node_name of this NodeMetric.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def metrics(self):
        """Gets the metrics of this NodeMetric.  # noqa: E501


        :return: The metrics of this NodeMetric.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this NodeMetric.


        :param metrics: The metrics of this NodeMetric.  # noqa: E501
        :type: dict(str, float)
        """

        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NodeMetric, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeMetric):
            return True

        return self.to_dict() != other.to_dict()
