Zabbix_templates
----------------
- 获取指定template名称对应id `get_template_id`
```
template = ZabbixTemplates()
templatename = ['Flume_Process_Running_Check','DNS OS Linux']
print(template.get_template_id(templatename=templatename))

output:
[{'templateid': '10832', 'host': 'DNS OS Linux'}, {'templateid': '10836', 'host': 'Flume_Process_Running_Check'}]
```

- 批量关联hosts和template `mass_add_templates`

## 该功能可能异常

```
mass_template = ZabbixTemplates()
hosts_list = [{'hostid': '10423'}, {'hostid': '10433'}]
mass_template.mass_add_templates(templatename="Flume_Process_Running_Check", hosts_list=hosts_list)

output：
None
```