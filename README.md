Handler_zabbix: zabbix api SDK
=========================================
**打算写一个zabbix api的sdk工具**

Zabbix_Hosts
--------------
**新增**

**删除**

**修改**

**过滤**

* 获取所有hosts数据 `get_all_hosts`
  
  * 样例
  
    ```
    zabbix_hosts = ZabbixHosts()
    print(zabbix_hosts.get_all_hosts())
           
    output:
    [{'hostid': '10084', 'proxy_hostid': '0', 'host': 'Zabbix-01', 'status': '0', 'disable_until': '0', 'error': '', 'available': '1', 'errors_from': '0', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'Zabbix-01', 'flags': '0', 'templateid': '0', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': '', 'proxy_address': '', 'auto_compress': '1'}, {'hostid': '10422', 'proxy_hostid': '10260', 'host': 'Zabbix-02', 'status': '0', 'disable_until': '0', 'error': '', 'available': '1', 'errors_from': '0', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'Zabbix-02', 'flags': '0', 'templateid': '0', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': '', 'proxy_address': '', 'auto_compress': '1'}]
    ```
    
* 自定义获取hosts数据 `get_customer_hosts`

  * 参数
    - countoutput: 输出匹配条目数
    - limit: 限制输出条目数，默认50
    - visiable: 是否打印输出payload
    - proxy_hosts: 是否只输出proxy_host
    - monitored_hosts: 是否只输出监控中的机器
    - output_data: 指定输出内容
    - **kwargs: 过滤规则
    
  * 样例
        
    ```    
    zabbix_hosts = ZabbixHosts()
    output_data = ["hostid","host"]
    host = ["FuJian-QZDX-Gateway","BeiJing-TZLT-Gateway"]
    print(zabbix_hosts.get_customer_hosts(countoutput=True,limit=40,visiable=1,output_data=output_data,monitored_hosts="true",host=host))
           
    output:
    [{'hostid': '10422', 'host': 'Zabbix-02'}, {'hostid': '10084', 'host': 'Zabbix-01'}]
    ```    

* 搜索hosts数据 `search_hosts_payload`
    
  * 参数

    - 已开启searchWildcardsEnabled,searchByAny参数
    - countoutput: 输出匹配条目数
    - limit: 限制输出条目数，默认50
    - visiable: 是否打印输出payload
    - output_data: 指定输出内容
    - **kwargs: 搜索规则
    
  * 样例
  
    ```
    zabbix_hosts = ZabbixHosts()
    output_data = ["hostid","host","status"]
    host = ["FuJian-XMYD-L1*","BeiJing-*Gateway"]
    print(zabbix_hosts.search_customer_hosts(countoutput=True,visiable=True,output_data=output_data,host=host))
           
    output:
    5
    ```
    
* 添加单个host `add_hosts`

  * 参数
    
    - host: 待添加主机名称
    - groupid: 待加入的主机组，可多个
    - templateid: 待加入模板，可多个，但模板一些特定key需要interfaces支持，比如snmp的模板，则需要使用snmp的方式才可以添加
    - _type: interfaces 参数
    - main: interfaces 参数
    - useip: interfaces 参数
    - ip: interfaces 参数
    - dns: interfaces 参数
    - port: interfaces 参数
    - check: 是否检查模式，默认为True，检查模式只打印payload，不会提交数据。
    
  * 样例
  
  ```
    zabbix_hosts = ZabbixHosts()
    host = 'test-zabbix'
    groupid = ["320","307"]
    templateid = ["10001","10788"]
    zabbix_hosts.add_hosts(host=host,groupid=groupid,check=False,templateid=templateid)
    
    output:
    ****************************************
    SUCCESS: Add host [test-zabbix] success!
    ****************************************
    Recall Message:
    {'hostids': ['10873']}
  ```
  
* 删除hosts `delete_hosts`

  * 参数
  
    - hostsids: 单个或者多个hostid
    - check: 检查模式，默认为True，检查模式只打印payload，不会提交数据。
    
  * 样例
  
  ```
    zabbix_hosts = ZabbixHosts()
    hostsids = ["10876","10877"]
    zabbix_hosts.delete_hosts(hostsids=hostsids,check=False)
    
    output:
    **************************************************
    SUCCESS: Delete host [['10876', '10877']] success!
    **************************************************
    Recall Message:
    {'hostids': ['10876', '10877']}
  ```
    
Zabbix_templates
----------------
- 获取指定template名称对应id `get_template_id`
```
template = ZabbixTemplates()
print(template.get_template_id(templatename='Flume_Process_Running_Check'))

output:
10836
```

- 批量关联hosts和template `mass_add_templates`

```
mass_template = ZabbixTemplates()
hosts_list = [{'hostid': '10423'}, {'hostid': '10433'}]
mass_template.mass_add_templates(templatename="Flume_Process_Running_Check", hosts_list=hosts_list)

output：
None
```





Feature Support
---------------
- hosts  (doing)
    - 新增host，单个 (done)
        - ~~关联单个或者多个主机组 (done)~~
        - ~~关联单个或者多个template模板 (done)~~
    - 批量增加host (undo)
    - ~~删除host，单个或者多个 (done)~~
    - 修改host，单个或者批量 (undo)
    - ~~查询host，单个或者多个 (done)~~
        - ~~返回所有的host信息~~
        - ~~根据host名称查询，支持通配~~
        - ~~能返回需要的数据，比如返回hostid，ip等属性~~
        - ~~限定输出条目~~
        - ~~只输出数据条目~~
    - ~~过滤host，根据条件过滤(done)~~
        - ~~只返回proxy_hosts节点~~
        - ~~只返回监控状态服务器~~
        - ~~限定输出条目~~
        - ~~只输出数据条目~~
        
- host group (undo)
    - 新增host group，单个或者多个
    - 删除host group，单个或者多个
    - 修改host group，单个或者批量
    - 查询host group，单个或者多个

- items (undo)
    - 新增item
    - 删除item
    - 修改item
    - 查询item

- trigger (undo)
    - 新增trigger
    - 删除trigger
    - 删除trigger依赖关系
    - 修改trigger
    - 查询trigger
    
- alert (undo)
    - 查询alert
    
- screen (undo)
    - 新增screen
    - 删除screen
    - 修改screen
    - 查询screen
    
- 输出约定:
    - SUCCESS:
    
    需要输出status(SUCCESS), recall message
    
    example:
    
    ```
    ****************************************
    SUCCESS: Add host [test-zabbix] success!
    ****************************************
    Recall message:
    {'hostids': ['10862']}
    ```

    - ERROR:

    需要输出status(ERROR),reason,payload
    
    example:
    
    ```
    ***************************************
    ERROR: Add host [test-zabbix] failure !
    ***************************************
    Reason: The host may already exists or other fault!
    The payload is:
    {'jsonrpc': '2.0', 'method': 'host.create', 'params': {'host': 'test-zabbix', 'interfaces': [{'type': 1, 'main': 1, 'useip': 1, 'ip': '127.0.0.1', 'dns': '', 'port': '10050'}], 'groups': [{'groupid': '320'}]}, 'auth': 'aa311fe719e1479bd1f462e61bcb6035', 'id': 1}
    
    ```