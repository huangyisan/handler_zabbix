import password
authinfo = {
    'username': 'Admin',
    'password': password.password,
    'url': 'http://{0}/zabbix/'.format(password.ip),
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