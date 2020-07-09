from django.contrib import admin
from django.urls import path

from Hello.View import views, annotation_view, answer_view, dataManager_view, entity_view, relation_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    #跳转到主页面
    path('toHome/', home_view.toHome),

    path('register/', views.register),
    path('login/', views.login),

    #跳转到数据管理页面
    path('toDataManager/', dataManager_view.toDataManager),
    #将一条数据插入到neo4j数据库
    path('importNeo4j/', dataManager_view.importNeo4j, name='importNeo4j'),

    path('importNeo4jMuilt/', dataManager_view.importNeo4jMuilt),

    path('deleteNeo4j/', dataManager_view.deleteNeo4j, name='deleteNeo4j'),

    #文本标注文件上传
    path('upload/', dataManager_view.upload),

    path('download/', dataManager_view.download),

    # 跳转到标注页面
    path('toAnnotation/', annotation_view.toAnnotation),
    # 显示待标注文本信息
    path('display_text/', annotation_view.display_text),
    # 自动标注
    path('text_annotation/', annotation_view.text_annotation),

    # 增加一条字典信息
    path('addDictionary/', annotation_view.addDictionary),
    # 删除标注文本信息
    path('deleteTemp/', annotation_view.deleteTemp, name='deleteTemp'),
    # 修改文本信息
    path('modifyTemp/', annotation_view.modifyTemp),
    # 增加一条文本信息
    path('addTemp/', annotation_view.addTemp),


    path('toEntity/', entity_view.toEntity),
    #跳转到关系查询界面
    path('toRelation/', relation_view.toRelation),
    #进行关系查询操作
    path('relation_search/', relation_view.relation_search),
    path('relation_modify/', relation_view.relation_modify),
    path('relation_delete/', relation_view.relation_delete, name='relation_delete'),

    path('toAnswer/', answer_view.toAnswer),

    #跳转到帮助界面
    path('help/', views.help),
    #退出系统
    path('exit/', views.exit),
]
