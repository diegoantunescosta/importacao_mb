import requests

url = "http://34.207.64.245:8080/api/upload"
file = {"file": open("importacao.csv", "rb")}

response = requests.post(url, files=file)

print(response.text)