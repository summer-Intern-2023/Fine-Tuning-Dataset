import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

# 读取 JSON 文件内容
with open('siziciyu.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# 验证 JSON 文件是否符合正确的 JSON 格式
if is_valid_json(json_data):
    print("JSON 文件内容符合正确的 JSON 格式")
else:
    print("JSON 文件内容不符合正确的 JSON 格式")
