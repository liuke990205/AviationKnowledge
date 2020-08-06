import pymysql
from django.contrib import messages
from django.shortcuts import render, redirect

from Hello.View.relation_view import Screen
from Hello.models import Annotation, User, Temp, Dictionary, Relation
from Hello.toolkit.pre_load import neo4jconn

from Hello.View.dataManager_view import insertNode

def toD2rq(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()
    count = cursor.execute("show tables")
    tableList = list()
    for i in range(count):
        result = cursor.fetchone()
        tableList.append(result[0])

    return render(request, 'd2rq.html', {"tableList": tableList})



#��ǰ�˻�ȡ������
def getTable(request):
    # ��ȡ����
    table = request.POST['databaseTable']

    #�����ݿ��������session
    request.session['table'] = table

    #�������ݿ�
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()

    #��ȡ���ű�������ֶ�
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




    cursor.close()  # �ر��α�
    conn.close()  # �ر�����



    return render(request, 'd2rq.html', {'tableList': tableList, 'aList': aList, 'table': table, 'bList': bList, 'primary': primary[0], 'primary2': primary2})


# �ӹ�ϵ���ݿ��г�ȡ֪ʶ
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

    messages.success(request, "success!!")
    return redirect('/toD2rq/')

def insertKnow(table2, entity_name2, re_name):
    global sum
    sum = 300
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='source')
    cursor = conn.cursor()
    sql = "select %s, %s from %s" % (entity_name2, re_name, table2)

    count = cursor.execute(sql)
    for i in range(count):
        result = cursor.fetchone()
        # ��ȡ��ͷʵ���βʵ�������
        headEntityType = Dictionary.objects.get(entity=result[0]).entity_type
        tailEntityType = Dictionary.objects.get(entity=result[1]).entity_type
        # ����ͷʵ���βʵ������ѯ֮��Ĺ�ϵ
        relation = Relation.objects.get(head_entity=headEntityType, tail_entity=tailEntityType)
        db = neo4jconn
        sum+=1
        db.insertRelation(result[0], relation.relation, result[1], str(sum))