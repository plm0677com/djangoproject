from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 视图是接收对象并返回对象的 Python 函数。接收‘请求’作为参数并返回‘响应’    这是你必须记住的流程！
def home(request):
    return HttpResponse('Hello, World!')
