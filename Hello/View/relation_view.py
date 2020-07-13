import json

from django.shortcuts import render

from Hello.toolkit.pre_load import neo4jconn

# 跳转到关系抽取页面
def toRelationeExtract(request):
    return render(request, 'relation_extract.html')

# 跳转到关系查询页面
def toRelationSearch(request):
    return render(request, 'relation_search.html')

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

def relation_search(request):
    ctx = {}
    if request.method == 'POST':
        entity1 = request.POST['entity1_text']
        relation = request.POST['relation_text']
        entity2 = request.POST['entity2_text']

        request.session['entity1'] = entity1
        request.session['relation'] = relation
        request.session['entity2'] = entity2


        db = neo4jconn

        tableData = []  # 列表   存格式化后的数据
        searchResult = {}
        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findRelationByEntity1(entity1)

        # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
        if (len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0):
            searchResult = db.findRelationByEntity2(entity2)

        # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0):
            searchResult = db.findOtherEntities(entity1, relation)

        # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
        if (len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0):
            searchResult = db.findOtherEntities2(entity2, relation)

        # 若输入entity1和entity2,则输出entity1和entity2之间的关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0):
            searchResult = db.findRelationByEntities(entity1, entity2)

        # 若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
        if (len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0):
            searchResult = db.findEntityRelation(entity1, relation, entity2)

        # 全为空
        if (len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findAll()

        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1, 'entity2': entity2, 'relation': relation})
        ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
        return render(request, 'relation_search.html', {'ctx': ctx})

    return render(request, 'relation_search.html', {'ctx': ctx})


def relation_modify(request):
    if request.method == 'POST':
        entity1 = request.POST['headEntity']
        entity2 = request.POST['tailEntity']
        relation = request.POST['relationshipCategory']
        temp_id = request.POST['temp_id']
        print(temp_id, entity1, entity2, relation)
        # 连接neo4j数据库
        db = neo4jconn
        db.modifyRelation(entity1, entity2, relation, temp_id)

        entity1 = request.session.get('entity1')
        relation = request.session.get('relation')
        entity2 = request.session.get('entity2')

        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findRelationByEntity1(entity1)
            print(searchResult)
            tableData = Screen(searchResult)  # 对结果集进行格式化

            if (len(tableData) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1})

        # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
        if (len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0):
            searchResult = db.findRelationByEntity2(entity2)
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity2': entity2})

        # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0):
            searchResult = db.findOtherEntities(entity1, relation)
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1, 'relation': relation})

        # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
        if (len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0):
            searchResult = db.findOtherEntities2(entity2, relation)
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity2': entity2, 'relation': relation})

        # 若输入entity1和entity2,则输出entity1和entity2之间的关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0):
            searchResult = db.findRelationByEntities(entity1, entity2)
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1, 'entity2': entity2})

        # 若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
        if (len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0):
            searchResult = db.findEntityRelation(entity1, relation, entity2)
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 全为空
        if (len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findAll()
            tableData = Screen(searchResult)
            if (len(searchResult) > 0):
                return render(request, 'relation_search.html',
                              {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                               'entity1': entity1, 'entity2': entity2, 'relation': relation})
        ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
        return render(request, 'relation_search.html', {'ctx': ctx})


def relation_delete(request):
    temp_id = request.GET.get('temp_id')
    print(temp_id)
    db = neo4jconn
    db.deleteRelation(temp_id)

    entity1 = request.session.get('entity1')
    relation = request.session.get('relation')
    entity2 = request.session.get('entity2')
    # print(entity1, relation, entity2)
    # 若只输入entity1,则输出与entity1有直接关系的实体和关系
    if (len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0):
        searchResult = db.findRelationByEntity1(entity1)
        print(searchResult)
        tableData = Screen(searchResult)  # 对结果集进行格式化

        if (len(tableData) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1})

    # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
    if (len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0):
        searchResult = db.findRelationByEntity2(entity2)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity2': entity2})

    # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
    if (len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0):
        searchResult = db.findOtherEntities(entity1, relation)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1, 'relation': relation})

    # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
    if (len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0):
        searchResult = db.findOtherEntities2(entity2, relation)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity2': entity2, 'relation': relation})

    # 若输入entity1和entity2,则输出entity1和entity2之间的关系
    if (len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0):
        searchResult = db.findRelationByEntities(entity1, entity2)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1, 'entity2': entity2})

    # 若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
    if (len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0):
        searchResult = db.findEntityRelation(entity1, relation, entity2)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1, 'entity2': entity2, 'relation': relation})

    # 全为空
    if (len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0):
        searchResult = db.findAll()
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'relation_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData,
                           'entity1': entity1, 'entity2': entity2, 'relation': relation})
    ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
    return render(request, 'relation_search.html', {'ctx': ctx})