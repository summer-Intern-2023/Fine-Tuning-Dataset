import json
import random

path = "/home/vcp/YiMu/LLaMA-Efficient-Tuning/data/data_zh/"


def split_text_by_essay(text):
    essay_list = text.split("\n\n")
    new_list = list(filter(None, essay_list))
    return new_list


def split_title_and_content(text):
    output_list = []
    title_random_list = [
        ["你是一个小学生，请你以：", " 为题来写一篇文章"],
        ["老师今天布置了一篇文章：", "，请你写一篇文章"],
        ["请你以：", "为题来写一篇文章"],
        ["请你以：", "为题写一篇文章"],
        ["作文题目是：", "，请你写一篇文章"],
        ["暑假来了，你的作业是：", "，请你写一篇文章"],
        ["周六日，老师布置了一篇作文：", "，请你这个为题写一篇文章"],
        ["请你以：", "写一篇文章"],
        ["老师，您能按照题目写一下这篇文章吗？题目：", ""],
        ["老师，您能写一篇满分作文嘛？题目：", ""],
        ["老师，您能按照题目写一篇作文嘛？题目：", ""],
        ["老师，您能按照题目写一篇高分作文嘛？题目：", ""],
        ["老师，您能按照题目写一篇优秀作文嘛？题目：", ""],
    ]
    for t in text:
        title_and_content_list = t.split()
        title = title_and_content_list[0]
        content = title_and_content_list[2:]
        random_num_generation = random.randint(1, 3)
        existing_set = set()
        for _ in range(random_num_generation):
            text_dict = {}
            random_title_choose_int = random.randint(0, len(title_random_list) - 1)
            while random_title_choose_int in existing_set:
                random_title_choose_int = random.randint(0, len(title_random_list) - 1)
            text_dict["instruction"] = (
                title_random_list[random_title_choose_int][0]
                + title
                + title_random_list[random_title_choose_int][1]
            )
            text_dict["input"] = ""
            text_dict["output"] = "".join(content)
            text_dict["history"] = []
            output_list.append(text_dict)
    print(len(output_list))
    return output_list


def test_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(len(data))
            print("test json file success")
    except IOError:
        print("Error: 没有找到文件或读取文件失败")


if __name__ == "__main__":
    file_names = input()
    file_names = file_names.split()
    file_names += ["essay/essay.txt", "essay/glm.txt"]
    total_convert_list = []
    for file in file_names:
        print(path + file)
        try:
            with open(path + file, "r", encoding="utf-8") as f:
                text = f.read()

                text_list = split_text_by_essay(text)
                output_list = split_title_and_content(text_list)
                total_convert_list.extend(output_list)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")

    try:
        with open(
            path + "essay/essay00.json", "w", encoding="utf-8"
        ) as fout:
            json.dump(total_convert_list, fout, ensure_ascii=False)
    except IOError:
        print("Error: 写入文件失败")

    merge_file_names = input("merge_file names: ")
    merge_file_names = merge_file_names.split()
    merge_file_names += [
        "dataset_from_llama/refgpt_zh_50k_p2.json",
        "dataset_from_llama/comparison_gpt4_data_zh.json",
        "dataset_from_llama/oaast_sft_zh.json",
        "dataset_from_llama/alpaca_gpt4_data_zh.json",
        "dataset_from_llama/alpaca_data_zh_51k.json",
        "text_book/essay_zh_4shang.json",
        "text_book/essay_zh_4xia.json",
        "text_book/essay_zh_5shang.json",
        "text_book/essay_zh_5xia.json",
        "text_book/essay_zh_6shang.json",
        "text_book/essay_zh_6xia.json",
        "chat_history/chathistory00.json",
        "chat_history/chathistory01.json",
        "dictionary/siziciyu.json",
        "essay/sentence_zh.json",
        "essay/essay00.json",
        "essay/essay01.json",
    ]
    total_merge_list = []
    for file in merge_file_names:
        try:
            with open(path + file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for d in data:
                    if "history" not in d.keys():
                        d["history"] = []
                    if type(d["history"]) == str and len(d["history"]) > 0:
                        d["history"] = [d["history"]]
                    elif len(d["history"]) == 0:
                        d["history"] = []
                    if "output" not in d.keys():
                        d["output"] = ""
                    if type(d["output"]) == list and len(d["output"]) > 0:
                        d["output"] = "".join(i for i in d["output"])
                total_merge_list.extend(data)
        except IOError:
            print(f"Error: 没有找到{path + file}或读取文件失败")

    try:
        with open("/home/vcp/YiMu/LLaMA-Efficient-Tuning/data/data_zh.json", "w", encoding="utf-8") as fout:
            json.dump(total_merge_list, fout, ensure_ascii=False)
    except IOError:
        print("Error: 写入文件失败")

    test_json_file("/home/vcp/YiMu/LLaMA-Efficient-Tuning/data/data_zh.json")
