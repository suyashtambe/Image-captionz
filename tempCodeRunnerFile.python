import requests

url = 'http://127.0.0.1:5000/generate'
data = {
    'place': 'beach',
    'weather': 'sunny',
    'description': 'a beautiful sunset'
}

response = requests.post(url, json=data)
print(response.json())
