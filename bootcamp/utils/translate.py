# -*- coding: utf-8 -*-

import os
import requests
import random
import json
from hashlib import md5
from retrying import retry

# Set your own appid/appkey.
appid = os.environ.get('BAIDU_APPID', '')
appkey = os.environ.get('BAIDU_APPKEY', '')

def retry_if_result_error(result):
    return not result

@retry(retry_on_result=retry_if_result_error, stop_max_attempt_number=2)
def get_translate(text, from_lang='en', to_lang='zh'):
    if not text: return text
    # zh 中文; cht 繁体中文; en 英文; id 印尼语; th 泰语; vie 越南语; kor 韩语; jp 日语；默认：auto
    if from_lang not in ['cht', 'en', 'id', 'th', 'vie', 'kor', 'jp']: from_lang = 'auto'
    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)
    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    # Send request
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    result = requests.post(url, params=payload, headers=headers).json()
    result = '\n'.join([i.get('dst', '') for i in result.get('trans_result', [])])
    return result


if __name__ == '__main__':

    query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'
    print(get_translate(query))
