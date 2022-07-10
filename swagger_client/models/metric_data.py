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


class MetricData(object):
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
        'metric_name': 'str',
        'from_time': 'datetime',
        'to_time': 'datetime',
        'instances': 'list[MetricInstanceData]'
    }

    attribute_map = {
        'metric_name': 'MetricName',
        'from_time': 'FromTime',
        'to_time': 'ToTime',
        'instances': 'Instances'
    }

    def __init__(self, metric_name=None, from_time=None, to_time=None, instances=None, _configuration=None):  # noqa: E501
        """MetricData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metric_name = None
        self._from_time = None
        self._to_time = None
        self._instances = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time
        if instances is not None:
            self.instances = instances

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricData.  # noqa: E501


        :return: The metric_name of this MetricData.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricData.


        :param metric_name: The metric_name of this MetricData.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def from_time(self):
        """Gets the from_time of this MetricData.  # noqa: E501


        :return: The from_time of this MetricData.  # noqa: E501
        :rtype: datetime
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this MetricData.


        :param from_time: The from_time of this MetricData.  # noqa: E501
        :type: datetime
        """

        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this MetricData.  # noqa: E501


        :return: The to_time of this MetricData.  # noqa: E501
        :rtype: datetime
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this MetricData.


        :param to_time: The to_time of this MetricData.  # noqa: E501
        :type: datetime
        """

        self._to_time = to_time

    @property
    def instances(self):
        """Gets the instances of this MetricData.  # noqa: E501


        :return: The instances of this MetricData.  # noqa: E501
        :rtype: list[MetricInstanceData]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this MetricData.


        :param instances: The instances of this MetricData.  # noqa: E501
        :type: list[MetricInstanceData]
        """

        self._instances = instances

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
        if issubclass(MetricData, dict):
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
        if not isinstance(other, MetricData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricData):
            return True

        return self.to_dict() != other.to_dict()
