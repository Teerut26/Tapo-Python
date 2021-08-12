import requests
def getData(url, headers, payload, verify=False):
    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=verify)
    return response.text
