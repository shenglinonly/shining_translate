# 自制翻译小软件



**效果预览 !**

![Snipaste_2022-07-22_20-59-41.png](https://s2.loli.net/2022/07/23/3lSRjPtKsId6ZJf.png)



**软件采用Python, PyQt5等技术, 从底层逻辑到页面设计都是小编亲手设计的, 满满自豪感😊!**



## 底层逻辑

### 爬虫

>**底层的翻译功能是对接到了有道翻译, 采用爬虫的方式, 调取接口,部分代码如下**

```python
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
```

### js 解密
> **因为其中的请求字段还遇到了 js 加密, 所以我们还需要进行 js 解密, js 解密部分代码如下 (完整代码可以自行网上搜索哦)**

```javascript
var n = function (e, t) {
    return e << t | e >>> 32 - t
}
    , r = function (e, t) {
    var n, r, i, o, a;
    return i = 2147483648 & e,
        o = 2147483648 & t,
        n = 1073741824 & e,
        r = 1073741824 & t,
        a = (1073741823 & e) + (1073741823 & t),
        n & r ? 2147483648 ^ a ^ i ^ o : n | r ? 1073741824 & a ? 3221225472 ^ a ^ i ^ o : 1073741824 ^ a ^ i ^ o : a ^ i ^ o
}
    , i = function (e, t, n) {
    return e & t | ~e & n
}
    , o = function (e, t, n) {
    return e & n | t & ~n
}
    , a = function (e, t, n) {
    return e ^ t ^ n
}
```

## 页面设计

### 图形界面

> **页面设计核心技术用到pyqt5, 设计软件用到qtdesigner, 这款软件设计起来还是很方便的, 很多控件直接拖拽即可, 最后布个局就完啦, 关于pyqt5可以看这个[网站](https://www.byhy.net/tut/py/gui/qt_01/)哦, 个人认为还是很详细的**.

### 控件逻辑

本软件有`点击翻译`和`清空文本`等功能, 并且需要与翻译脚本通信, 具体代码如下:

```python
from PyQt5 import uic
from translates import translate as trans
from threading import Thread


class Stats:
    def __init__(self):
        self.ui = uic.loadUi("ui\\translate.ui")
        self.ui.pushButton.clicked.connect(self.translate)
        self.ui.pushButton_2.clicked.connect(self.remove)
        # self.trans = trans(self.trans_text)

    def translate(self):
        def run():
            trans_text = self.ui.textEdit.toPlainText()
            trans_result = trans(trans_text)
            return trans_result
        thread = Thread(target=run)
        thread.start()
        self.ui.textEdit_2.setPlainText(run())

    def remove(self):
        self.ui.textEdit_2.setPlainText('')
        self.ui.textEdit.setPlainText('')


```



## 打包

打包用到了pyinstaller, 一行命令就解决啦

```
pyinstaller -F -w -i logo.ico main.py
```



**这就是整个软件的思路和步骤啦, 感兴趣的小伙伴可以点个赞哦**👍

​																											-----作者shiningonly
