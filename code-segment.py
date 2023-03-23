import flask
from flask import request
from flask import jsonify

import requests


json = {
    'dashboardId': 20, 
    'evalMatches': [
        {
            'value': 88.21247214016819, 'metric': '{instance="node_exporter_host:9100", job="server_target"}', 
            'tags': {'instance': 'node_exporter_host:9100', 'job': 'server_target'}
        }
    ], 
    'message': 'Alarma con el nivel de swap consumido en el servidor.', 
    'orgId': 1, 
    'panelId': 12, 
    'ruleId': 16, 
    'ruleName': 'Swap alarm level 2', 
    'ruleUrl': 'http://localhost:3000/d/gx1ihprMz/artifactory-alerts?tab=alert&editPanel=12&orgId=1', 
    'state': 'alerting', 
    'tags': {'ACTION': 'clean-swap', 'ALARM_LEVEL': '2', 'ALARM_TYPE': 'SWAP', 'TARGET': 'server_target'}, 
    'title': '[Alerting] Swap alarm level 2'
}


if 'tags' in json:
    if 'ACTION' in json['tags']:

        action = json['tags']['ACTION']
        target = json['tags']['TARGET']

        print(action)
        print(target)

        url = "http://jenkinsurl:8080/job/DevOps/job/webhook-trigger/buildWithParameters?token=hIXQZLbnut89tnb8P6xo2kuPEcaCz83B&action=' + action + '&target=" + target

        print(url)

        result = requests.get(url)

        print(result)

