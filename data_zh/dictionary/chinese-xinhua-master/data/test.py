import json

import random

# 定义问题库，包含十个问题
question_bank = [
    "请你解释作文中会用到的词语",
    "我不太能理解这个词语",
    "请你给我解释一下词语",
    "我们作文中用到了一个词语，我不太明白是什么意思，这个词语是：",
    "作文中的词语是什么意思，这个词语是：",
    "请你给我解释一下四字词语",
]

def get_random_question():
    return random.choice(question_bank)

output_list = []
# 逐行读取 JSON 文件并处理每个字典的 "word" 字段
with open('idiom.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        ci = item.get('word')
        explanation = item.get('explanation')
        text_dict = {}
        random_question = get_random_question()
        text_dict["instruction"] = random_question + "'"+ ci + "'"
        text_dict["input"] = ""
        text_dict["output"] = explanation
        text_dict["history"] = []
        output_list.append(text_dict)

with open(r'siziciyu.json', "w", encoding='utf-8') as fout:
   json.dump(output_list , fout, ensure_ascii=False)
'''
with open('idiom.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        word = item.get('word')
        print(word)
'''
