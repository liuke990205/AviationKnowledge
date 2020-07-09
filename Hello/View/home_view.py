from django.shortcuts import render

from Hello.toolkit.pre_load import neo4jconn
import json

# 跳转到主页面
def toHome(request):
    db = neo4jconn
    searchResult={}
    searchResult=db.findAll()
    searchEntity=db.findAllEntity()
    print(len(searchEntity))
    print(len(searchResult))
    return render(request, 'home.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False), 'relation_amount':len(searchResult), 'entity_amount':len(searchEntity)})