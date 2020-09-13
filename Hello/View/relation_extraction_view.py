import csv
import os
import re

import jieba
from django.contrib import messages
from django.shortcuts import render, redirect

from Hello.models import Relation, Rel


# 跳转到关系抽取页面
def toRelation(request):
    return render(request, 'relation_extract.html')


def upload3(request):
    if request.method == 'POST':
        # 获取文件名
        file = request.FILES.get('file')
        if file:
            new_data = []
            # 读取文件内容，并且插入到数据库中
            with open(file.name, "r", encoding="utf-8") as lines:
                dataList = lines.readlines()
                print(dataList)
                for data in dataList:
                    data = data.strip('\n')
                    new_data.append(data)
            messages.success(request, "上传成功！")

            request.session['new_data'] = new_data
            a = []
            for data in new_data:
                a.append(data)
            str = ""

            str=''.join(a)
            return render(request, 'relation_extract.html', {'str': str})
        else:
            messages.success(request, "文件为空！")
            return redirect('/toRelation/')


# 读取待识别文本并转化成所要形式
def re_text(request):
    if request.POST:
        text = request.POST['user_text']
        # 获取输入文本
        sen_list = []

        relation_list = []

        result = re.split(r'[。\n]', text)
        if "\n" in result:
            result.remove("\n")
        for i in range(len(result)):
            sen = str((result[i]).replace('\n', '').replace('\r', '') + "。\n")
            sen_list.append(sen)

        dic_dir = "C:/Users/26407/Desktop/HelloWorld/hello/toolkit/dic.txt"
        temp_file_dir = "C:/Users/26407/Desktop/HelloWorld/hello/toolkit/rel_data.csv"

        jieba.load_userdict(dic_dir)

        f = open(temp_file_dir, 'w')
        f.truncate()

        relList = Rel.objects.filter(re_flag=0)
        for rel in relList:
            rel.delete()

        f1 = open(dic_dir, 'r', encoding='utf-8')
        f2 = open(temp_file_dir, 'a')

        dic_entity = []
        dic_entity_type_ori = []
        dic_entity_type = []
        sen_entity = []
        entity_type = []

        for w in f1.readlines():  # 读取词典中的实体
            w_array = w.split(" ")
            dic_entity.append(w_array[0])
            dic_entity_type_ori.append(w_array[2].replace("\n", ""))
        # print(dic_entity)

        for type in dic_entity_type_ori:
            if type == "hkq":
                dic_entity_type.append("航空器")
                continue
            if type == "wq":
                dic_entity_type.append("武器")
                continue
            if type == "sxmx":
                dic_entity_type.append("数学模型")
                continue
            if type == "ckwd":
                dic_entity_type.append("参考文档")
                continue
            if type == "xt":
                dic_entity_type.append("系统")
                continue
            if type == "xnzb":
                dic_entity_type.append("性能指标")
                continue
            if type == "csz":
                dic_entity_type.append("参数值")
                continue

        for i in range(len(sen_list)):

            seg1 = jieba.cut(sen_list[i])
            seg2 = "/".join(seg1)
            seg_list = seg2.split("/")  # 分词

            for j in range(len(seg_list)):
                for k in range(len(dic_entity)):
                    if seg_list[j] == dic_entity[k]:
                        # print(seg_list[j])
                        sen_entity.append(dic_entity[k])
                        entity_type.append(dic_entity_type[k].replace("\n", ""))  # 去除迷之换行

            if len(sen_entity) == 2 and sen_entity[0] != sen_entity[1]:
                flag = relation_schema(entity_type[0], entity_type[1])  # 利用schema提供约束
                if (flag == 1):
                    sentence = sen_list[i].replace("\n", "")
                    s = str(sentence) + "," + str(sen_entity[0]) + "," + str(entity_type[0]) + "," + str(
                        sen_entity[1]) + "," + str(entity_type[1]) + "\n"  #
                    f2.write(s)
                    relation_list.append([str(sentence), str(sen_entity[0]), str(entity_type[0]), str(sen_entity[1]),
                                          str(entity_type[1])])
                    print(relation_list)

                if (flag == 2):
                    sentence = sen_list[i].replace("\n", "")
                    entity_type[0], entity_type[1] = entity_type[1], entity_type[0]
                    relation_list.append([str(sentence), str(sen_entity[0]), str(entity_type[1]), str(sen_entity[1]),
                                          str(entity_type[0])])
                    print(relation_list)
                    s = str(sentence) + "," + str(sen_entity[0]) + "," + str(entity_type[1]) + "," + str(
                        sen_entity[1]) + "," + str(entity_type[0]) + "\n"  #
                    f2.write(s)

            if len(sen_entity) > 2:
                for j in range(len(sen_entity)):
                    for k in range(len(sen_entity) - j - 1):  # 每个实体及其后的单词两两配对
                        if sen_entity[j] != sen_entity[j + k + 1]:
                            flag = relation_schema(entity_type[j], entity_type[k + j + 1])  # 利用schema提供约束
                            # print(flag)
                            if (flag == 1):
                                sentence = sen_list[i].replace("\n", "")
                                relation_list.append(
                                    [str(sentence), str(sen_entity[j]), str(entity_type[j]), str(sen_entity[j + k + 1]),
                                     str(entity_type[j + k + 1])])
                                print(relation_list)
                                s = str(sentence) + "," + str(sen_entity[j]) + "," + str(entity_type[j]) + "," + str(
                                    sen_entity[j + k + 1]) + "," + str(entity_type[j + k + 1]) + "\n"  #
                                f2.write(s)
                            if (flag == 2):
                                sentence = sen_list[i].replace("\n", "")
                                relation_list.append(
                                    [str(sentence), str(sen_entity[j + k + 1]), str(entity_type[k + j + 1]),
                                     str(sen_entity[j]),
                                     str(entity_type[j])])
                                print(relation_list)
                                s = str(sentence) + "," + str(sen_entity[j + k + 1]) + "," + str(
                                    entity_type[k + j + 1]) + "," + str(
                                    sen_entity[j]) + "," + str(entity_type[j]) + "\n"  # 调换一下
                                f2.write(s)
            sen_entity = []
            entity_type = []
        f2.close()
        os.system("python C:/Users/26407/Desktop/HelloWorld/hello/toolkit/deepke/predict1.py")

        textfile = open(temp_file_dir, 'r')

        reader = csv.reader(textfile)
        for rel in reader:
            if len(rel) == 6:
                text = rel[0]
                headEntity = rel[1]
                headEntityType = rel[2]
                tailEntity = rel[3]
                tailEntityType = rel[4]
                relationshipCategory = rel[5]
                rel = Rel(headEntity=headEntity, headEntityType=headEntityType, tailEntity=tailEntity,
                          tailEntityType=tailEntityType, relationshipCategory=relationshipCategory, text=text,
                          re_flag=0)
                rel.save()

    resultList = Rel.objects.filter(re_flag=0)

    return render(request, 'relation_extract.html', {'resultList': resultList})


def relation_schema(type1, type2):
    schema_type1 = Relation.objects.values_list("head_entity", flat=True)
    schema_type2 = Relation.objects.values_list("tail_entity", flat=True)
    #print(schema_type1)

    for i in range(len(schema_type1)):
        if type1 == schema_type1[i] and type2 == schema_type2[i]:
            return 1

    for i in range(len(schema_type1)):
        if type2 == schema_type1[i] and type1 == schema_type2[i]:
            return 2

    return 0


# 删除选中的Rel
def deleteRel(request):
    # 获取前端传过来的rel_id
    id = request.GET.get('rel_id')
    # 删除rel_id
    rel = Rel.objects.get(rel_id=id)
    rel.delete()
    resultList = Rel.objects.filter(re_flag=0)
    return render(request, 'relation_extract.html', {'resultList': resultList})


# 修改Rel信息
def modifyRel(request):
    rel_id = request.POST.get('rel_id')
    new_headEntity = request.POST.get('headEntity')
    new_headEntityType = request.POST.get('headEntityType')
    new_tailEntity = request.POST.get('tailEntity')
    new_tailEntityType = request.POST.get('tailEntityType')
    new_relationshipCategory = request.POST.get('relationshipCategory')

    # 获取前端传过来的信息
    rel = Rel.objects.get(rel_id=rel_id)
    rel.headEntity = new_headEntity
    rel.headEntityType = new_headEntityType
    rel.tailEntity = new_tailEntity
    rel.tailEntityType = new_tailEntityType
    rel.relationshipCategory = new_relationshipCategory
    rel.save()

    # 获取修改之后的Rel
    resultList = Rel.objects.filter(re_flag=0)
    return render(request, 'relation_extract.html', {'resultList': resultList})


def saveRel(request):
    relList = Rel.objects.filter(re_flag=0)
    print(relList)
    for rel in relList:
        print(rel)
        rel.re_flag = 1
        rel.save()

    return render(request, 'relation_extract.html')
