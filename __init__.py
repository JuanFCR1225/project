import os
import configparser
import flask
from flask import request
from flask import jsonify

import requests


cfg = configparser.ConfigParser()
print(os.getcwd())
cfg.read(os.getcwd() + '/grafel/grafel/grafel.conf')
jenkins_username = cfg.get('jenkins', 'user').strip()
jenkins_token = cfg.get('jenkins', 'user_api_token').strip()
jenkins_actions_router_job = cfg.get('jenkins', 'actions_router_job').strip()
jenkins_actions_router_job_token = cfg.get('jenkins', 'actions_router_job_token').strip()


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

    #ejecutar actions de alarmas de grafana
    if 'tags' in request.json:
        if 'ACTION' in request.json['tags']:

            print("Ejecutando action de alarma grafana")

            action = request.json['tags']['ACTION']
            target = request.json['tags']['TARGET']

            

            url = "http://10.100.82.238:8080/job/DevOps/job/webhook-trigger/buildWithParameters?token=hIXQZLbnut89tnb8P6xo2kuPEcaCz83B&action=" + action + "&target=" + target
            
            print(url)

            #result = requests.get(url, proxies=proxies, auth=auth, timeout=(60,60))
            cmd = 'curl -vvv  --noproxy "*" -u ' + jenkins_username + ':' + jenkins_token + ' "' + jenkins_actions_router_job  + '?token=' + jenkins_actions_router_job_token + '&action=' + action + '&target=' + target + '"'
            print(cmd)
            os.system(cmd)

            # print(result.status_code)
            # print(result.content)
            # print(result.text)


    #resultado del webhook

    resp = jsonify(success=True)
    resp.status_code = 200;


    return resp





if __name__ == '__main__':    
    app.run()
