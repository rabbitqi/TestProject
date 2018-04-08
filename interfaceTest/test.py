# _*_ coding:utf-8 _*_
#!/usr/bin/python

import json,requests
import sendEmail

with open('config.json', 'r',encoding='UTF-8') as fr:
    o = json.load(fr)
    print(o)

baseUrls = o['baseUrls']
interfaces = o['interfaces']
print(baseUrls)
print(interfaces)
for baseUrl in baseUrls:
    baseUrlName = baseUrl['name']
    baseUrlHost = baseUrl['host']
    print(baseUrlName + '-----------' + baseUrlHost)
    for interface in interfaces:
        interfaceName = interface['name']
        interfaceUrl = baseUrlHost + interface['url']
        print(interfaceName + '----------' + interfaceUrl)
        try:
            s = requests.get(interfaceUrl, allow_redirects=False)
        except Exception as e:
            print(e)
        if (200 == s.status_code):
            print(s.status_code)
            print('1111111')
        else:
            print(str(s.status_code) + '---' + baseUrlName + '-' + interfaceName + '-' + interface['url'])
            sendEmail.send(str(s.status_code), baseUrlName, interfaceName, interface['url'])


