import pymysql
from django.contrib import messages
from django.shortcuts import render, redirect
import xlrd
from Hello.toolkit.pre_load import neo4jconn
from Hello.models import Dictionary

# ��ת��excel����
def toExcel(request):

    return render(request, 'excel.html')

def upload_excel(request):
    if request.method == 'POST':
        # ��ȡ�ļ���
        file = request.FILES.get('file')
        if file:
            # ����������ã���ȡ��excel�е��ֶκ�����
            excel = xlrd.open_workbook(file.name)
            sheet = excel.sheet_by_index(0)
            row_number = sheet.nrows
            column_number = sheet.ncols
            field_list = sheet.row_values(0)
            data_list = []
            for i in range(1, row_number):
                data_list.append(sheet.row_values(i))
            # ����������ã������ֶδ�������������ִ�в������
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                                   database='source')
            cursor = conn.cursor()
            drop_sql = "drop table if exists {}".format('name')
            cursor.execute(drop_sql)
            create_sql = "create table {}(".format('name')
            for field in field_list[:-1]:
                create_sql += "{} varchar(50),".format(field)
            create_sql += "{} varchar(50))".format(field_list[-1])
            cursor.execute(create_sql)
            for data in data_list:
                new_data = ["'{}'".format(i) for i in data]
                insert_sql = "insert into {} values({})".format('name', ','.join(new_data))
                cursor.execute(insert_sql)

            sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'" % ('name')
            count = cursor.execute(sql)
            name_list = list()
            for i in range(count):
                rr = cursor.fetchone()[0]
                if rr not in name_list:
                    name_list.append(rr)
            print(name_list)
            conn.commit()
            conn.close()

            return render(request, 'excel.html', {'name_list': name_list})
    return redirect('/toExcel/')

def excel_extract(request):
    if request.method == 'POST':
        #��ȡ��ǰ��ѡ����ֶ�
        entity_list = request.POST.getlist('select2')
        property_list = request.POST.getlist('select3')

        print(entity_list, property_list)


        entity_sum = len(entity_list)
        print(entity_sum)
        
        #################
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                               database='source')
        cursor = conn.cursor()
        #ƴ��ʵ�����б�
        entity_list_last = ','.join(entity_list)

        # ƴ�������б�
        property_list_last = ','.join(property_list)

        #���ƴ�Ӻ��ʵ�������������б�
        print(entity_list_last, property_list_last)

        # ���ݲ�ѯ������д�Ĳ�ѯ���
        sql = "select %s, %s from name" % (entity_list_last, property_list_last)
        count = cursor.execute(sql)

        # �洢��ѯ��������ֵ�洢��
        dict = {}

        # ѭ���������α�ָ��
        for i in range(count):
            result = cursor.fetchone()
            print(result)
            # ����ѯ���ת�����б�洢
            result = list(result)
            # ��ѯ����ǰ entity_sum ��ֵ��ʵ����
            name = '_'.join(result[0:entity_sum])

            #��ȡʣ���ʵ��������
            property_list_name = result[entity_sum:]

            #���ÿ��ʵ�����Ӻ������
            print(name)

            # ����neo4j���ݿ�
            db = neo4jconn
            # ����ʵ����������neo4j���ݿ��Ƿ��Ѿ�����ʵ��
            result1 = db.findEntity(name)
            if result1:
                pass
            # ���û�д��ڽ�����������
            else:
                # ��ȡ�ֵ��ȫ����Ϣ
                dictionary_entity = Dictionary.objects.all()
                # ʵ������
                type = ""
                for entity in dictionary_entity:
                    if entity.entity == name:
                        type = entity.entity_type
                        break
                # �������ʵ������
                if type:
                    # ����ʵ��ڵ�
                    for i in range(len(property_list)):
                        dict.update({property_list[i]: property_list_name[i]})
                    db = neo4jconn
                    db.createNode(name, type, dict)

        cursor.close()  # �ر��α�
        conn.close()  # �ر�����

    return render(request, 'excel.html')