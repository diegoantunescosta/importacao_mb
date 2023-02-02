import csv
from datetime import datetime
import requests
import time
import csv

API_ENDPOINT = "https://member.mailingboss.com/integration/index.php/lists/subscribers/create/110895:d9db4a4176ee8a69750ba441cfe97a5d"
LIST_UID = '62e7d1065030b'
PATH = 'importacao.csv'

with open(PATH, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
now = datetime.now()


def get_csv_column(filename, column):
    with open(filename) as stream:
        reader = csv.reader(stream)
        for row in reader:
            yield row[column]


for i in range(15000, 50000):
    email = list(get_csv_column(PATH, 0))[i]

    # name = list(get_csv_column(PATH, 1))[i]
    status = 'confirmed'
    data = {
        'list_uid': LIST_UID,
        'email': email,
        #    'name': name,
        'status': status
    }
    time.sleep(1)
    r = requests.post(url=API_ENDPOINT, data=data)
    pastebin_url = r.text
    print(email)
    print(
        "Tentativa de cadastro no horário: {} no email: {} resposta do Json: {}"
        .format(now, email, pastebin_url))
print("IMPORTADO COM SUCESSO !")
