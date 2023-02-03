from flask import Flask, request, render_template
import csv
from datetime import datetime
import requests
import time
import csv

API_ENDPOINT = "https://member.mailingboss.com/integration/index.php/lists/subscribers/create/110895:d9db4a4176ee8a69750ba441cfe97a5d"
LIST_UID = '63c20cebe240f'
PATH = 'importacao.csv'
now = datetime.now()
app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_content = file.read().decode('utf-8')
    email_list = file_content.split("\n")
    

    
    for i in email_list:
        print(i)
       
        # name = list(get_csv_column(PATH, 1))[i]
        status = 'confirmed'
        data = {
            'list_uid': LIST_UID,

            'email': i,
            #    'name': name,
            'status': status
        }
        time.sleep(5)
        r = requests.post(url=API_ENDPOINT, data=data)
        pastebin_url = r.text
        
        print(
            "Tentativa de cadastro no horário: {} no email: {} resposta do Json: {}"
            .format(now, i, pastebin_url))
        print("IMPORTADO COM SUCESSO !")
        


if __name__ == "__main__":
    app.run(debug=True)
    rota = app.run(host='0.0.0.0', port=8080)
    print (rota)

