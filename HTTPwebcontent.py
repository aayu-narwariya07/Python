# Task1
# Making the get requests
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print("Request was successful. ")
    # print the JSON data returned by the request
    posts = response.json()
    for post in posts:
        print(f"Title: {post['title']}")
else:
    print(f"Request faild with status code: {response.status_code}")

# Task 2.
# making the post request
import requests
data = {
    'tital': 'foo',
    'body': 'bar',
    'userId' : 1
    }

# making the post request
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
if response.status_code == 201:
    print("Resource created successfully. ")
    print("Response data:", response.json())

else:
    print(f"Request faild with status code: {response.status_code}")

# Task 3.
# making a put request

import requests
data = {
    'id': 1,
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}

response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
if response.status_code == 200:
    print("Resource updated successfully.")
    print("Response data:", response.json())
else:
    print(f"Request faild with status code: {response.status_code}")

# Task 4.
#  Making a DELETE request
import requests
response = requests.delete('https://jsonplaceholder.typicode.com/posts1')
if response.status_code == 200:
    print("Response deleted successfully.")
else:
    (f"Request faild with status code: {response.status_code}")

# Task 5.
# Sending a get request with query paremeters
import requests
params = {
    'userId' : 1
}
response = requests.get('https://jsonplaceholder.typicode.com/posts',params=params)
if response.status_code == 200:
    print("Request was successful.")
    posts = response.json()
    for post in posts:
        print(f"Title: {post['title']}")
else:
    print(f"Request failed with stutus code: {response.status_code}")
