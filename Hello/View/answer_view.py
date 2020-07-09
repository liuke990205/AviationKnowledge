from django.shortcuts import render


# 跳转到问答系统页面
def toAnswer(request):
    return render(request, 'answer.html')
