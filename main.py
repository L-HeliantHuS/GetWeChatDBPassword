import pymem
import config
import struct
import binascii

def getCBytes(password):
    result = ""
    for i in range(0, len(password), 2):
        result += "0x" + password[i:i+2] + ", "



    return """
        unsigned char pass[] = {%s};
    """%(result)
def getPassword(p) -> (str, int, str):
    # 得到这个进程加载的WeChatWin.dll的基地址
    base_address = pymem.process.module_from_name(p.process_handle, "wechatwin.dll").lpBaseOfDll

    # 获得一个地址中内存的数据
    result = p.read_bytes(base_address + config.wechatOffset, 4)
    addr = struct.unpack("<I", result)[0]

    # 读上一个内存中存储的地址的内容
    password = p.read_bytes(addr, 0x20)

    # 解码
    result = binascii.b2a_hex(password)
    return base_address, result.decode()

def printResult(base_offset, password):
    print(f"""
        当前微信版本: {config.wechatVersion},
        WeChatWin.Dll的基地址为: {hex(base_offset)},
        最终密码的位置为: {hex(base_offset + config.wechatOffset)},
        ChatMsg.db的密码为: {password},
        解密数据库的C语言格式密码: {getCBytes(password)}


            Enjoy Python!
    """)

if __name__ == '__main__':
    p = pymem.Pymem()
    p.open_process_from_name("WeChat.exe")
    base_offset, password = getPassword(p)
    printResult(base_offset, password)



