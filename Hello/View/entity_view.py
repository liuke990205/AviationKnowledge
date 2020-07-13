from django.shortcuts import render
from Hello.toolkit.pre_load import neo4jconn

import json

def Screen(searchResult):
    tableData = []
    for i in range(0, len(searchResult)):
        relationData = []
        relationData.append(searchResult[i]['n1']['name'])
        relationData.append(searchResult[i]['rel']['type'])
        relationData.append(searchResult[i]['n2']['name'])
        relationData.append(int(searchResult[i]['rel']['id']))
        tableData.append(relationData)
    print(tableData)
    return tableData

# 跳转到实体识别页面
def toEntity(request):
    return render(request, 'entity.html')

#跳转到实体查询页面
def toEntitySearch(request):
    return render(request, 'entity_search.html')


#实体查询
def entity_search(request):
    if request.method == 'POST':
        entity1 = request.POST['entity1_text']
        db = neo4jconn

        request.session['entity'] = entity1

        tableData = []  # 列表   存格式化后的数据
        searchResult = {}
        searchResult=db.getEntityRelationbyEntity(entity1)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'entity_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData, 'entity1': entity1})
        ctx = '数据库中暂未添加该实体!!'
        return render(request, 'entity_search.html', {'ctx': ctx})

#实体修改
def entity_modify(request):
    if request.method == 'POST':
        entity1 = request.POST['headEntity1']
        entity2 = request.POST['tailEntity1']
        relation = request.POST['relationshipCategory1']
        temp_id = request.POST['temp_id1']
        # 连接neo4j数据库
        db = neo4jconn
        db.modifyRelation(entity1, entity2, relation, temp_id)

        entity1 = request.session.get('entity')

        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0):
            searchResult = db.getEntityRelationbyEntity(entity1)
            tableData = Screen(searchResult)  # 对结果集进行格式化

            if (len(tableData) > 0):
                return render(request, 'entity_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1})

        ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
        return render(request, 'entity_search.html', {'ctx': ctx})

#实体删除
def entity_delete(request):
    temp_id = request.GET.get('temp_id')
    print(temp_id)
    db = neo4jconn
    db.deleteRelation(temp_id)

    entity1 = request.session.get('entity')

    # print(entity1, relation, entity2)
    # 若只输入entity1,则输出与entity1有直接关系的实体和关系
    if (len(entity1) != 0 ):
        searchResult = db.getEntityRelationbyEntity(entity1)
        print(searchResult)
        tableData = Screen(searchResult)  # 对结果集进行格式化

        if (len(tableData) > 0):
            return render(request, 'entity_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1})
    ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
    return render(request, 'entity_search.html', {'ctx': ctx})