import requests


def SendRequest(url, method):

    if method == "GET":
        response = requests.get(url)
        return response.json()
    if method == "POST":
        response = requests.post(url)
        return response.json()
    if method == "PUT":
        response = requests.put(url)
        return response.json()
    if method == "DELETE":
        response = requests.delete(url)
        return response.json()
