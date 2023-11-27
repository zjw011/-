import random
import string
from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 处理登录逻辑
        username = request.form.get('username')
        password = request.form.get('password')
        address = request.form.get('address')
        beizhu = request.form.get('beizhu')

        if username and password and address:  # 判断用户名、密码和地址都不为空
            # 在这里进行登录验证等操作

            # 连接到 MongoDB 数据库
            client = pymongo.MongoClient("mongodb://182.43.225.101:32769/")

            # 创建一个名为 "customers" 的集合
            db = client["mydatabase"]
            collection = db["users"]

            deviceID = ''.join(random.sample(string.digits + string.ascii_lowercase, 36))
            data = [
                {
                    "enabled": True,
                    "adddate": "2023-11-16 09:56:53",
                    "enddate": "2023-12-16 09:56:53",
                    "name": beizhu,
                    "phone": username,
                    "password": password,
                    "deviceId": "iphone",
                    "dToken": deviceID,
                    "modify_coordinates": False,
                    "address": address,
                    "longitude": "113.462502",
                    "latitude": "34.146873",
                    "pushmode": 2,
                    "pushdata": {
                        "Ding": {
                            "Secret": None,
                            "Token": None
                        },
                        "PushPlus": {
                            "Token": "aea58034f194403e984dca157b7d6776"
                        },
                        "Server_Turbo": {
                            "Token": None
                        },
                        "Email": {
                            "Send": None,
                            "Password": None,
                            "Server_Address": None,
                            "Smtp_Port": None,
                            "Receiver": None
                        }
                    }
                }
            ]

            # 向集合中插入数据
            collection.insert_many(data)
            return redirect(url_for('game'))


        else:
            error = '请填写完整的登录信息'
            return render_template('index.html', error=error)

    return render_template('index.html')


@app.route('/game')
def game():
    client = pymongo.MongoClient("mongodb://182.43.225.101:32769/")

    # 创建一个名为 "customers" 的集合
    db = client["mydatabase"]
    collection = db["users"]
    data = collection.find()  # 获取数据库中的数据

    return render_template('game.html', data=data)  # 将数据传递给模板进行展示


if __name__ == '__main__':
    app.run(debug=True)
