# -*- coding:utf8 -*-
import json
import random

cet4_file = open("CET4_edited.json", encoding="utf8")
cet4_str = cet4_file.read()
cet4_file.close()
cet4_json = json.loads(cet4_str)
print (cet4_json["total"],end="\n=============================\n")

while True:
    random_num = random.randint(0, cet4_json["total"])
    print (cet4_json["words"][random_num]["english_word"])
    str = input()
    if(str == "q"):
        break
    print (cet4_json["words"][random_num]["chinese_word"],end="\n=============================\n")