import requests
def multiply(self, x):
    res = requests.get("http://localhost:5000/multiply/",x)
    data = res.json()
    print(data['result'])
#class ApiClient:
    