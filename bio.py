# coding:utf-8

"""
构造NER训练集，实体序列标注，训练BERT+BiLSTM+CRF
"""

# 进行标注的内容 路径
file = r"C:\Users\leade\Desktop\data\train2.txt"
# 标注写入的文件路经
output_path = r"C:\Users\leade\Desktop\data\train_pos.txt"
# 存储 不同标注的词 列表
key_list = []
company_list = []
Radical_list = []

# 读取词
with open(r"C:\Users\leade\Desktop\data\new_key.txt", "r", encoding='utf-8') as kf:
    for ik in kf:
        key_list.append(ik.strip())

with open(r"C:\Users\leade\Desktop\data\company.dict", "r", encoding='utf-8') as cf:
    for ic in cf:
        company_list.append(ic.strip())
with open(r"C:\Users\leade\Desktop\data\radical.txt", "r", encoding='utf-8') as rf:
    for ir in rf:
        Radical_list.append(ir.strip())

# 读取标注的文章，按行标注
with open(file, encoding='utf-8') as f:
    for line in f:
        # 去除首末的空白格及 \n等符号
        q_str = ''.join([word.strip() for word in line.strip() if word not in [" ", ' ', 'O', 'o']])
        # 是否是空的
        if q_str:  # new question answer triple
            q_list = list(q_str)  # 单个列表
            tag_list = ["O" for i in range(len(q_list))]  # 生成 标注列表

            # 一、这里的代码都是标注的代码
            for entities in key_list:
                y = True
                ind = 0
                if entities in q_str:
                    while y:
                        tag_start_index = q_str.find(entities, ind)
                        if tag_start_index != -1:
                            for i in range(tag_start_index, tag_start_index + len(entities)):
                                if tag_start_index == i:
                                    tag_list[i] = "B-PON"
                                else:
                                    tag_list[i] = "I-PON"
                        else:
                            ind = 0
                            y = False
                        if y:
                            ind = tag_start_index + len(entities)
                else:
                    pass

            # 二、和上面的一样 重复的
            for com in company_list:
                y = True
                ind = 0
                if com in q_str:
                    while y:
                        tag_start_index = q_str.find(com, ind)
                        if tag_start_index != -1:
                            for i in range(tag_start_index, tag_start_index + len(com)):
                                if tag_start_index == i:
                                    tag_list[i] = "B-COI"
                                else:
                                    tag_list[i] = "I-COI"
                        else:
                            ind = 0
                            y = False
                        if y:
                            ind = tag_start_index + len(com)
                else:
                    pass

            # 三、和上面的一样 重复的
            for cal in Radical_list:
                y = True
                ind = 0
                if cal in q_str:
                    while y:
                        tag_start_index = q_str.find(cal, ind)
                        if tag_start_index != -1:
                            for i in range(tag_start_index, tag_start_index + len(cal)):
                                if tag_start_index == i:
                                    tag_list[i] = "B-ROI"
                                else:
                                    tag_list[i] = "I-ROI"
                        else:
                            ind = 0
                            y = False
                        if y:
                            ind = tag_start_index + len(cal)
                else:
                    pass

            # 字表 标注表 进行对应写入
            seq_result = [str(q) + " " + tag + "\n" for q, tag in zip(q_list, tag_list)]
            with open(output_path, "a", encoding='utf-8') as f:
                f.write(''.join(seq_result))
