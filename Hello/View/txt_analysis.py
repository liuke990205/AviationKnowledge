# -*- coding: utf-8 -*-
import csv
'''
python读取文件，将文件中的空白行和数字开头的行去掉
'''
def read_txt(infile, outfile, num):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")

    lines = infopen.readlines()
    for line in lines:
        if line.split():
            #for data in line.split('。'):
                for i in range(9):
                    if line.startswith(str(i)) == True:
                        break
                if i == 8:
                    outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
    if num == 1:
        #调用关键词匹配函数
        keyword_match1(outfile)
    elif num == 2:
        keyword_match2(outfile)
    elif num == 3:
        keyword_match3(outfile)

'''
调用关键词匹配函数
'''
def keyword_match1(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    lines = infopen.readlines()
    relation = ["位于", "使用", "采用", "主要包括"]
    result_list = [["头实体", "关系", "尾实体", "所在文本行"]]
    for line in lines:
        for r in relation:
            start = line.find(r)
            end = line.find("，")
            if start != -1:
                if end == -1:
                    end = line.find("。")
                #头实体 0 ~ caiyong-1
                #尾实体  caiyong+2 ~ 、或。
                if r == "位于":
                    temp_list = [line[0:start], "位置关系", line[start+len(r):end], line]
                    result_list.append(temp_list)
                    print(line[0:start], "位置关系", line[start+len(r):end])
                elif r == "主要包括":
                    list = line[start + len(r):end]
                    #print(line[start + len(r):end], 222)

                    if list.find("、") != -1:
                        for data in list.split("、"):
                            if data[-1] == "等":
                                temp_list = [line[0:start], "组成关系", data[0:-1], line]
                                result_list.append(temp_list)
                                print(line[0:start], "组成关系", data[0:-1])
                            else:
                                temp_list = [line[0:start], "组成关系", data, line]
                                result_list.append(temp_list)
                                print(line[0:start], "组成关系", data)
                elif r == "采用" or r == "使用":
                    temp_list = [line[0:start], "使用关系", line[start+len(r):end], line]
                    result_list.append(temp_list)
                    print(line[0:start], "使用关系", line[start+len(r):end])
        start0 = line.find("，")
        start1 = line.find("由")
        start2 = line.find("组成")
        if start1 != -1 and start2 != -1 and start2 > start1:
            list1 = line[start1+1:start2]
            for data in list1.split("、"):
                temp_list = [line[start0+1:start1], "组成关系", data, line]
                result_list.append(temp_list)
                print(line[start0+1:start1], "组成关系", data)

    for data in result_list:
        print(data)
        with open("C:/Users/26407/Desktop/txt_analysis/txt_export.csv", "a+", newline="") as csvfile:
            write = csv.writer(csvfile)
            write.writerow(data)


def keyword_match2(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    lines = infopen.readlines()
    #result_list = [["头实体", "关系", "尾实体", "所在文本行"]]
    result_list = []
    head_entity = ""
    for line in lines:
        index = line.find("主要包括")
        if index != -1:
            head_entity = line[0:index]
        # !/usr/bin/python
        for i in range(ord("a"), ord("z") + 1):
            if line.startswith(chr(i)) == True:
                temp = line[2:-2]
                if temp.find("，") == -1:
                    temp_list = [head_entity, "组成关系", temp, line]
                    result_list.append(temp_list)
                else:
                    head_entity = temp[0:temp.find("，")]
                    tt = temp[temp.find("，")+3:]
                    while len(tt) != 0:
                        num = tt.find("，")
                        num2 = tt.find("和")
                        if num != -1:
                            tail_entity = tt[0:num]
                            tt = tt[num+1:]
                        elif num2 != -1:
                            tail_entity = tt[0:num2]
                            tt = tt[num2+1:]
                        else:
                            tail_entity = tt[0:]
                            tt = []
                        temp_list = [head_entity, "组成关系", tail_entity, line]
                        result_list.append(temp_list)
    for data in result_list:
        with open("C:/Users/26407/Desktop/txt_analysis/txt_export.csv", "a+", newline="") as csvfile:
            write = csv.writer(csvfile)
            write.writerow(data)


def keyword_match3(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    lines = infopen.readlines()
    #result_list = [["头实体", "关系", "尾实体", "所在文本行"]]
    result_list = []
    for line in lines:
        if line.find("表") == -1:
            data = line.split()
            for i in range(len(data)-1):
                temp_list = [data[i], "组成关系", data[i+1], line]
                #print(data[i], data[i+1])
                result_list.append(temp_list)
    for data in result_list:
        with open("C:/Users/26407/Desktop/txt_analysis/txt_export.csv", "a+", newline="") as csvfile:
            write = csv.writer(csvfile)
            write.writerow(data)

if __name__ == '__main__':
    read_txt("C:/Users/26407/Desktop/txt_analysis/test1.txt", "C:/Users/26407/Desktop/txt_analysis/temp.txt", 1)
    read_txt("C:/Users/26407/Desktop/txt_analysis/test2.txt", "C:/Users/26407/Desktop/txt_analysis/temp.txt", 2)
    read_txt("C:/Users/26407/Desktop/txt_analysis/test3.txt", "C:/Users/26407/Desktop/txt_analysis/temp.txt", 3)