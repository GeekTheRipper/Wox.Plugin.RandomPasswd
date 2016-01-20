#encoding=utf8
import json
import re,os
import random

from wox import Wox,WoxAPI

class Shadowsocks(Wox):

    # def generate_random_passwd(self,params):
    def generate_random_passwd(self,digits,is_rand_letter,is_rand_num,is_rand_punc):

        # digits=params[0]
        # is_rand_letter=params[1]
        # is_rand_num=params[2]
        # is_rand_punc=params[3]

        randSource=""
        if is_rand_letter:
            randSource+="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        if is_rand_num:
            randSource+="0123456789"
        if is_rand_punc:
            randSource+="!\"#$%&'()*+,-./:;<=>?@[\\]_`{|}~"

        randpass=""
        for i in range(digits):  
            randpass+=(random.choice(randSource))

        
        command = 'echo ' + "^^^" + "^^^".join(randpass.strip()) + '| clip'
        os.system(command)
        # WoxAPI.show_msg("成功","已生成 {} 位随机密码到剪贴板".format(digits))

    def query(self,query):
        digits=[]
        res = []

        for i in range(4):
            if not query:
                digits.append(random.randint(10,20))
            elif query.isdigit():
                digits.append(int(query))
            else:
                res.append({
                    "Title": "错误的输入，请输入一个整数作为参数",
                    "IcoPath":"randpass-error.png"
                    })
                return res

        res.append({
            "Title": "生成 {} 位随机密码到剪贴板（大小写字母、随机数、符号）".format(digits[0]),
            "IcoPath":"randpass1.png",
            "JsonRPCAction":{"method": "generate_random_passwd", "parameters": [digits[0],True,True,True]}
            })
        res.append({
            "Title": "生成 {} 位随机密码到剪贴板（大小写字母、随机数）".format(digits[1]),
            "IcoPath":"randpass2.png",
            "JsonRPCAction":{"method": "generate_random_passwd", "parameters": [digits[1],True,True,False]}
            })
        res.append({
            "Title": "生成 {} 位随机密码到剪贴板（大小写字母）".format(digits[2]),
            "IcoPath":"randpass3.png",
            "JsonRPCAction":{"method": "generate_random_passwd", "parameters": [digits[2],True,False,False]}
            })
        res.append({
            "Title": "生成 {} 位随机密码到剪贴板（随机数）".format(digits[3]),
            "IcoPath":"randpass4.png",
            "JsonRPCAction":{"method": "generate_random_passwd", "parameters": [digits[3],False,True,False]}
            })
        if not query:
            res.append({
                "Title": "未指定密码位数，将生成随机位随机密码",
                "IcoPath":"randpass.png"
                })

        return res

if __name__ == "__main__":
    Shadowsocks()
