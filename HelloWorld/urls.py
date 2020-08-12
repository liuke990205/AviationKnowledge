from django.contrib import admin
from django.urls import path

from Hello.View import views, annotation_view, answer_view, dataManager_view, entity_view, relation_view, home_view, d2rq_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    #跳转到主页面
    path('toHome/', home_view.toHome),
    #用户注册
    path('register/', views.register),
    #用户登录
    path('login/', views.login),

    #跳转到数据管理页面
    path('toDataManager/', dataManager_view.toDataManager),

    #跳转到D2rq界面
    path('toD2rq/', d2rq_view.toD2rq),

    #选择数据库管理系统名
    path('commitDatabase/', d2rq_view.commitDatabase),
    #提交数据库连接配置
    path('commitConfiguration/', d2rq_view.commitConfiguration),

    #获取选中的表名
    path('getTable/', d2rq_view.getTable),
    ##从关系数据库中抽取知识
    path('d2neo4j/', d2rq_view.d2neo4j),

    #将一条数据插入到neo4j数据库
    path('importNeo4j/', dataManager_view.importNeo4j, name='importNeo4j'),
    #批量导入
    path('importNeo4jMuilt/', dataManager_view.importNeo4jMuilt),
    #删除
    path('deleteNeo4j/', dataManager_view.deleteNeo4j, name='deleteNeo4j'),
    #删除所有
    path('deleteAllNeo4j/', dataManager_view.deleteAllNeo4j, name='deleteAllNeo4j'),



    #导出Neo4j数据库
    path('download/', dataManager_view.download),

    # 跳转到标注页面
    path('toAnnotation/', annotation_view.toAnnotation),
    #文本标注文件上传
    path('upload/', annotation_view.upload),
    # 显示待标注文本信息
    path('display_text/', annotation_view.display_text),
    # 自动标注
    path('text_annotation/', annotation_view.text_annotation),

    # 增加一条字典信息
    path('addDictionary/', annotation_view.addDictionary),
    #删除一条字典信息
    path('deleteDictionary/', annotation_view.deleteDictionary, name='deleteDictionary'),
    #修改一条字典信息
    path('modifyDictionary/', annotation_view.modifyDictionary),

    # 删除标注文本信息
    path('deleteTemp/', annotation_view.deleteTemp, name='deleteTemp'),
    # 修改文本信息
    path('modifyTemp/', annotation_view.modifyTemp),
    # 增加一条文本信息
    path('addTemp/', annotation_view.addTemp),

    #跳转到实体识别页面
    path('toEntityRecognition/', entity_view.toEntityRecognition),

    path('upload2/', entity_view.upload2),

    path('display_result/', entity_view.display_result),

    #跳转到实体查询页面
    path('toEntitySearch/', entity_view.toEntitySearch),
    #进行实体查询操作
    path('entity_search/', entity_view.entity_search),
    #进行实体修改操作
    path('entity_modify/', entity_view.entity_modify),
    #进行实体删除操作
    path('entity_delete/', entity_view.entity_delete, name='entity_delete'),

    #跳转到关系抽取页面
    path('toRelationeExtract/', relation_view.toRelationeExtract),

    #跳转到关系查询界面
    path('toRelationSearch/', relation_view.toRelationSearch),
    #进行关系查询操作
    path('relation_search/', relation_view.relation_search),
    #进行关系修改操作
    path('relation_modify/', relation_view.relation_modify),
    #进行关系删除操作
    path('relation_delete/', relation_view.relation_delete, name='relation_delete'),

    #跳转到问答系统界面
    path('toAnswer/', answer_view.toAnswer),

    #跳转到帮助界面
    path('help/', views.help),
    #退出系统
    path('exit/', views.exit),
]
