Handler_zabbix: zabbix api SDK
=========================================
**打算写一个zabbix api的sdk工具**

Zabbix_Hosts
--------------
- 获取所有hosts数据 `get_all_hosts`
```
zabbix_hosts = ZabbixHosts()
print(zabbix_hosts.get_all_hosts())

output:
[{'hostid': '10084', 'proxy_hostid': '0', 'host': 'Zabbix-01', 'status': '0', 'disable_until': '0', 'error': '', 'available': '1', 'errors_from': '0', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'Zabbix-01', 'flags': '0', 'templateid': '0', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': '', 'proxy_address': '', 'auto_compress': '1'}, {'hostid': '10422', 'proxy_hostid': '10260', 'host': 'Zabbix-02', 'status': '0', 'disable_until': '0', 'error': '', 'available': '1', 'errors_from': '0', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'Zabbix-02', 'flags': '0', 'templateid': '0', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': '', 'proxy_address': '', 'auto_compress': '1'}]
```

- 自定义获取hosts数据 `get_customer_hosts`

```
zabbix_hosts = ZabbixHosts()
output_data = ["hostid","host"]
host = ["Zabbix-01","Zabbix-02"]
print(zabbix_hosts.get_customer_hosts(output_data=output_data,host=host))

output:
[{'hostid': '10422', 'host': 'Zabbix-02'}, {'hostid': '10084', 'host': 'Zabbix-01'}]
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
    - 新增host，单个或者多个 (undo)
    - 删除host，单个或者多个 (undo)
    - 修改host，单个或者批量 (undo)
    - 查询host，单个或者多个 (doing)
        - 返回所有的host信息 (done)
        - 根据host名称查询，精确或者通配
        - 能返回需要的数据，比如返回hostid，ip等属性
    - 过滤host，根据条件过滤
        - 只返回proxy_hosts节点
        - 只返回监控状态服务器
        - 限定输出条目
        
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