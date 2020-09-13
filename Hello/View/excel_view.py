import pymysql
from django.contrib import messages
from django.shortcuts import render, redirect
import xlrd
from Hello.toolkit.pre_load import neo4jconn
from Hello.models import Dictionary

# 跳转到excel界面
def toExcel(request):

    return render(request, 'excel.html')

def upload_excel(request):
    if request.method == 'POST':
        # 获取文件名
        file = request.FILES.get('file')
        if file:
            # 下面代码作用：获取到excel中的字段和数据
            excel = xlrd.open_workbook(file.name)
            sheet = excel.sheet_by_index(0)
            row_number = sheet.nrows
            column_number = sheet.ncols
            field_list = sheet.row_values(0)
            data_list = []
            for i in range(1, row_number):
                data_list.append(sheet.row_values(i))
            # 下面代码作用：根据字段创建表，根据数据执行插入语句
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
        #获取到前端选择的字段
        entity_list = request.POST.getlist('select2')
        property_list = request.POST.getlist('select3')

        print(entity_list, property_list)


        entity_sum = len(entity_list)
        print(entity_sum)
        
        #################
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                               database='source')
        cursor = conn.cursor()
        #拼接实体名列表
        entity_list_last = ','.join(entity_list)

        # 拼接属性列表
        property_list_last = ','.join(property_list)

        #输出拼接后的实体名和属性名列表
        print(entity_list_last, property_list_last)

        # 根据查询条件编写的查询语句
        sql = "select %s, %s from name" % (entity_list_last, property_list_last)
        count = cursor.execute(sql)

        # 存储查询结果集（字典存储）
        dict = {}

        # 循环来遍历游标指针
        for i in range(count):
            result = cursor.fetchone()
            print(result)
            # 将查询结果转换成列表存储
            result = list(result)
            # 查询到的前 entity_sum 个值是实体名
            name = '_'.join(result[0:entity_sum])

            #获取剩余的实体属性名
            property_list_name = result[entity_sum:]

            #输出每个实体连接后的名字
            print(name)

            # 连接neo4j数据库
            db = neo4jconn
            # 根据实体名来查找neo4j数据库是否已经存在实体
            result1 = db.findEntity(name)
            if result1:
                pass
            # 如果没有存在进行下述操作
            else:
                # 获取字典的全部信息
                dictionary_entity = Dictionary.objects.all()
                # 实体类型
                type = ""
                for entity in dictionary_entity:
                    if entity.entity == name:
                        type = entity.entity_type
                        break
                # 如果存在实体类型
                if type:
                    # 生成实体节点
                    for i in range(len(property_list)):
                        dict.update({property_list[i]: property_list_name[i]})
                    db = neo4jconn
                    db.createNode(name, type, dict)

        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接

    return render(request, 'excel.html')