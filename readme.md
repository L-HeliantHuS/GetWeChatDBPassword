# GetWeChatDBPassword
用于获取`Windows`版本的微信聊天记录数据库密码, 可以自己添加各种版本的偏移量.

## 介绍
#### config.py
用于配置版本号以及偏移量

#### main.py
主程序, 通过[Pymem](https://github.com/srounet/Pymem)模块来进行进程中内存数据的查找 (果然好东西知道的人就是少, 这东西真的好用).

程序运行结果示例: 
```python
        当前微信版本: 2.9.0.123,
        WeChatWin.Dll的基地址为: 0x78880000,
        最终密码的位置为: 0x79f34d50,
        ChatMsg.db的密码为: d1eef413cac44d5a9572411334144af01de56ddf05aa49a3b820b8c1a6a9bc35,
        解密数据库的C语言格式密码:
        unsigned char pass[] = {0xd1, 0xee, 0xf4, 0x13, 0xca, 0xc4, 0x4d, 0x5a, 0x95, 0x72, 0x41, 0x13, 0x34, 0x14, 0x4a, 0xf0, 0x1d, 0xe5, 0x6d, 0xdf, 0x05, 0xaa, 0x49, 0xa3, 0xb8, 0x20, 0xb8, 0xc1, 0xa6, 0xa9, 0xbc, 0x35, };



            Enjoy Python!
```
程序编写时, `Windows`版本微信最新版本为`2.9.0.123`

## 感谢
程序使用`PyCharm`进行编写, 特此感谢[JetBrains](https://www.jetbrains.com/)提供的开源许可。