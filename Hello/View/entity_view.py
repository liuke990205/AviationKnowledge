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

        tableData = []  # 列表   存格式化后的数据
        searchResult = {}
        searchResult=db.getEntityRelationbyEntity(entity1)
        tableData = Screen(searchResult)
        if (len(searchResult) > 0):
            return render(request, 'entity_search.html',
                          {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'tableData': tableData, 'entity1': entity1})
        ctx = '数据库中暂未添加该实体!!'
        return render(request, 'entity_search.html', {'ctx': ctx})