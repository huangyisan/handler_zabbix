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