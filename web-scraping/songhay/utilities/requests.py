import requests

def getHtml(uri):
    response = requests.get(uri)
    html = response.content.decode()

    return html