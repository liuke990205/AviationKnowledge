from django.shortcuts import render


# 跳转到实体识别页面
def toEntity(request):
    return render(request, 'entity.html')
