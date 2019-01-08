authinfo = {
    'username': 'Admin',
    'password': '!',
    'url': 'http://10.1.18.1/zabbix/'
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