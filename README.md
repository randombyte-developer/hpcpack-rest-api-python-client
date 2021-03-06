# swagger-client
This is the API spec for Microsoft HPC Pack 2019. (https://github.com/Azure/hpcpack-rest-api-spec)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2020-01-01.6.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
job_id = 56 # int | Job Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of task to add. (optional)

try:
    # Add Task
    api_response = api_instance.add_task(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_task: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/hpc*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_task**](docs/DefaultApi.md#add_task) | **POST** /jobs/{jobId}/tasks | Add Task
*DefaultApi* | [**cancel_job**](docs/DefaultApi.md#cancel_job) | **POST** /jobs/{jobId}/cancel | Cancel Job
*DefaultApi* | [**cancel_subtask**](docs/DefaultApi.md#cancel_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/cancel | Cancel Subtask
*DefaultApi* | [**cancel_task**](docs/DefaultApi.md#cancel_task) | **POST** /jobs/{jobId}/tasks/{taskId}/cancel | Cancel Task
*DefaultApi* | [**create_job**](docs/DefaultApi.md#create_job) | **POST** /jobs | Create Job
*DefaultApi* | [**create_job_from_xml**](docs/DefaultApi.md#create_job_from_xml) | **POST** /jobs/jobFile | Create Job From XML
*DefaultApi* | [**create_node_group**](docs/DefaultApi.md#create_node_group) | **POST** /cluster/nodeGroups | Create a Node Group
*DefaultApi* | [**delete_node_group**](docs/DefaultApi.md#delete_node_group) | **DELETE** /cluster/nodeGroups/{name} | Delete Node Group
*DefaultApi* | [**finish_job**](docs/DefaultApi.md#finish_job) | **POST** /jobs/{jobId}/finish | Finish Job
*DefaultApi* | [**finish_subtask**](docs/DefaultApi.md#finish_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/finish | Finish Subtask
*DefaultApi* | [**finish_task**](docs/DefaultApi.md#finish_task) | **POST** /jobs/{jobId}/tasks/{taskId}/finish | Finish Task
*DefaultApi* | [**get_cluster_active_head_node**](docs/DefaultApi.md#get_cluster_active_head_node) | **GET** /cluster/activeHeadNode | Get Active Head Node Name
*DefaultApi* | [**get_cluster_date_time_format**](docs/DefaultApi.md#get_cluster_date_time_format) | **GET** /cluster/info/dateTimeFormat | Get DateTime Format
*DefaultApi* | [**get_cluster_first_operation**](docs/DefaultApi.md#get_cluster_first_operation) | **GET** /cluster/operations/first | Get the First Cluster Operation Log in Time Order
*DefaultApi* | [**get_cluster_job_metrics**](docs/DefaultApi.md#get_cluster_job_metrics) | **GET** /cluster/metrics/jobs | Get Cluster Job Metrics
*DefaultApi* | [**get_cluster_metric_defintions**](docs/DefaultApi.md#get_cluster_metric_defintions) | **GET** /cluster/metrics/definitions | Get cluster metric definitions
*DefaultApi* | [**get_cluster_metric_history**](docs/DefaultApi.md#get_cluster_metric_history) | **GET** /cluster/metrics/history/{name} | Get cluster metric history
*DefaultApi* | [**get_cluster_node**](docs/DefaultApi.md#get_cluster_node) | **GET** /cluster/nodes/{name} | Get Cluster Node by Name
*DefaultApi* | [**get_cluster_node_metrics**](docs/DefaultApi.md#get_cluster_node_metrics) | **GET** /cluster/nodes/metrics | Get Node Metrics
*DefaultApi* | [**get_cluster_node_stat_of_health**](docs/DefaultApi.md#get_cluster_node_stat_of_health) | **GET** /cluster/nodes/stats/health | Get Cluster Node Stat of Health
*DefaultApi* | [**get_cluster_node_stat_of_state**](docs/DefaultApi.md#get_cluster_node_stat_of_state) | **GET** /cluster/nodes/stats/state | Get Cluster Node Stat of State
*DefaultApi* | [**get_cluster_nodes**](docs/DefaultApi.md#get_cluster_nodes) | **GET** /cluster/nodes | Get Cluster Nodes
*DefaultApi* | [**get_cluster_operation**](docs/DefaultApi.md#get_cluster_operation) | **GET** /cluster/operations/{id} | Get Cluster Operation Log by ID
*DefaultApi* | [**get_cluster_operations**](docs/DefaultApi.md#get_cluster_operations) | **GET** /cluster/operations | Get Cluster Operation Logs
*DefaultApi* | [**get_cluster_version**](docs/DefaultApi.md#get_cluster_version) | **GET** /cluster/version | Get HPC Pack Version
*DefaultApi* | [**get_job**](docs/DefaultApi.md#get_job) | **GET** /jobs/{jobId} | Get Job
*DefaultApi* | [**get_job_custom_properties**](docs/DefaultApi.md#get_job_custom_properties) | **GET** /jobs/{jobId}/customProperties | Get Job Custom Properties
*DefaultApi* | [**get_job_environment_variables**](docs/DefaultApi.md#get_job_environment_variables) | **GET** /jobs/{jobId}/envVariables | Get Job Environment Variables
*DefaultApi* | [**get_job_templates**](docs/DefaultApi.md#get_job_templates) | **GET** /jobs/templates | Get Job Templates
*DefaultApi* | [**get_jobs**](docs/DefaultApi.md#get_jobs) | **GET** /jobs | Get Job List
*DefaultApi* | [**get_node_group**](docs/DefaultApi.md#get_node_group) | **GET** /cluster/nodeGroups/{name} | Get Node Group
*DefaultApi* | [**get_node_groups**](docs/DefaultApi.md#get_node_groups) | **GET** /cluster/nodeGroups | Get Node Group List
*DefaultApi* | [**get_nodes_of_group**](docs/DefaultApi.md#get_nodes_of_group) | **GET** /cluster/nodeGroups/{name}/nodes | Get Nodes of a Group
*DefaultApi* | [**get_subtask**](docs/DefaultApi.md#get_subtask) | **GET** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId} | Get Subtask
*DefaultApi* | [**get_task**](docs/DefaultApi.md#get_task) | **GET** /jobs/{jobId}/tasks/{taskId} | Get Task
*DefaultApi* | [**get_task_custom_properties**](docs/DefaultApi.md#get_task_custom_properties) | **GET** /jobs/{jobId}/tasks/{taskId}/customProperties | Get Task Custom Properties
*DefaultApi* | [**get_task_environment_variables**](docs/DefaultApi.md#get_task_environment_variables) | **GET** /jobs/{jobId}/tasks/{taskId}/envVariables | Get Task Environment Variables
*DefaultApi* | [**get_tasks**](docs/DefaultApi.md#get_tasks) | **GET** /jobs/{jobId}/tasks | Get Task List
*DefaultApi* | [**get_user_roles**](docs/DefaultApi.md#get_user_roles) | **GET** /cluster/userRoles | Get Cluster User Roles
*DefaultApi* | [**move_nodes_of_group**](docs/DefaultApi.md#move_nodes_of_group) | **PATCH** /cluster/nodeGroups/{name}/nodes | Add/Remove Nodes to/from a Group
*DefaultApi* | [**operate_cluster_node**](docs/DefaultApi.md#operate_cluster_node) | **POST** /cluster/nodes/{name}/operations/{operation} | Operate a Cluster Node
*DefaultApi* | [**requeue_job**](docs/DefaultApi.md#requeue_job) | **POST** /jobs/{jobId}/requeue | Requeue Job
*DefaultApi* | [**requeue_subtask**](docs/DefaultApi.md#requeue_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/requeue | Requeue Subtask
*DefaultApi* | [**requeue_task**](docs/DefaultApi.md#requeue_task) | **POST** /jobs/{jobId}/tasks/{taskId}/requeue | Requeue Task
*DefaultApi* | [**set_job_custom_properties**](docs/DefaultApi.md#set_job_custom_properties) | **POST** /jobs/{jobId}/customProperties | Set Job Custom Properties
*DefaultApi* | [**set_job_environment_variables**](docs/DefaultApi.md#set_job_environment_variables) | **POST** /jobs/{jobId}/envVariables | Set Job Environment Variables
*DefaultApi* | [**set_job_properties**](docs/DefaultApi.md#set_job_properties) | **PUT** /jobs/{jobId} | Set Job Properties
*DefaultApi* | [**set_subtask_properties**](docs/DefaultApi.md#set_subtask_properties) | **PUT** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId} | Set Subtask Properties
*DefaultApi* | [**set_task_custom_properties**](docs/DefaultApi.md#set_task_custom_properties) | **POST** /jobs/{jobId}/tasks/{taskId}/customProperties | Set Task Custom Properties
*DefaultApi* | [**set_task_environment_variables**](docs/DefaultApi.md#set_task_environment_variables) | **POST** /jobs/{jobId}/tasks/{taskId}/envVariables | Set Task Environment Variables
*DefaultApi* | [**set_task_properties**](docs/DefaultApi.md#set_task_properties) | **PUT** /jobs/{jobId}/tasks/{taskId} | Set Task Properties
*DefaultApi* | [**submit_job**](docs/DefaultApi.md#submit_job) | **POST** /jobs/{jobId}/submit | Submit Job
*DefaultApi* | [**update_node_group**](docs/DefaultApi.md#update_node_group) | **PUT** /cluster/nodeGroups/{name} | Update Node Group


## Documentation For Models

 - [MetricData](docs/MetricData.md)
 - [MetricDefinition](docs/MetricDefinition.md)
 - [MetricInstanceData](docs/MetricInstanceData.md)
 - [Node](docs/Node.md)
 - [NodeGroup](docs/NodeGroup.md)
 - [NodeGroupOperation](docs/NodeGroupOperation.md)
 - [NodeHealth](docs/NodeHealth.md)
 - [NodeMetric](docs/NodeMetric.md)
 - [NodeServiceRole](docs/NodeServiceRole.md)
 - [NodeStatOfHealth](docs/NodeStatOfHealth.md)
 - [NodeStatOfState](docs/NodeStatOfState.md)
 - [NodeState](docs/NodeState.md)
 - [OperationLog](docs/OperationLog.md)
 - [OperationLogEntry](docs/OperationLogEntry.md)
 - [RestObject](docs/RestObject.md)
 - [RestProperty](docs/RestProperty.md)
 - [UserRole](docs/UserRole.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

hpcpack@microsoft.com

