from Zabbix_Hosts.zabbix_handler_hosts import ZabbixHosts
from Zabbix_Templates.zabbix_handler_templates import ZabbixTemplates
import re

hosts = ZabbixHosts()

pattern = '.*-flume-.*'
a = re.match(pattern, 'hosts', re.I)

output_data = ["hostid","host"]
hosts = hosts.get_customer_info(output_data=output_data)
hostsid = []
for i in hosts:
    print(i)
    if re.match(pattern, i.get('host'), re.I):
        hostsid.append(i.get('hostid'))

hosts_list = [{'hostid':i} for i in hostsid]

mass_template = ZabbixTemplates()
mass_template.mass_add_templates(templateid=, hosts_list=hosts_list)
