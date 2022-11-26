import json
import urllib.request
resp = urllib.request.urlopen("https://api.gcorelabs.com/cdn/public-ip-list")
f = open('ip.txt','w')
ele_json = json.loads(resp.read())
for ips in ele_json['addresses']:
    f.write(ips+"\n")
for ips in ele_json['addresses_v6']:
    f.write(ips+"\n")
f.close()