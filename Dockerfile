FROM httpd:2.4

RUN apt-get update && apt-get install python3 virtualenv libapache2-mod-wsgi-py3 curl -y

RUN mkdir grafel && mkdir grafel/grafel

RUN virtualenv -p /usr/bin/python3  grafel/grafel/venv

COPY install-python-dependencies.sh requirements.txt ./

RUN ./install-python-dependencies.sh

COPY __init__.py grafel.conf grafel/grafel/

COPY grafel.wsgi  grafel/

COPY httpd.conf  /usr/local/apache2/conf/


