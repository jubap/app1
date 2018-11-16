import db
import json
import requests
import io

from flask import Flask, render_template, url_for, json, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "OLA MUNDO!"


@app.route('/ola')
def ola():
    return "OLA!!!!!"


@app.route('/listar')
def lista():
    html = ['<ul>']
    for username, user in db.users.items():

        html.append(
            f"<li>{user['name']}- {username}</li>"
        )
    html.append('</ul>')
    return '\n'.join(html)


@app.route('/listar2')
def lista2():
    arq = 'db2.json'

    with open(arq, mode='r') as f:
        json_data = json.load(f)

    result_list = []

    for json_dict in json_data:
        result_list.append('<ul>')
        result_list.append(json_dict['name'] + '<br>')
        result_list.append(json_dict['partType'] + '<br>')
        result_list.append(json_dict['partCode'] + '<br>')
        result_list.append('</ul>')

    return '\n'.join(result_list)


@app.route('/listar3')
def lista3():
    arq = 'db2.json'

    with open(arq, mode='r') as f:
        json_data = json.load(f)

    result_list = [(f'<br>{json_dict["name"]}<br>{json_dict["partCode"]}<br>')
                   for json_dict in json_data]

    return '\n'.join(result_list)


@app.route('/lejson')
def le_json():

    arq = 'http://bkapp.devedp.com.br:6080/hom/v2/catalog/api/catalog/product/get?BkNumber=22121&productId=d6210f1a-e48b-4f41-a774-486fa7ed68f9'

    r = read_json_from_file_as_dictionary(arq)
    return r['data']


@app.route('/clima',methods=['GET'])
def clima():
    nv_cidade = request.from.get('city')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    cidade = 'São Paulo'

    if nv_cidade : 
        cidade = nv_cidade


    clima_data = []

    r = requests.get(url.format(cidade)).json()
    Clima = {
        'cidade': cidade,
        'temperatura': (r['main']['temp']),
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']

    }

    clima_data.append(Clima)

    return render_template('clima.html',clima_data=clima_data)


@app.route("/json")
def readwrite():

     #html :""

    #arq = 'http://bkapp.devedp.com.br:6080/hom/v2/catalog/api/catalog/product/get?BkNumber=22121&productId=d6210f1a-e48b-4f41-a774-486fa7ed68f9'

    r = ''  # requests.get(arq).json()

    print(r)

    return r


def read_json_from_file_as_dictionary(json_file_path):
    import json
    with io.open(json_file_path, 'r', encoding='utf8') as content_file:
        complete_json = content_file.read()
        return json.loads(complete_json)
# use_reloader=True,


app.run(host='10.200.24.177')
