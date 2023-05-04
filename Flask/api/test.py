import requests

BASE="http://127.0.0.1:5000/"

data = [
    {"likes": 10, "name":"jordy", "views":10000000},
    {"likes": 78, "name":"how to make rest api", "views":80000},
    {"likes": 65, "name":"joe", "views":7893},
]

# testing put
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# testing deleting
response = requests.delete(BASE + "video/0")
print(response)

#testing get
input()
response = requests.get(BASE + "video/1")
print(response.json())

# response = requests.get(BASE + "helloworld/tim/19")
# print(response.json())