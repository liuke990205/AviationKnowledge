import csv

import pymysql
from django.contrib import messages
from django.shortcuts import render, redirect

from Hello.View.relation_view import Screen
from Hello.models import Annotation, User, Temp, Dictionary, Relation
from Hello.toolkit.pre_load import neo4jconn


# 跳转到数据管理页面
def toDataManager(request):
    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects. \
        get(username=username)
    user_id = user.user_id

    # 根据当前用户 查询所有的关系数据
    tempList = Temp.objects.filter(user_id=user_id)

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()
    count = cursor.execute("show tables")
    tableList = list()
    for i in range(count):
        result = cursor.fetchone()
        tableList.append(result[0])
    #print(tableList)
    return render(request, 'data_manager.html', {'tempList': tempList, 'tableList': tableList})

#从前端获取到表名
def getTable(request):
    # 获取表名
    table = request.POST['databaseTable']

    #将数据库表名存入session
    request.session['table'] = table

    #连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()

    #获取本张表的所有字段
    sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'" % (table)
    count = cursor.execute(sql)
    aList = set()
    for i in range(count):
        aList.add(cursor.fetchone()[0])


    count = cursor.execute("show tables")
    tableList = list()
    for i in range(count):
        result = cursor.fetchone()
        tableList.append(result[0])
    #print(tableList)


    sql = "select TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where CONSTRAINT_SCHEMA ='source' AND REFERENCED_TABLE_NAME = '%s';" % (table)
    count = (cursor.execute(sql))
    bList = set()
    primary2 = []
    if count > 0:
        re = cursor.fetchone()

        request.session['table2'] = re[0]
        request.session['re_name'] = re[1]

        sql2 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'" % (re[0])
        count = cursor.execute(sql2)

        for i in range(count):
            bList.add(cursor.fetchone()[0])
        sql3 = "SELECT  COLUMN_NAME FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE` WHERE table_name='%s' AND constraint_name='PRIMARY'" % (
            re[0])
        count = cursor.execute(sql3)
        primary2 = cursor.fetchone()[0]
        print(primary2, '999')

    sql4 = "SELECT  COLUMN_NAME FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE` WHERE table_name='%s' AND constraint_name='PRIMARY'" % (table)
    count = cursor.execute(sql4)
    primary = cursor.fetchone()
    print(primary[0], '00')




    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接

    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.user_id

    # 根据当前用户 查询所有的关系数据
    tempList = Temp.objects.filter(user_id=user_id)


    return render(request, 'data_manager.html', {'tempList': tempList, 'tableList': tableList, 'aList': aList, 'table': table, 'bList': bList, 'primary': primary[0], 'primary2': primary2})


# 从关系数据库中抽取知识
def d2neo4j(request):

    table = request.session.get('table')
    entity_name = request.POST.get('entity_name')
    entity_property = request.POST.getlist('entity_property')
    insertNode(table, entity_name, entity_property)

    entity_name2 = request.POST.get('entity_name2')
    entity_property2 = request.POST.getlist('entity_property2')
    if entity_name2:
        table2 = request.session.get('table2')
        insertNode(table2, entity_name2, entity_property2)

        re_name = request.session.get('re_name')
        insertKnow(table2, entity_name2, re_name)

    messages.success(request, "知识抽取成功！")
    return redirect('/toDataManager/')

def insertKnow(table2, entity_name2, re_name):
    global sum
    sum = 300
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()
    sql = "select %s, %s from %s" % (entity_name2, re_name, table2)

    count = cursor.execute(sql)
    for i in range(count):
        result = cursor.fetchone()
        # 获取到头实体和尾实体的类型
        headEntityType = Dictionary.objects.get(entity=result[0]).entity_type
        tailEntityType = Dictionary.objects.get(entity=result[1]).entity_type
        # 根据头实体和尾实体来查询之间的关系
        relation = Relation.objects.get(head_entity=headEntityType, tail_entity=tailEntityType)
        db = neo4jconn
        sum+=1
        db.insertRelation(result[0], relation.relation, result[1], str(sum))


def insertNode(table, entity_name, entity_property):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()

    str=','.join(entity_property)
    #print(str)

    sql = "select %s, %s from %s" % (entity_name, str, table)
    print(sql)
    count = cursor.execute(sql)

    dict={}
    for i in range(count):
        result = cursor.fetchone()
        print(result)
        result = list(result)
        name = result[0]
        # 获取字典的全部信息
        dictionary_entity = Dictionary.objects.all()
        # 实体类型
        type = ""
        for entity in dictionary_entity:
            if entity.entity == name:
                type = entity.entity_type
                break
        #print(type)

        if type:
            # 生成实体节点（是否插入属性）
            result.remove(name)
            for i in range(len(entity_property)):
                dict.update({entity_property[i]: result[i]})
            db = neo4jconn
            db.createNode(name, type, dict)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


# 将一条数据插入到Neo4j数据库
def importNeo4j(request):
    # 获取temp_id
    id = request.GET.get('temp_id')
    relation = Temp.objects.get(temp_id=id)
    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.user_id
    # 连接数据库
    db = neo4jconn

    # 查询出来头实体和尾实体是否已经存在
    result1 = db.findEntity(relation.headEntity)
    result2 = db.findEntity(relation.tailEntity)
    if result1 and result2:
        # 判断是否存在关系
        if (db.findRelationByEntities(relation.headEntity, relation.tailEntity)):  # 如果存在关系，更新关系
            db.modifyRelation(relation.headEntity, relation.tailEntity, relation.relationshipCategory, id)
        else:  # 如果两个实体不存在关系，则直接创建关系
            db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
        temp = Temp.objects.get(temp_id=id)
        temp.delete()
        return redirect('/toDataManager/')
    elif result1:
        # 创建尾实体
        db.createNode(relation.tailEntity, relation.tailEntityType)
        # 插入一条neo4j数据库信息
        db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
        temp = Temp.objects.get(temp_id=id)
        temp.delete()
        tempList = Temp.objects.filter(user_id=user_id)
        return redirect('/toDataManager/')
    elif result2:
        # 创建头实体
        db.createNode(relation.headEntity, relation.headEntityType)
        # 插入一条neo4j数据库信息
        db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
        temp = Temp.objects.get(temp_id=id)
        temp.delete()
        tempList = Temp.objects.filter(user_id=user_id)
        return redirect('/toDataManager/')
    else:
        # 创建头实体
        db.createNode(relation.headEntity, relation.headEntityType)
        # 创建尾实体
        db.createNode(relation.tailEntity, relation.tailEntityType)
        # 插入一条neo4j数据库信息
        db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
        temp = Temp.objects.get(temp_id=id)
        temp.delete()
        tempList = Temp.objects.filter(user_id=user_id)
        # return render(request, 'data_manager.html', {'tempList': list})
        return redirect("/toDataManager/")


# 批量导入Neo4j数据库
def importNeo4jMuilt(request):
    boxList = request.POST.getlist('boxList')
    # 连接数据库
    db = neo4jconn
    if boxList:
        for temp_id in boxList:
            relation = Temp.objects.get(temp_id=temp_id)
            # 查询出来头实体和尾实体是否已经存在
            result1 = db.findEntity(relation.headEntity)
            result2 = db.findEntity(relation.tailEntity)
            if result1 and result2:
                # 判断是否存在关系
                if (db.findRelationByEntities(relation.headEntity, relation.tailEntity)):  # 如果存在关系，更新关系
                    db.modifyRelation(relation.headEntity, relation.tailEntity, relation.relationshipCategory, temp_id)
                else:  # 如果两个实体不存在关系，则直接创建关系
                    db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, temp_id)
                temp = Temp.objects.get(temp_id=temp_id)
                temp.delete()
            elif result1:
                # 创建尾实体
                db.createNode(relation.tailEntity, relation.tailEntityType)
                # 插入一条neo4j数据库信息
                db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, temp_id)
                temp = Temp.objects.get(temp_id=temp_id)
                temp.delete()
            elif result2:
                # 创建头实体
                db.createNode(relation.headEntity, relation.headEntityType)
                # 插入一条neo4j数据库信息
                db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
                temp = Temp.objects.get(temp_id=id)
                temp.delete()
            else:
                # 创建头实体
                db.createNode(relation.headEntity, relation.headEntityType)
                # 创建尾实体
                db.createNode(relation.tailEntity, relation.tailEntityType)
                # 插入一条neo4j数据库信息
                db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
                temp = Temp.objects.get(temp_id=id)
                temp.delete()
    else:
        messages.success(request, "未选中任何数据！")
    return redirect('/toDataManager/')


# 删除一条Neo4j数据
def deleteNeo4j(request):
    # 获取前端传过来的temp_id
    id = request.GET.get('temp_id')

    # 删除temp_id
    temp = Temp.objects.get(temp_id=id)
    temp.delete()

    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.user_id

    # 获取删除之后的Temp
    tempList = Temp.objects.filter(user_id=user_id)
    return redirect('/toDataManager/')


# 删除所有数据
def deleteAllNeo4j(request):
    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.user_id

    # 删除temp_id
    temp = Temp.objects.filter(user_id=user_id)
    temp.delete()

    # 获取删除之后的Temp
    tempList = Temp.objects.filter(user_id=user_id)
    return redirect('/toDataManager/')


# 上传文件，并且将数据保存到数据库中
def upload(request):
    if request.method == 'POST':
        # 获取文件名
        file = request.FILES.get('file')
        if file:
            # 获取当前用户的id
            username = request.session.get('username')
            user = User.objects.get(username=username)
            user_id = user.user_id
            # 读取文件内容，并且插入到数据库中
            with open(file.name, "r", encoding="utf-8") as lines:
                data = lines.readlines()
                for i in data:
                    i = i.strip('\n')
                    q = Annotation(content=i, file_name=file, flag=False, user_id_id=user_id)  # 将数据插入到数据库中
                    q.save()
            messages.success(request, "上传成功！")
            return redirect('/toDataManager/')
        else:
            messages.success(request, "文件为空！")
            return redirect('/toDataManager/')


# 导出Neo4J数据库
def download(request):
    db = neo4jconn
    searchResult = {}
    tableData = []
    searchResult = db.findAll()
    tableData = Screen(searchResult)
    if tableData:
        for data in tableData:
            with open("exload_all_relation.csv", "a", newline="") as csvfile:
                write = csv.writer(csvfile)
                write.writerow(data)
        messages.success(request, "下载成功！")
        return redirect('/toDataManager/')
    else:
        messages.success(request, "Neo4j数据库为空！")
        return redirect('/toDataManager/')
