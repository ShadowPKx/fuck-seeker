import logging

from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


print('''
Разработчик: @nkitas
Наш канальчик в тг: @Termuxtop
 ▄▄ • ▄▄▄ .▄▄▄▄▄ ▄▄▄·      .▄▄ · 
▐█ ▀ ▪▀▄.▀·•██  ▐█ ▄█▪     ▐█ ▀. 
▄█ ▀█▄▐▀▀▪▄ ▐█.▪ ██▀· ▄█▀▄ ▄▀▀▀█▄
▐█▄▪▐█▐█▄▄▌ ▐█▌·▐█▪·•▐█▌.▐▌▐█▄▪▐█
·▀▀▀▀  ▀▀▀  ▀▀▀ .▀    ▀█▄▀▪ ▀▀▀▀ 
''')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/print-data', methods=['POST', 'GET'])
def print_data():
    print(request.get_data().decode('utf-8'))
    return jsonify({'success': '1'})


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app, log = None)
    http_server.serve_forever()