Zabbix_HostGroups
--------------
**新增**

**删除**

**修改**

**过滤**

* **获取自定义hostgroup数据** `get_customer_hostgroups`

  * 参数
    - name: 待查询组名
    - output_data: 输出过滤内容，默认为groupid,name
    
  * 样例
  
    ```
    zabbix_hostgroups = ZabbixHostGroups()
    name = ['test-zabbix','DNS-lts']
    print(zabbix_hostgroups.get_customer_hostgroups(name=name))
     
    output:
    [{'groupid': '324', 'name': 'DNS-lts'}, {'groupid': '321', 'name': 'test-zabbix'}]
    ```