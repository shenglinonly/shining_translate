import execjs
import requests

youdao_url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1515437214@10.169.0.82; OUTFOX_SEARCH_USER_ID_NCOO=952066673.3810828; JSESSIONID=aaatF34s9lXLg5bHQdU0x; ___rl__test__cookies=1637155464608',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}


def translate(word):
    with open('js_decrypt.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()
    compile_result = execjs.compile(js_code)
    encode_result = compile_result.call('youdao', word)  # js加密后的结果

    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        # 'salt': '16371554646124',
        # 'sign': '6b299f9b6b4e40586ca521654f29dbcd',
        # 'lts': '1637155464612',
        # 'bv': 'c795a332c678d5063a1ee5eb15253848',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    data.update(encode_result)

    response = requests.post(url=youdao_url, data=data, headers=headers)
    json_data = response.json()
    # print(json_data)

    """提取翻译的结果"""
    trans_result = json_data['translateResult'][0][0]['tgt']
    # print(translateResult)
    return trans_result


if __name__ == '__main__':
    word = input('请输入你想翻译的内容')
    translate()

