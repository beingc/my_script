#!/usr/bin/env python3
# coding=utf-8
# Date: 2023-07-01
# Desc: mock simple interface

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test/setCodeV1', methods=['POST'])
def set_code():
    print(request.data)
    return jsonify({'resultCode': '0', 'resultDesc': 'success'})


if __name__ == '__main__':
    app.run(host='192.168.0.177', port=8080)
