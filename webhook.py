import flask
from flask import request
from flask import jsonify

import requests

proxies = {
  'http': 'http://jvilleos:06Jvo%40D3v0Ps202..@proxyune.epmtelco.com.co:8080',
  'https': 'http://jvilleos:06Jvo%40D3v0Ps202..@proxyune.epmtelco.com.co:8080',
}


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def home():
    print("Recibiendo peticion de grafana")
    print("Datos enviados de grafana: ")
    #print(request.data)
    #print(request.args.to_dict())
    #print(request.form.to_dict())



    #print(request.json['title'])
    print(request.json)

    print("Enviando mensaje a telegram")

    token = '1718076208:AAEakKONzljeSrmMVC9Qoo8jONo1kTddO9s'
    chat_id = '-1001238999974'
    message = request.json['title']
    #message = request.json['message']

    current_value =  request.json["evalMatches"][0]["value"]
    server = request.json["evalMatches"][0]["tags"]["job"]
    message = request.json["message"] + "\n" + "Servidor: " + server + "\n" + "Valor medido: " + str(current_value)


    url = 'https://api.telegram.org/bot1718076208:AAEakKONzljeSrmMVC9Qoo8jONo1kTddO9s/sendMessage'

    data = {'chat_id': chat_id, 'text': message }

    result = requests.post(url, data=data, proxies=proxies)

    print(result)

    resp = jsonify(success=True)
    resp.status_code = 200;

    return resp

    
app.run(host='10.100.82.70', port=5000)
