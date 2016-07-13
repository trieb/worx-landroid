import requests
import json

def send_command(command):
    try:
        url = 'http://192.168.1.90/jsondata.cgi'
        auth = ('admin', '0000')
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        data = 'data=[["settaggi",{},1]]'.format(str(command))
        response = requests.post(url, auth=auth, headers=headers, data=data)
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Connection timeout")
    except requests.exceptions.RequestException:
        print("Connection error")

def check_data(data, command):
    result = data['settaggi'][command]
    print("Command {} was set to: {}".format(command, result))

command = 11
data = send_command(command)
if data is not None:
    check_data(data, command)

print(data['settaggi'])


