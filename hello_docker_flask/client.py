import requests
#x = float(x)
res = requests.get("http://localhost:5000/multiply?x={0}".format(2.0))
data = res.json()
print(data)
print("get : ", data['result'])
r = requests.post("http://localhost:5000/add", json={'x': 2.5, 'y':3.5})
print(r.json()["result"])
print(r.status_code, r.reason)