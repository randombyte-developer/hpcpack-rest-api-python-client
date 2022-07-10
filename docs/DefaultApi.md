# swagger_client.DefaultApi

All URIs are relative to *https://localhost/hpc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_task**](DefaultApi.md#add_task) | **POST** /jobs/{jobId}/tasks | Add Task
[**cancel_job**](DefaultApi.md#cancel_job) | **POST** /jobs/{jobId}/cancel | Cancel Job
[**cancel_subtask**](DefaultApi.md#cancel_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/cancel | Cancel Subtask
[**cancel_task**](DefaultApi.md#cancel_task) | **POST** /jobs/{jobId}/tasks/{taskId}/cancel | Cancel Task
[**create_job**](DefaultApi.md#create_job) | **POST** /jobs | Create Job
[**create_job_from_xml**](DefaultApi.md#create_job_from_xml) | **POST** /jobs/jobFile | Create Job From XML
[**create_node_group**](DefaultApi.md#create_node_group) | **POST** /cluster/nodeGroups | Create a Node Group
[**delete_node_group**](DefaultApi.md#delete_node_group) | **DELETE** /cluster/nodeGroups/{name} | Delete Node Group
[**finish_job**](DefaultApi.md#finish_job) | **POST** /jobs/{jobId}/finish | Finish Job
[**finish_subtask**](DefaultApi.md#finish_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/finish | Finish Subtask
[**finish_task**](DefaultApi.md#finish_task) | **POST** /jobs/{jobId}/tasks/{taskId}/finish | Finish Task
[**get_cluster_active_head_node**](DefaultApi.md#get_cluster_active_head_node) | **GET** /cluster/activeHeadNode | Get Active Head Node Name
[**get_cluster_date_time_format**](DefaultApi.md#get_cluster_date_time_format) | **GET** /cluster/info/dateTimeFormat | Get DateTime Format
[**get_cluster_first_operation**](DefaultApi.md#get_cluster_first_operation) | **GET** /cluster/operations/first | Get the First Cluster Operation Log in Time Order
[**get_cluster_job_metrics**](DefaultApi.md#get_cluster_job_metrics) | **GET** /cluster/metrics/jobs | Get Cluster Job Metrics
[**get_cluster_metric_defintions**](DefaultApi.md#get_cluster_metric_defintions) | **GET** /cluster/metrics/definitions | Get cluster metric definitions
[**get_cluster_metric_history**](DefaultApi.md#get_cluster_metric_history) | **GET** /cluster/metrics/history/{name} | Get cluster metric history
[**get_cluster_node**](DefaultApi.md#get_cluster_node) | **GET** /cluster/nodes/{name} | Get Cluster Node by Name
[**get_cluster_node_metrics**](DefaultApi.md#get_cluster_node_metrics) | **GET** /cluster/nodes/metrics | Get Node Metrics
[**get_cluster_node_stat_of_health**](DefaultApi.md#get_cluster_node_stat_of_health) | **GET** /cluster/nodes/stats/health | Get Cluster Node Stat of Health
[**get_cluster_node_stat_of_state**](DefaultApi.md#get_cluster_node_stat_of_state) | **GET** /cluster/nodes/stats/state | Get Cluster Node Stat of State
[**get_cluster_nodes**](DefaultApi.md#get_cluster_nodes) | **GET** /cluster/nodes | Get Cluster Nodes
[**get_cluster_operation**](DefaultApi.md#get_cluster_operation) | **GET** /cluster/operations/{id} | Get Cluster Operation Log by ID
[**get_cluster_operations**](DefaultApi.md#get_cluster_operations) | **GET** /cluster/operations | Get Cluster Operation Logs
[**get_cluster_version**](DefaultApi.md#get_cluster_version) | **GET** /cluster/version | Get HPC Pack Version
[**get_job**](DefaultApi.md#get_job) | **GET** /jobs/{jobId} | Get Job
[**get_job_custom_properties**](DefaultApi.md#get_job_custom_properties) | **GET** /jobs/{jobId}/customProperties | Get Job Custom Properties
[**get_job_environment_variables**](DefaultApi.md#get_job_environment_variables) | **GET** /jobs/{jobId}/envVariables | Get Job Environment Variables
[**get_job_templates**](DefaultApi.md#get_job_templates) | **GET** /jobs/templates | Get Job Templates
[**get_jobs**](DefaultApi.md#get_jobs) | **GET** /jobs | Get Job List
[**get_node_group**](DefaultApi.md#get_node_group) | **GET** /cluster/nodeGroups/{name} | Get Node Group
[**get_node_groups**](DefaultApi.md#get_node_groups) | **GET** /cluster/nodeGroups | Get Node Group List
[**get_nodes_of_group**](DefaultApi.md#get_nodes_of_group) | **GET** /cluster/nodeGroups/{name}/nodes | Get Nodes of a Group
[**get_subtask**](DefaultApi.md#get_subtask) | **GET** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId} | Get Subtask
[**get_task**](DefaultApi.md#get_task) | **GET** /jobs/{jobId}/tasks/{taskId} | Get Task
[**get_task_custom_properties**](DefaultApi.md#get_task_custom_properties) | **GET** /jobs/{jobId}/tasks/{taskId}/customProperties | Get Task Custom Properties
[**get_task_environment_variables**](DefaultApi.md#get_task_environment_variables) | **GET** /jobs/{jobId}/tasks/{taskId}/envVariables | Get Task Environment Variables
[**get_tasks**](DefaultApi.md#get_tasks) | **GET** /jobs/{jobId}/tasks | Get Task List
[**get_user_roles**](DefaultApi.md#get_user_roles) | **GET** /cluster/userRoles | Get Cluster User Roles
[**move_nodes_of_group**](DefaultApi.md#move_nodes_of_group) | **PATCH** /cluster/nodeGroups/{name}/nodes | Add/Remove Nodes to/from a Group
[**operate_cluster_node**](DefaultApi.md#operate_cluster_node) | **POST** /cluster/nodes/{name}/operations/{operation} | Operate a Cluster Node
[**requeue_job**](DefaultApi.md#requeue_job) | **POST** /jobs/{jobId}/requeue | Requeue Job
[**requeue_subtask**](DefaultApi.md#requeue_subtask) | **POST** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId}/requeue | Requeue Subtask
[**requeue_task**](DefaultApi.md#requeue_task) | **POST** /jobs/{jobId}/tasks/{taskId}/requeue | Requeue Task
[**set_job_custom_properties**](DefaultApi.md#set_job_custom_properties) | **POST** /jobs/{jobId}/customProperties | Set Job Custom Properties
[**set_job_environment_variables**](DefaultApi.md#set_job_environment_variables) | **POST** /jobs/{jobId}/envVariables | Set Job Environment Variables
[**set_job_properties**](DefaultApi.md#set_job_properties) | **PUT** /jobs/{jobId} | Set Job Properties
[**set_subtask_properties**](DefaultApi.md#set_subtask_properties) | **PUT** /jobs/{jobId}/tasks/{taskId}/subtasks/{subtaskId} | Set Subtask Properties
[**set_task_custom_properties**](DefaultApi.md#set_task_custom_properties) | **POST** /jobs/{jobId}/tasks/{taskId}/customProperties | Set Task Custom Properties
[**set_task_environment_variables**](DefaultApi.md#set_task_environment_variables) | **POST** /jobs/{jobId}/tasks/{taskId}/envVariables | Set Task Environment Variables
[**set_task_properties**](DefaultApi.md#set_task_properties) | **PUT** /jobs/{jobId}/tasks/{taskId} | Set Task Properties
[**submit_job**](DefaultApi.md#submit_job) | **POST** /jobs/{jobId}/submit | Submit Job
[**update_node_group**](DefaultApi.md#update_node_group) | **PUT** /cluster/nodeGroups/{name} | Update Node Group


# **add_task**
> int add_task(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Add Task

Add a task to a job.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of task to add. | [optional] 

### Return type

**int**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_job**
> cancel_job(job_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)

Cancel Job

Cancel the specified job.

### Example
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
forced = false # bool | Specifies whether to stop the job immediately without using the grace period for canceling the tasks in the job and without running the node release task, if the job contains one. True indicates that the job should stop immediately without using the grace period for canceling the tasks in the job and without running the node release task. False indicates that the job should not stop immediately and should use the grace period for canceling the tasks in the job and run the node release task. (optional) (default to false)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Cancel Job
    api_instance.cancel_job(job_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **forced** | **bool**| Specifies whether to stop the job immediately without using the grace period for canceling the tasks in the job and without running the node release task, if the job contains one. True indicates that the job should stop immediately without using the grace period for canceling the tasks in the job and without running the node release task. False indicates that the job should not stop immediately and should use the grace period for canceling the tasks in the job and run the node release task. | [optional] [default to false]
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subtask**
> cancel_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)

Cancel Subtask

Cancel the specified subtask.

### Example
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
task_id = 56 # int | Task Id
subtask_id = 56 # int | Subtask Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
forced = false # bool | Specifies whether to stop the subtask immediately without using the grace period for canceling a task. True indicates that the subtask should stop immediately without using the grace period for canceling a task. False indicates that the subtask should use the grace period for canceling. (optional) (default to false)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Cancel Subtask
    api_instance.cancel_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_subtask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **subtask_id** | **int**| Subtask Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **forced** | **bool**| Specifies whether to stop the subtask immediately without using the grace period for canceling a task. True indicates that the subtask should stop immediately without using the grace period for canceling a task. False indicates that the subtask should use the grace period for canceling. | [optional] [default to false]
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_task**
> cancel_task(job_id, task_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)

Cancel Task

Cancel the specified task.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
forced = false # bool | Specifies whether to stop the task immediately without using the grace period for canceling a task. True indicates that the task should stop immediately without using the grace period for canceling a task. False indicates that the task should use the grace period for canceling a task. (optional) (default to false)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Cancel Task
    api_instance.cancel_task(job_id, task_id, x_ms_as_user=x_ms_as_user, forced=forced, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **forced** | **bool**| Specifies whether to stop the task immediately without using the grace period for canceling a task. True indicates that the task should stop immediately without using the grace period for canceling a task. False indicates that the task should use the grace period for canceling a task. | [optional] [default to false]
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> int create_job(x_ms_as_user=x_ms_as_user, properties=properties)

Create Job

Creates a new job on the HPC cluster.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of job to create (optional)

try:
    # Create Job
    api_response = api_instance.create_job(x_ms_as_user=x_ms_as_user, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of job to create | [optional] 

### Return type

**int**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_from_xml**
> int create_job_from_xml(x_ms_as_user=x_ms_as_user, xml=xml)

Create Job From XML

Create a new job on the HPC cluster by using the information in the specified job XML string.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
xml = 'xml_example' # str | A job described in XML. For an example:  ```xml <Job>   <Tasks>     <Task CommandLine=\"hostname\" MinCores=\"1\" MaxCores=\"1\" />   </Tasks> </Job> ```  Note that since the server accepts input in JSON, the XML has to be encoded in a JSON string.  See [Job Schema](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc907034%28v%3dvs.85%29) for more details on the XML content.  (optional)

try:
    # Create Job From XML
    api_response = api_instance.create_job_from_xml(x_ms_as_user=x_ms_as_user, xml=xml)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_job_from_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **xml** | **str**| A job described in XML. For an example:  &#x60;&#x60;&#x60;xml &lt;Job&gt;   &lt;Tasks&gt;     &lt;Task CommandLine&#x3D;\&quot;hostname\&quot; MinCores&#x3D;\&quot;1\&quot; MaxCores&#x3D;\&quot;1\&quot; /&gt;   &lt;/Tasks&gt; &lt;/Job&gt; &#x60;&#x60;&#x60;  Note that since the server accepts input in JSON, the XML has to be encoded in a JSON string.  See [Job Schema](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc907034%28v%3dvs.85%29) for more details on the XML content.  | [optional] 

### Return type

**int**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_group**
> NodeGroup create_node_group(x_ms_as_user=x_ms_as_user, node_group=node_group)

Create a Node Group

Create a Node Group

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
node_group = swagger_client.NodeGroup() # NodeGroup |  (optional)

try:
    # Create a Node Group
    api_response = api_instance.create_node_group(x_ms_as_user=x_ms_as_user, node_group=node_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_node_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **node_group** | [**NodeGroup**](NodeGroup.md)|  | [optional] 

### Return type

[**NodeGroup**](NodeGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_group**
> delete_node_group(name, x_ms_as_user=x_ms_as_user)

Delete Node Group

Delete a node group.

### Example
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
name = 'name_example' # str | Node group name.
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Delete Node Group
    api_instance.delete_node_group(name, x_ms_as_user=x_ms_as_user)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_node_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node group name. | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_job**
> finish_job(job_id, x_ms_as_user=x_ms_as_user, message=message)

Finish Job

Finish the specified job. It's silimar to canceling a job, but sets the job state to \"Finished\" rather than \"Canceled\".

### Example
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
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Finish Job
    api_instance.finish_job(job_id, x_ms_as_user=x_ms_as_user, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->finish_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_subtask**
> finish_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, message=message)

Finish Subtask

Finish the specified subtask.

### Example
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
task_id = 56 # int | Task Id
subtask_id = 56 # int | Subtask Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Finish Subtask
    api_instance.finish_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->finish_subtask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **subtask_id** | **int**| Subtask Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_task**
> finish_task(job_id, task_id, x_ms_as_user=x_ms_as_user, message=message)

Finish Task

Finish the specified task. It's silimar to canceling a task, but sets the task state to \"Finished\" rather than \"Canceled\".

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Finish Task
    api_instance.finish_task(job_id, task_id, x_ms_as_user=x_ms_as_user, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->finish_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_active_head_node**
> str get_cluster_active_head_node(x_ms_as_user=x_ms_as_user)

Get Active Head Node Name

Get the name of the active head node of the HPC Pack cluster.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Active Head Node Name
    api_response = api_instance.get_cluster_active_head_node(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_active_head_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_date_time_format**
> str get_cluster_date_time_format(x_ms_as_user=x_ms_as_user)

Get DateTime Format

Get DateTime format for the DateTime objects returned in the API

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get DateTime Format
    api_response = api_instance.get_cluster_date_time_format(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_date_time_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_first_operation**
> OperationLog get_cluster_first_operation(x_ms_as_user=x_ms_as_user, from_time=from_time, to_time=to_time, node_names=node_names)

Get the First Cluster Operation Log in Time Order

Get the first cluster operation log in time order, optionally under given conditions.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
from_time = '2013-10-20T19:20:30+01:00' # datetime | The start time(exclusive) in UTC (optional)
to_time = '2013-10-20T19:20:30+01:00' # datetime | The end time(exclusive) in UTC (optional)
node_names = 'node_names_example' # str | A comma-separated list of names for which the logs will be retrieved. (optional)

try:
    # Get the First Cluster Operation Log in Time Order
    api_response = api_instance.get_cluster_first_operation(x_ms_as_user=x_ms_as_user, from_time=from_time, to_time=to_time, node_names=node_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_first_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **from_time** | **datetime**| The start time(exclusive) in UTC | [optional] 
 **to_time** | **datetime**| The end time(exclusive) in UTC | [optional] 
 **node_names** | **str**| A comma-separated list of names for which the logs will be retrieved. | [optional] 

### Return type

[**OperationLog**](OperationLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_job_metrics**
> MetricData get_cluster_job_metrics(x_ms_as_user=x_ms_as_user)

Get Cluster Job Metrics

Get cluster job metrics for the last 7 days.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster Job Metrics
    api_response = api_instance.get_cluster_job_metrics(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_job_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**MetricData**](MetricData.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metric_defintions**
> list[MetricDefinition] get_cluster_metric_defintions(x_ms_as_user=x_ms_as_user)

Get cluster metric definitions

Get cluster metric definitions. You can then get the history of a metric.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get cluster metric definitions
    api_response = api_instance.get_cluster_metric_defintions(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_metric_defintions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**list[MetricDefinition]**](MetricDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metric_history**
> MetricData get_cluster_metric_history(name, from_time, to_time, x_ms_as_user=x_ms_as_user)

Get cluster metric history

Get cluster metric history

### Example
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
name = 'name_example' # str | Metric name
from_time = '2013-10-20T19:20:30+01:00' # datetime | The start time in UTC
to_time = '2013-10-20T19:20:30+01:00' # datetime | The end time in UTC
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get cluster metric history
    api_response = api_instance.get_cluster_metric_history(name, from_time, to_time, x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_metric_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Metric name | 
 **from_time** | **datetime**| The start time in UTC | 
 **to_time** | **datetime**| The end time in UTC | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**MetricData**](MetricData.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> Node get_cluster_node(name, x_ms_as_user=x_ms_as_user)

Get Cluster Node by Name

### Example
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
name = 'name_example' # str | Node name
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster Node by Name
    api_response = api_instance.get_cluster_node(name, x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node name | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_metrics**
> list[NodeMetric] get_cluster_node_metrics(metric_names)

Get Node Metrics

Get metrics of nodes

### Example
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
metric_names = 'metric_names_example' # str | A comma separated names of metrics, available names are HPCCpuUsage, HPCMemoryPaging, HPCDiskThroughput, HPCNetwork and HPCCoresInUse

try:
    # Get Node Metrics
    api_response = api_instance.get_cluster_node_metrics(metric_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_node_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_names** | **str**| A comma separated names of metrics, available names are HPCCpuUsage, HPCMemoryPaging, HPCDiskThroughput, HPCNetwork and HPCCoresInUse | 

### Return type

[**list[NodeMetric]**](NodeMetric.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_stat_of_health**
> NodeStatOfHealth get_cluster_node_stat_of_health(x_ms_as_user=x_ms_as_user)

Get Cluster Node Stat of Health

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster Node Stat of Health
    api_response = api_instance.get_cluster_node_stat_of_health(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_node_stat_of_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**NodeStatOfHealth**](NodeStatOfHealth.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_stat_of_state**
> NodeStatOfState get_cluster_node_stat_of_state(x_ms_as_user=x_ms_as_user)

Get Cluster Node Stat of State

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster Node Stat of State
    api_response = api_instance.get_cluster_node_stat_of_state(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_node_stat_of_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**NodeStatOfState**](NodeStatOfState.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> list[Node] get_cluster_nodes(x_ms_as_user=x_ms_as_user, names=names, jobs=jobs, group=group, state=state, health=health)

Get Cluster Nodes

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
names = 'names_example' # str | A comma-separated list of node names. (optional)
jobs = 'jobs_example' # str | A comma-separated list of job ids. (optional)
group = 'group_example' # str | A node group name. (optional)
state = 'state_example' # str | Node state. (optional)
health = 'health_example' # str | Node health. (optional)

try:
    # Get Cluster Nodes
    api_response = api_instance.get_cluster_nodes(x_ms_as_user=x_ms_as_user, names=names, jobs=jobs, group=group, state=state, health=health)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **names** | **str**| A comma-separated list of node names. | [optional] 
 **jobs** | **str**| A comma-separated list of job ids. | [optional] 
 **group** | **str**| A node group name. | [optional] 
 **state** | **str**| Node state. | [optional] 
 **health** | **str**| Node health. | [optional] 

### Return type

[**list[Node]**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_operation**
> OperationLog get_cluster_operation(id, x_ms_as_user=x_ms_as_user)

Get Cluster Operation Log by ID

Get cluster operation log by ID.

### Example
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
id = 'id_example' # str | Operation ID
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster Operation Log by ID
    api_response = api_instance.get_cluster_operation(id, x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Operation ID | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**OperationLog**](OperationLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_operations**
> list[OperationLog] get_cluster_operations(x_ms_as_user=x_ms_as_user, from_time=from_time, to_time=to_time, limit=limit, node_names=node_names, with_detail=with_detail)

Get Cluster Operation Logs

Get cluster operation logs in time order, with the latest log being first.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
from_time = '2013-10-20T19:20:30+01:00' # datetime | The start time(exclusive) in UTC (optional)
to_time = '2013-10-20T19:20:30+01:00' # datetime | The end time(exclusive) in UTC (optional)
limit = 8.14 # float | The max number of logs to return (optional)
node_names = 'node_names_example' # str | A comma-separated list of names for which the logs will be retrieved. (optional)
with_detail = false # bool | Whether to include the \"Entries\" property for each log. By deafult no \"Entries\" will be returned.  (optional) (default to false)

try:
    # Get Cluster Operation Logs
    api_response = api_instance.get_cluster_operations(x_ms_as_user=x_ms_as_user, from_time=from_time, to_time=to_time, limit=limit, node_names=node_names, with_detail=with_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **from_time** | **datetime**| The start time(exclusive) in UTC | [optional] 
 **to_time** | **datetime**| The end time(exclusive) in UTC | [optional] 
 **limit** | **float**| The max number of logs to return | [optional] 
 **node_names** | **str**| A comma-separated list of names for which the logs will be retrieved. | [optional] 
 **with_detail** | **bool**| Whether to include the \&quot;Entries\&quot; property for each log. By deafult no \&quot;Entries\&quot; will be returned.  | [optional] [default to false]

### Return type

[**list[OperationLog]**](OperationLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_version**
> str get_cluster_version(x_ms_as_user=x_ms_as_user)

Get HPC Pack Version

Get the version of Microsoft HPC Pack installed on the HPC cluster that hosts the web service.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get HPC Pack Version
    api_response = api_instance.get_cluster_version(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cluster_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> list[RestProperty] get_job(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Get Job

Get information about the specified job.

### Example
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
properties = 'properties_example' # str | A comma-separated list of the names for the properties of the job for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the job. See [ISchedulerJob](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897474%28v%3dvs.85%29) for available properties. (optional)

try:
    # Get Job
    api_response = api_instance.get_job(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | **str**| A comma-separated list of the names for the properties of the job for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the job. See [ISchedulerJob](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897474%28v%3dvs.85%29) for available properties. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_custom_properties**
> list[RestProperty] get_job_custom_properties(job_id, x_ms_as_user=x_ms_as_user, names=names)

Get Job Custom Properties

Get the values of the specified custom properties for the job, or the values of all of the properties if none are specified.

### Example
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
names = 'names_example' # str | A comma-separated list of the names for the custom properties of the job for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the custom properties for the job. (optional)

try:
    # Get Job Custom Properties
    api_response = api_instance.get_job_custom_properties(job_id, x_ms_as_user=x_ms_as_user, names=names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_job_custom_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **names** | **str**| A comma-separated list of the names for the custom properties of the job for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the custom properties for the job. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_environment_variables**
> list[RestProperty] get_job_environment_variables(job_id, x_ms_as_user=x_ms_as_user, names=names)

Get Job Environment Variables

Get the values of the specified environment variables for the job, or the values of all of the environment variables if none are specified.

### Example
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
names = 'names_example' # str | A comma-separated list of the names for the environment variables in the job for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the environment variables for the job. If an environment variable with a specified name does not exist for the job, the response contains an empty string for the value of that environment variable. (optional)

try:
    # Get Job Environment Variables
    api_response = api_instance.get_job_environment_variables(job_id, x_ms_as_user=x_ms_as_user, names=names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_job_environment_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **names** | **str**| A comma-separated list of the names for the environment variables in the job for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the environment variables for the job. If an environment variable with a specified name does not exist for the job, the response contains an empty string for the value of that environment variable. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_templates**
> list[str] get_job_templates(x_ms_as_user=x_ms_as_user)

Get Job Templates

Get a list of the names of the job templates that are available on the HPC cluster.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Job Templates
    api_response = api_instance.get_job_templates(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_job_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

**list[str]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> list[RestObject] get_jobs(x_ms_as_user=x_ms_as_user, node_names=node_names, properties=properties, owner=owner, filter=filter, sort_jobs_by=sort_jobs_by, asc=asc, start_row=start_row, rows_per_read=rows_per_read, query_id=query_id)

Get Job List

Gets all/filtered jobs for the HPC cluster.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
node_names = 'node_names_example' # str | A comma-separated list of nodes names. It will list jobs running on these nodes. When this parameter is specified, all other parameters except the \"x-ms-as-user\" header are ignored. All properties of a jobs will be retrieved. An invalid name will be ignored.  (optional)
properties = 'Id,Owner,Name,State,Priority' # str | A comma-separated list of the names for the properties of the jobs for which you want to get values. See [ISchedulerJob](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897474%28v%3dvs.85%29) for available properties. (optional) (default to Id,Owner,Name,State,Priority)
owner = 'owner_example' # str | The user who created, submitted, or queued the job. (optional)
filter = 'filter_example' # str | Filter jobs by specified filters. A filter is in the form of \"<name>%20eq%20<value>\", and multiple filters can be ANDed like \"<filter1>%20and%20<filter2>…\". Available filter names are _JobState_, _NodeGroup_ and _ChangeTimeFrom_.  (optional)
sort_jobs_by = 'Id' # str | A job property by which jobs will be sorted. If this parameter is not specified or a property with a specified name does not exist for a job, the result will be sorted by job Id. (optional) (default to Id)
asc = true # bool | Specifies the sort order. (optional)
start_row = 8.14 # float | Specifies the start number of rows to read. The number of the first row is 0. When this parameter presents, pagination is activated and _queryId_ is ignored. And the total number of rows will be returned in the response header _x-ms-row-count_, while no _x-ms-continuation-queryId_ will be returned. (optional)
rows_per_read = 10 # int | Specifies how many rows of data to retrieve each time. (optional) (default to 10)
query_id = 'query_id_example' # str | The value of the _x-ms-continuation-queryId_ header from the previouse response of this operation, used for reading the next page of data. (optional)

try:
    # Get Job List
    api_response = api_instance.get_jobs(x_ms_as_user=x_ms_as_user, node_names=node_names, properties=properties, owner=owner, filter=filter, sort_jobs_by=sort_jobs_by, asc=asc, start_row=start_row, rows_per_read=rows_per_read, query_id=query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **node_names** | **str**| A comma-separated list of nodes names. It will list jobs running on these nodes. When this parameter is specified, all other parameters except the \&quot;x-ms-as-user\&quot; header are ignored. All properties of a jobs will be retrieved. An invalid name will be ignored.  | [optional] 
 **properties** | **str**| A comma-separated list of the names for the properties of the jobs for which you want to get values. See [ISchedulerJob](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897474%28v%3dvs.85%29) for available properties. | [optional] [default to Id,Owner,Name,State,Priority]
 **owner** | **str**| The user who created, submitted, or queued the job. | [optional] 
 **filter** | **str**| Filter jobs by specified filters. A filter is in the form of \&quot;&lt;name&gt;%20eq%20&lt;value&gt;\&quot;, and multiple filters can be ANDed like \&quot;&lt;filter1&gt;%20and%20&lt;filter2&gt;…\&quot;. Available filter names are _JobState_, _NodeGroup_ and _ChangeTimeFrom_.  | [optional] 
 **sort_jobs_by** | **str**| A job property by which jobs will be sorted. If this parameter is not specified or a property with a specified name does not exist for a job, the result will be sorted by job Id. | [optional] [default to Id]
 **asc** | **bool**| Specifies the sort order. | [optional] 
 **start_row** | **float**| Specifies the start number of rows to read. The number of the first row is 0. When this parameter presents, pagination is activated and _queryId_ is ignored. And the total number of rows will be returned in the response header _x-ms-row-count_, while no _x-ms-continuation-queryId_ will be returned. | [optional] 
 **rows_per_read** | **int**| Specifies how many rows of data to retrieve each time. | [optional] [default to 10]
 **query_id** | **str**| The value of the _x-ms-continuation-queryId_ header from the previouse response of this operation, used for reading the next page of data. | [optional] 

### Return type

[**list[RestObject]**](RestObject.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_group**
> NodeGroup get_node_group(name, x_ms_as_user=x_ms_as_user)

Get Node Group

Get a node group by name.

### Example
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
name = 'name_example' # str | Node group name.
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Node Group
    api_response = api_instance.get_node_group(name, x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node group name. | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**NodeGroup**](NodeGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_groups**
> list[NodeGroup] get_node_groups(x_ms_as_user=x_ms_as_user)

Get Node Group List

Get the names and descriptions for all of the node groups for the HPC cluster.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Node Group List
    api_response = api_instance.get_node_groups(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**list[NodeGroup]**](NodeGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_of_group**
> list[str] get_nodes_of_group(name, x_ms_as_user=x_ms_as_user)

Get Nodes of a Group

Get the list of the nodes that belong to the specified node group.

### Example
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
name = 'name_example' # str | Node group name.
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Nodes of a Group
    api_response = api_instance.get_nodes_of_group(name, x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_nodes_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node group name. | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

**list[str]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtask**
> list[RestProperty] get_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, properties=properties)

Get Subtask

Get the values of the specified properties for the specified subtask, or the values of all of the properties if no properties are specified. Only Parameteric Sweep job have subtasks.

### Example
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
task_id = 56 # int | Task Id
subtask_id = 56 # int | Subtask Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = 'properties_example' # str | A comma-separated list of the names for the properties of the subtask for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the subtask. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v=vs.85)) for avaialbe properties. (optional)

try:
    # Get Subtask
    api_response = api_instance.get_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_subtask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **subtask_id** | **int**| Subtask Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | **str**| A comma-separated list of the names for the properties of the subtask for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the subtask. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v&#x3D;vs.85)) for avaialbe properties. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> list[RestProperty] get_task(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)

Get Task

Get the values of the specified properties for the specified task, or the values of all of the properties if no properties are specified.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = 'properties_example' # str | A comma-separated list of the names for the properties of the task for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the task. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v=vs.85)) for avaialbe properties. (optional)

try:
    # Get Task
    api_response = api_instance.get_task(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | **str**| A comma-separated list of the names for the properties of the task for which you want to get values. If you do not specify this parameter, the response contains values for all of the properties of the task. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v&#x3D;vs.85)) for avaialbe properties. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_custom_properties**
> list[RestProperty] get_task_custom_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, names=names)

Get Task Custom Properties

Get the values of the specified custom properties for the task, or the values of all of the properties if none are specified.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
names = 'names_example' # str | A comma-separated list of the names for the custom properties of the task for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the custom properties for the task. (optional)

try:
    # Get Task Custom Properties
    api_response = api_instance.get_task_custom_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, names=names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_custom_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **names** | **str**| A comma-separated list of the names for the custom properties of the task for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the custom properties for the task. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_environment_variables**
> list[RestProperty] get_task_environment_variables(job_id, task_id, x_ms_as_user=x_ms_as_user, names=names)

Get Task Environment Variables

Get the values of the specified environment variables for the task, or the values of all of the environment variables if none are specified.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
names = 'names_example' # str | A comma-separated list of the names for the environment variables in the task for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the environment variables for the task. If an environment variable with a specified name does not exist for the task, the response contains an empty string for the value of that environment variable. (optional)

try:
    # Get Task Environment Variables
    api_response = api_instance.get_task_environment_variables(job_id, task_id, x_ms_as_user=x_ms_as_user, names=names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_environment_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **names** | **str**| A comma-separated list of the names for the environment variables in the task for which you want to get values. If you do not specify the Names parameter, the response contains values for all of the environment variables for the task. If an environment variable with a specified name does not exist for the task, the response contains an empty string for the value of that environment variable. | [optional] 

### Return type

[**list[RestProperty]**](RestProperty.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> list[RestObject] get_tasks(job_id, x_ms_as_user=x_ms_as_user, properties=properties, expand_parametric=expand_parametric, filter=filter, sort_tasks_by=sort_tasks_by, asc=asc, start_row=start_row, rows_per_read=rows_per_read, query_id=query_id)

Get Task List

Get the values of the properties for all of the tasks in the specified job.

### Example
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
properties = 'TaskId,Name,State,CommandLine,ExitCode,ParentJobId,JobTaskId,InstanceId' # str | A comma-separated list of the names for the properties of the tasks for which you want to get values. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v=vs.85)) for avaialbe properties. (optional) (default to TaskId,Name,State,CommandLine,ExitCode,ParentJobId,JobTaskId,InstanceId)
expand_parametric = true # bool | Specifies whether to get properties only for the master task for a parametric sweep task, or for all of the subtasks instead. True indicates that you want to get properties for all of the subtasks. False indicates that you want to get properties only for the master task. (optional) (default to true)
filter = 'filter_example' # str | Filter tasks by specified filters. A filter is in the form of \"<name>%20eq%20<value>\", and multiple filters can be ANDed like \"<filter1>%20and%20<filter2>…\". Available filter names are _TaskState_, _ChangeTimeFrom_, _TaskStates_, _TaskIds_ and _TaskInstanceIds_.  (optional)
sort_tasks_by = 'TaskId' # str | A task property by which tasks will be sorted. If this parameter is not specified or a property with a specified name does not exist for a task, the result will be sorted by task Id. (optional) (default to TaskId)
asc = true # bool | Specifies the sort order. (optional)
start_row = 8.14 # float | Specifies the start number of rows to read. The number of the first row is 0. When this parameter presents, pagination is activated and _queryId_ is ignored. And the total number of rows will be returned in the response header _x-ms-row-count_, while no _x-ms-continuation-queryId_ will be returned. (optional)
rows_per_read = 10 # int | Specifies how many rows of data to retrieve each time. (optional) (default to 10)
query_id = 'query_id_example' # str | The value of the _x-ms-continuation-queryId_ header from the previouse response of this operation, used for reading the next page of data. (optional)

try:
    # Get Task List
    api_response = api_instance.get_tasks(job_id, x_ms_as_user=x_ms_as_user, properties=properties, expand_parametric=expand_parametric, filter=filter, sort_tasks_by=sort_tasks_by, asc=asc, start_row=start_row, rows_per_read=rows_per_read, query_id=query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | **str**| A comma-separated list of the names for the properties of the tasks for which you want to get values. See [ISchedulerTask](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/cc897577(v&#x3D;vs.85)) for avaialbe properties. | [optional] [default to TaskId,Name,State,CommandLine,ExitCode,ParentJobId,JobTaskId,InstanceId]
 **expand_parametric** | **bool**| Specifies whether to get properties only for the master task for a parametric sweep task, or for all of the subtasks instead. True indicates that you want to get properties for all of the subtasks. False indicates that you want to get properties only for the master task. | [optional] [default to true]
 **filter** | **str**| Filter tasks by specified filters. A filter is in the form of \&quot;&lt;name&gt;%20eq%20&lt;value&gt;\&quot;, and multiple filters can be ANDed like \&quot;&lt;filter1&gt;%20and%20&lt;filter2&gt;…\&quot;. Available filter names are _TaskState_, _ChangeTimeFrom_, _TaskStates_, _TaskIds_ and _TaskInstanceIds_.  | [optional] 
 **sort_tasks_by** | **str**| A task property by which tasks will be sorted. If this parameter is not specified or a property with a specified name does not exist for a task, the result will be sorted by task Id. | [optional] [default to TaskId]
 **asc** | **bool**| Specifies the sort order. | [optional] 
 **start_row** | **float**| Specifies the start number of rows to read. The number of the first row is 0. When this parameter presents, pagination is activated and _queryId_ is ignored. And the total number of rows will be returned in the response header _x-ms-row-count_, while no _x-ms-continuation-queryId_ will be returned. | [optional] 
 **rows_per_read** | **int**| Specifies how many rows of data to retrieve each time. | [optional] [default to 10]
 **query_id** | **str**| The value of the _x-ms-continuation-queryId_ header from the previouse response of this operation, used for reading the next page of data. | [optional] 

### Return type

[**list[RestObject]**](RestObject.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[UserRole] get_user_roles(x_ms_as_user=x_ms_as_user)

Get Cluster User Roles

Get the roles of the cluster user who makes the API call.

### Example
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
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Get Cluster User Roles
    api_response = api_instance.get_user_roles(x_ms_as_user=x_ms_as_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

[**list[UserRole]**](UserRole.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_nodes_of_group**
> list[str] move_nodes_of_group(name, x_ms_as_user=x_ms_as_user, operation=operation)

Add/Remove Nodes to/from a Group

Add nodes to, or remove nodes from, a node group.

### Example
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
name = 'name_example' # str | Node group name.
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
operation = swagger_client.NodeGroupOperation() # NodeGroupOperation |  (optional)

try:
    # Add/Remove Nodes to/from a Group
    api_response = api_instance.move_nodes_of_group(name, x_ms_as_user=x_ms_as_user, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->move_nodes_of_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node group name. | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **operation** | [**NodeGroupOperation**](NodeGroupOperation.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_cluster_node**
> operate_cluster_node(name, operation, x_ms_as_user=x_ms_as_user)

Operate a Cluster Node

The requested operation will be performed asynchronously. The API doesn't ensure it's successfully on return. The caller has to query the node state for the operation result. 

### Example
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
name = 'name_example' # str | Node name
operation = 'operation_example' # str | 
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Operate a Cluster Node
    api_instance.operate_cluster_node(name, operation, x_ms_as_user=x_ms_as_user)
except ApiException as e:
    print("Exception when calling DefaultApi->operate_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node name | 
 **operation** | **str**|  | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeue_job**
> requeue_job(job_id, x_ms_as_user=x_ms_as_user)

Requeue Job

Resubmit the specified job to the queue.

### Example
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

try:
    # Requeue Job
    api_instance.requeue_job(job_id, x_ms_as_user=x_ms_as_user)
except ApiException as e:
    print("Exception when calling DefaultApi->requeue_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeue_subtask**
> requeue_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user)

Requeue Subtask

Move a failed, canceled, or queued subtask to the configuring state so that the subtask can be queued again when the job is resubmitted.

### Example
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
task_id = 56 # int | Task Id
subtask_id = 56 # int | Subtask Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)

try:
    # Requeue Subtask
    api_instance.requeue_subtask(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user)
except ApiException as e:
    print("Exception when calling DefaultApi->requeue_subtask: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **subtask_id** | **int**| Subtask Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requeue_task**
> requeue_task(job_id, task_id, x_ms_as_user=x_ms_as_user, message=message)

Requeue Task

Move a failed, canceled, or queued task to the configuring state so that the task can be queued again when the job is resubmitted.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
message = 'message_example' # str | A message for the operation. (optional)

try:
    # Requeue Task
    api_instance.requeue_task(job_id, task_id, x_ms_as_user=x_ms_as_user, message=message)
except ApiException as e:
    print("Exception when calling DefaultApi->requeue_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **message** | **str**| A message for the operation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_job_custom_properties**
> set_job_custom_properties(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Job Custom Properties

Set the values of custom properties for a job.

### Example
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
properties = [swagger_client.RestProperty()] # list[RestProperty] | Custom properties for the job (optional)

try:
    # Set Job Custom Properties
    api_instance.set_job_custom_properties(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_job_custom_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Custom properties for the job | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_job_environment_variables**
> set_job_environment_variables(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Job Environment Variables

Sets the values of environment variables for a job.

### Example
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
properties = [swagger_client.RestProperty()] # list[RestProperty] | Environment variables for the job (optional)

try:
    # Set Job Environment Variables
    api_instance.set_job_environment_variables(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_job_environment_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Environment variables for the job | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_job_properties**
> set_job_properties(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Job Properties

Set the values for the properties of the specified job.

### Example
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
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of job to set (optional)

try:
    # Set Job Properties
    api_instance.set_job_properties(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_job_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of job to set | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subtask_properties**
> set_subtask_properties(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Subtask Properties

Set the values of properties for a subtask in a job.

### Example
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
task_id = 56 # int | Task Id
subtask_id = 56 # int | Subtask Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of subtask to set. (optional)

try:
    # Set Subtask Properties
    api_instance.set_subtask_properties(job_id, task_id, subtask_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_subtask_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **subtask_id** | **int**| Subtask Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of subtask to set. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_custom_properties**
> set_task_custom_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Task Custom Properties

Set the values of custom properties for a task.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Custom properties for the task (optional)

try:
    # Set Task Custom Properties
    api_instance.set_task_custom_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_task_custom_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Custom properties for the task | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_environment_variables**
> set_task_environment_variables(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Task Environment Variables

Set the value of one or more environment variables for a task.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Environment variables for the task (optional)

try:
    # Set Task Environment Variables
    api_instance.set_task_environment_variables(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_task_environment_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Environment variables for the task | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_properties**
> set_task_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)

Set Task Properties

Set the values of properties for a task in a job.

### Example
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
task_id = 56 # int | Task Id
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of task to set. (optional)

try:
    # Set Task Properties
    api_instance.set_task_properties(job_id, task_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->set_task_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **task_id** | **int**| Task Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of task to set. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job**
> submit_job(job_id, x_ms_as_user=x_ms_as_user, properties=properties)

Submit Job

Submit a job to the HPC Job Scheduler Service so that the HPC Job Scheduler Service can add the job to the queue of jobs to run. If the credentials for the account under which the job should run are not cached on the server, you can set them in the UserName and Password properties. A job that is submitted by this operation is not validated. After the job is submitted, you can get information about the job by using the Get Job operation.

### Example
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
properties = [swagger_client.RestProperty()] # list[RestProperty] | Properties of job to submit (optional)

try:
    # Submit Job
    api_instance.submit_job(job_id, x_ms_as_user=x_ms_as_user, properties=properties)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Job Id | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **properties** | [**list[RestProperty]**](RestProperty.md)| Properties of job to submit | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_group**
> NodeGroup update_node_group(name, x_ms_as_user=x_ms_as_user, node_group=node_group)

Update Node Group

Update a node group.

### Example
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
name = 'name_example' # str | Node group name.
x_ms_as_user = 'x_ms_as_user_example' # str | The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. (optional)
node_group = swagger_client.NodeGroup() # NodeGroup |  (optional)

try:
    # Update Node Group
    api_response = api_instance.update_node_group(name, x_ms_as_user=x_ms_as_user, node_group=node_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_node_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Node group name. | 
 **x_ms_as_user** | **str**| The name of user whom you want to make request as. You must be an HPC Pack administrator or HPC Pack Job administrator to make it work. | [optional] 
 **node_group** | [**NodeGroup**](NodeGroup.md)|  | [optional] 

### Return type

[**NodeGroup**](NodeGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

