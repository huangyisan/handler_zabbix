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

`output_data` 输出内容

`kv` 过滤内容
```
zabbix_hosts = ZabbixHosts()
output_data = ["hostid","host"]
host = ["Zabbix-01","Zabbix-02"]
print(zabbix_hosts.get_customer_hosts(output_data=output_data,host=host))

output:
[{'hostid': '10422', 'host': 'Zabbix-02'}, {'hostid': '10084', 'host': 'Zabbix-01'}]
```





Feature Support
---------------

- login

