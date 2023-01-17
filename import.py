import csv
from datetime import datetime
import requests
import time
import pandas as pd

API_ENDPOINT = "https://member.mailingboss.com/integration/index.php/lists/subscribers/create/110895:d9db4a4176ee8a69750ba441cfe97a5d"
LIST_UID = '62e7d1065030b'
PATH = 'importacao_email (1).csv'
results = pd.read_csv(PATH)
ROWS = len(results) + 1
now = datetime.now()


def get_csv_column(filename, column):
    with open(filename) as stream:
        reader = csv.reader(stream)
        for row in reader:
            yield row[column]


for i in range(1, ROWS):
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
    print(
        "Tentativa de cadastro no horário: {} no email: {} resposta do Json: {}"
        .format(now, email, pastebin_url))
print("IMPORTADO COM SUCESSO !")
