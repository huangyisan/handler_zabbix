authinfo = {
    'username': 'Admin',
    'password': '!',
    'url': 'http://1.1.1.1/zabbix/',
    # 'url': 'http://ip/zabbix/'
}

auth_payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "{0}".format(authinfo.get('username','')),
        "password": "{0}".format(authinfo.get('password',''))
    },
    "id": 1,
}