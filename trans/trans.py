import hashlib
import json
import random
import requests
import pandas as pd
import time
import csv

url = "http://api.fanyi.baidu.com/api/trans/vip/translate"


appid = ''  # appid
secretKey = ''  # 密钥

# appid = ''  # 你的appid陈磊阳
# secretKey = ''  # 你的密钥陈磊阳

salt = random.randint(32768, 65536)
errorcodenum = 0


def write_csv(file_name, rows):
    # ‘a’是追加模式，可以改成'w'——覆盖写模式
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(rows + '\n')


def get_tra_res(q, fromLang='auto', toLang='en'):
    global errorcodenum
    # 生成签名
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    # post请求参数
    data = {
        "appid": appid,
        "q": q,
        "from": fromLang,
        "to": toLang,
        "salt": str(salt),
        "sign": sign,
    }
    # post请求
    try:
        res = requests.post(url, data=data)
        # 返回时一个json
        trans_result = json.loads(res.content)
        print(trans_result)
        if ('error_code' in trans_result):
            if (trans_result['error_code'] == '52001'):
                if errorcodenum > 3:
                    errorcodenum = 0
                    return q
                else:
                    errorcodenum = errorcodenum + 1
                    get_tra_res(q, fromLang='auto', toLang='en')
            if (trans_result['error_code'] == '52002'):
                return q

        else:
            return trans_result['trans_result'][0]['dst']
    except:
        get_tra_res(q, fromLang='auto', toLang='en')


def main():
    # datas = []
    ix = 0
    for i in range(19, 31):
        print(i)
        csv_data = pd.read_csv('C:/Users/Administrator/Desktop/translate/0825/hkx_08' +str(i) + '.csv')  # 读取训练数据
        # csv_data = pd.read_csv('C:/Users/Administrator/Desktop/translate/0811/2500raw' +'.csv')  # 读取训练数据
        x = csv_data.loc[0:, ['tweet']].values
        x = x.reshape(1, len(x)).tolist()  # 转换成 List [[1, 2, 3]]
        x = list(x[0])
        # del x[0: 13217]
        for value in x:
            tran = get_tra_res(value, fromLang='auto', toLang='en')
            if tran is None:
                tran = ''
            write_csv('C:/Users/Administrator/Desktop/translate/0825_trans/hkx_tweet_trans_08' +str(i) + '.csv', tran)
            # write_csv('C:/Users/Administrator/Desktop/translate/0811_trans/hkx_tweet_trans_2500raw' + '.csv', tran)
            print(ix)
            ix = ix + 1
            time.sleep(0.5)


if __name__ == '__main__':
    # get things rolling
    main()
