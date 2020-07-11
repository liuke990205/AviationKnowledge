import csv

from django.contrib import messages
from django.shortcuts import render,redirect
from py2neo import Graph

from Hello.View.relation_view import Screen
from Hello.models import Annotation, User, Temp
from Hello.toolkit.pre_load import neo4jconn


# 跳转到数据管理页面
def toDataManager(request):
    # 获取当前用户的ID
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.user_id

    # 根据当前用户 查询所有的关系数据
    tempList = Temp.objects.filter(user_id=user_id)

    return render(request, 'data_manager.html', {'tempList': tempList})


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

    #查询出来头实体和尾实体是否已经存在
    result1 = db.findEntity(relation.headEntity)
    result2 = db.findEntity(relation.tailEntity)
    if result1 and result2:
        #判断是否存在关系
        if(db.findRelationByEntities(relation.headEntity,relation.tailEntity)):#如果存在关系，更新关系
            db.modifyRelation(relation.headEntity,relation.tailEntity,relation.relationshipCategory,id)
        else:#如果两个实体不存在关系，则直接创建关系
            db.insertRelation(relation.headEntity, relation.relationshipCategory, relation.tailEntity, id)
        temp = Temp.objects.get(temp_id=id)
        temp.delete()
        return redirect('/toDataManager/')
    elif result1:
        #创建尾实体
        db.createNode(relation.tailEntity, relation.tailEntityType)
        #插入一条neo4j数据库信息
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
        #return render(request, 'data_manager.html', {'tempList': list})
        return redirect("/toDataManager/")



#批量导入Neo4j数据库
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

def download(request):
    db = neo4jconn
    searchResult = {}
    tableData = []
    searchResult = db.findAll()
    tableData = Screen(searchResult)
    print(tableData)
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
