Handler_zabbix: zabbix api SDK
=========================================
**打算写一个zabbix api的sdk工具**


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