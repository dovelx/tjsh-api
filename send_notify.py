import requests
import time
import hmac
import hashlib
import base64
import urllib.parse


def send_wxwork_notify_markdown(content, api_key, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    hook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}".format(api_key)
    data = {"msgtype": "markdown",
            "markdown": {
                "content": "{}".format(content)
            }}
    notify_res = requests.post(url=hook_url, json=data, headers=headers)
    return notify_res


def send_wxwork_notify_text(content, mentioned_mobile_list, api_key, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    if not mentioned_mobile_list or not isinstance(mentioned_mobile_list, list):
        raise TypeError("mentioned_mobile_list should be a list!")
    hook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}".format(api_key)
    data = {"msgtype": "text",
            "text": {
                "content": "{}".format(content),
                "mentioned_mobile_list": mentioned_mobile_list
            }}
    notify_res = requests.post(url=hook_url, json=data, headers=headers)
    return notify_res


def send_ding_talk_notify_markdown(content_title, content_text, access_token, at_mobiles=[], secret=None, headers=None):
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    hook_url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(access_token)
    if secret:
        timestamp, sign = generate_timestamp_and_sign(secret)
        hook_url = "https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}".format(access_token,
                                                                                                      timestamp, sign)
    data = {
        "msgtype": "markdown",
    }
    if at_mobiles and "@all" in at_mobiles:
        data['markdown'] = {
            "title": "{} @all".format(content_title),
            "text": "{} @all".format(content_text)
        }
        data['at'] = {
            "atMobiles": at_mobiles,
            "isAtAll": True
        }
    elif at_mobiles and "@all" not in at_mobiles:
        if len(at_mobiles) > 1:
            at_mobiles_str = "@".join(at_mobiles)
            at_mobiles_str = "@{}".format(at_mobiles_str)
        else:
            at_mobiles_str = "@{}".format(at_mobiles[0])
        data['markdown'] = {
            "title": "{} {}".format(content_title, at_mobiles_str),
            "text": "{} {}".format(content_text, at_mobiles_str)
        }
        data['at'] = {
            "atMobiles": at_mobiles,
            "isAtAll": True
        }
    notify_res = requests.post(url=hook_url, json=data, headers=headers)
    return notify_res


def generate_timestamp_and_sign(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


if __name__ == "__main__":

    import datetime
    import global_result
    now = datetime.datetime.now().date()
    executed_history_id = time.strftime('%Y%m%d', time.localtime())
    #send_ding_talk_notify_markdown(content_title, content_text, access_token, at_mobiles=[], secret=None, headers=None):
    # 获取dingtalk token url
    access_token = 'd1c7782d9e3cb687c018e1b08f503685ac7bb8490192cc6fb62bb7284760692b'
    #397939e6742eb8ef2d3a3c461574715d36ce95d717345d858a2f6f76a0d0b7b0
    #access_token = '397939e6742eb8ef2d3a3c461574715d36ce95d717345d858a2f6f76a0d0b7b0'
    content_title = 'apitest'
    res = global_result.CollectResult()
    content_text =  str(now) + res  + ' 详情链接:https://1533963bv3.oicp.vip/test_report' + str(executed_history_id) + '.html'
    # 钉钉消息内容，注意test是自定义的关键字，需要在钉钉机器人设置中添加，这样才能接收到消息
    content_text = content_text

    # 要@的人的手机号，可以是多个，注意：钉钉机器人设置中需要添加这些人，否则不会接收到消息
    at_mobiles = ['所有人']
    # 发送钉钉消息
    send_ding_talk_notify_markdown(content_title, content_text, access_token, at_mobiles, secret="", headers="")