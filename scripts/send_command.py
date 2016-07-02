import requests

def send_command(command):
    try:
        url = 'http://192.168.1.90/jsondata.cgi'
        auth = ('admin', '5885')
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        data = 'data=[["settaggi", "11", 1]]'
        response = requests.post(url, auth=auth, headers=headers, json=data)
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Connection timeout")
    except requests.exceptions.RequestException:
        print("Connection error")


data = send_command(12)
print(data)
