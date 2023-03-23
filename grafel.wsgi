#!/usr/bin/python


##!/usr/local/apache2/grafel/grafel/venv/bin/python

activate_this = '/usr/local/apache2/grafel/grafel/venv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))


import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/usr/local/apache2/grafel/")

from grafel import app as application
application.secret_key = 'S3cr3tK3y'
