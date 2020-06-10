import logging
import os

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


os.system('cls' if os.name=='nt' else 'clear')

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
    app.run()
