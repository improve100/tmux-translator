# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
from imp import reload

import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '7ef8a8eb0c08a737'
APP_SECRET = 'WBTRKPsT7qssAI8WM7zonmVy3Rp7NQ8x'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # return requests.post(YOUDAO_URL, data=data, headers=headers)
    return requests.get(YOUDAO_URL, params=data).json()


def connect():
    # q = "DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses"
    q = "Deprecation"

    data = {}
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = "您的用户词表ID"

    response = do_request(data)
    print(response)
    # contentType = response.headers['Content-Type']
    # if contentType == "audio/mp3":
    #     millis = int(round(time.time() * 1000))
    #     filePath = "合成的音频存储路径" + str(millis) + ".mp3"
    #     fo = open(filePath, 'wb')
    #     fo.write(response.content)
    #     fo.close()
    # else:
    #     print(type(response.content))
    #     # import json
    #     # print(response.content)
    #     # print(json.dumps(response.content))
    #     print(response.text)


if __name__ == '__main__':
    connect()
