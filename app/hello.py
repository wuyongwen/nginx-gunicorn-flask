""" hello.py """

import logging
from flask import Flask, jsonify
from multiprocessing import Process,Lock
import os
import time

app = Flask(__name__)
lock=Lock()
@app.route('/')
def hello():
    n = 's'
    lock.acquire()
    app.logger.info('%s: %s is running' %(n,os.getpid()))
    time.sleep(20)
    app.logger.info('%s:%s is done' %(n,os.getpid()))
    lock.release()

    return jsonify({
        'hello': 'world'
    })

# make app to use gunicorn logger handler
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
