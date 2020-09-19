# coding=gbk

import xlrd
import csv
from Hello.toolkit.pre_load import neo4jconn

def excel_one_line_to_list():
    file_name = "C:/Users/26407/Desktop/import.xlsx"
    excel = xlrd.open_workbook(file_name)
    sheet = excel.sheet_by_index(0)
    row_number = sheet.nrows
    column_number = sheet.ncols
    field_list = sheet.row_values(1)
    print(field_list)

    for data in field_list:
        if data == "���ϼ�":
            # ���ϼ���������
            faulty_component = field_list.index(data)
        elif data == "רҵ":
            # רҵ��������
            professional = field_list.index(data)
        elif data == "����":
            # ���ŵ�������
            department = field_list.index(data)
        elif data == "����λ��":
            # ����λ�õ�������
            local = field_list.index(data)
        elif data == "��������":
            # ���������������
            failure_phenomenon = field_list.index(data)

        elif data == "����ʱ��":
            # ����ʱ����������
            find_the_opportunity = field_list.index(data)
        elif data == "����ԭ��":
            # ���ŵ�������
            cause_of_failure = field_list.index(data)
        elif data == "�ų�����":
            # �ų�������������
            ruled_out = field_list.index(data)
    data_list = []
    for i in range(2, row_number):
        data_list.append(sheet.row_values(i))
    print(data_list)
    db = neo4jconn

    # �����ս��
    result_list = []
    temp_list = ["ͷʵ��", "ͷʵ������", "βʵ��", "βʵ������", "��ϵ"]
    result_list.append(temp_list)
    for data in data_list:
        # ���м���
        temp_list = [data[faulty_component], "���ϼ�", data[professional], "רҵ", "����רҵ"]
        #д�뵽��ʱ����б�
        result_list.append(temp_list)
        #���ڵ���Ϣд�뵽Neo4j���ݿ�
        db.createNode(data[faulty_component], "���ϼ�", {})
        db.createNode(data[professional], "רҵ", {})
        db.insertExcelRelation(data[faulty_component], data[professional], "����רҵ")


        temp_list = [data[faulty_component], "���ϼ�", data[department], "����", "��������"]
        result_list.append(temp_list)

        db.createNode(data[faulty_component], "���ϼ�", {})
        db.createNode(data[department], "����", {})
        db.insertExcelRelation(data[faulty_component], data[department], "��������")


        temp_list = [data[faulty_component], "���ϼ�", data[local], "����λ��", "����λ��"]
        result_list.append(temp_list)

        db.createNode(data[faulty_component], "���ϼ�", {})
        db.createNode(data[local], "����λ��", {})
        db.insertExcelRelation(data[faulty_component], data[local], "����λ��")


        temp_list = [data[faulty_component], "���ϼ�", data[failure_phenomenon], "��������", "��������"]
        result_list.append(temp_list)


        db.createNode(data[faulty_component], "���ϼ�", {})
        db.createNode(data[failure_phenomenon], "��������", {})
        db.insertExcelRelation(data[faulty_component], data[failure_phenomenon], "��������")


        temp_list = [data[failure_phenomenon], "��������", data[find_the_opportunity], "����ʱ��", "����ʱ��"]
        result_list.append(temp_list)

        db.createNode(data[failure_phenomenon], "��������", {})
        db.createNode(data[find_the_opportunity], "����ʱ��", {})
        db.insertExcelRelation(data[failure_phenomenon], data[find_the_opportunity], "����ʱ��")


        temp_list = [data[failure_phenomenon], "��������", data[cause_of_failure], "����ԭ��", "����ԭ��"]
        result_list.append(temp_list)

        db.createNode(data[failure_phenomenon], "��������", {})
        db.createNode(data[cause_of_failure], "����ԭ��", {})
        db.insertExcelRelation(data[failure_phenomenon], data[cause_of_failure], "����ԭ��")


        temp_list = [data[faulty_component], "���ϼ�", data[ruled_out], "�ų�����", "�ų�����"]
        result_list.append(temp_list)

        db.createNode(data[faulty_component], "���ϼ�", {})
        db.createNode(data[ruled_out], "�ų�����", {})
        db.insertExcelRelation(data[faulty_component], data[ruled_out], "�ų�����")


    print(result_list)
    #���б���Ϣ�洢��Excel��
    for data in result_list:

        with open("C:/Users/26407/Desktop/export.csv", "a", newline="") as csvfile:
            write = csv.writer(csvfile)
            write.writerow(data)

if __name__ == '__main__':
    excel_one_line_to_list()