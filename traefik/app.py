# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         print(f"Request body: {request.data}")
#     return 'Origin works!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True)

from flask import Flask, request
import logging
import os

app = Flask(__name__)

# 创建日志目录
log_directory = "/"

# 配置日志
log_file = os.path.join(log_directory, "app.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     logging.info(f"Request method: {request.method}")
#     logging.info(f"Request URL: {request.url}")
#     logging.info(f"Request headers: {request.headers}")

#     if request.method == 'POST':
#         logging.info(f"Request body: {request.data}")
#     elif request.method == 'GET':
#         logging.info(f"Query string: {request.args}")

#     return 'Origin works!'
    
@app.route('/', methods=['GET', 'POST'])
def index():
    logging.debug(f"Request method: {request.method}")
    logging.debug(f"Request URL: {request.url}")
    logging.debug(f"Request headers: {request.headers}")

    if request.method == 'POST':
        logging.debug(f"Request body: {request.data}")
    elif request.method == 'GET':
        logging.debug(f"Query string: {request.args}")

    return 'Origin works!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)