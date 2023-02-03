import requests

url = "http://localhost:5000/api/upload"
file = {"file": open("importacao.csv", "rb")}

response = requests.post(url, files=file)

print(response.text)