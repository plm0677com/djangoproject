## venv

### 配置

virtualenv venv

-p python.exe地址  （指定python地址）

### 启动

venv\Scripts\activate

### 停用

venv\Scripts\deactivate.bat



## 前端页面设计

https://www.bootcdn.cn/

## django

### 启动新项目

django-admin startproject '项目名'

### 目录如下

> manage.py : 使用Django-admin 命令行实用程序的快捷方式。它用于运行与项目相关的管理命令。我们将使用它来运行开发服务器、运行测试、创建迁移等等。
>
> __init__.py: 此空文件告诉Python此文件夹是python的包。
>
> setting.py: 此文件包含项目的所有配置。我们将参考这个文件所有的时间。
>
> urls.py: 此文件负责映射我们项目中的路由和路径。例如，如果要在URL中显示内容，必须先映射它。`/about/`
>
> wsgi.py: 此文件是用于部署的简单网关接口

### 启动Django的web服务器

python manage.py runserver

### 创建我们的第一个应用

django-admin startapp boards

> migrations/: 在这里，Django存储一些文件来跟踪您在models.py文件，以便保存数据库和models.py同步
>
> admin.py : 这是一个名为Django Admin的内置Django应用程序的配置文件
>
> apps.py : 这是应用程序本身的配置文件
>
> models.py : 这里是我们定义Web应用程序实体的地方。模型由Django自动转换为数据库表
>
> test.py: 此文件用于编写应用程序的单元测试。
>
> views.py: 这是我们处理Web应用程序的请求/响应周期的文件

### setting.py

INSTALLED_APPS：列出已安装的应用。我们把我们的应用boards添加到 INSTALLED_APPS

### views.py

使用 Django 创建新页面的外观。

### urls.py

现在我们必须告诉 Django什么时候提供这个views.

## 编写一个视图

### step1: views.py

```python
from django.http import HttpResponse
# 每个视图负责执行以下两项操作之一：返回包含所请求页面内容的HttpResponse对象，或引发异常（如Http404）

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### step2:应用目录中创建urls.py

```python
from django.urls import path

from . import views
# path(路线，视图， kwargs = 无， 名称 =无)
urlpatterns = [
    path('', views.index, name='index'),
]
```

### step3:下一步是将根URLconf指向模块(项目指向应用)

```python
from django.contrib import admin
from django.urls import include, path
# include(模块，命名空间=无)
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## 编写一个应用程序

### step1:数据库设置 setting.py->DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # ENGINE 引擎
        'NAME': BASE_DIR / 'db.sqlite3',
        # NAME 数据库的名称
    }
}
```

### step2:将应用添加到项目

```python
INSTALLED_APPS = [
    'django.contrib.admin',  # 管理网站
    'django.contrib.auth',  # 身份验证系统
    'django.contrib.contenttypes',  # 内容类型的框架
    'django.contrib.sessions',  # 会话框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 管理静态文件
    'boards' # 自己的应用
]
```

## 创建模型

在命令行中运行

```shell
python manage.py migrate   #  创建表结构
python manage.py makemigrations boards  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
python manage.py sqlmigrate boards 0001
```

### `__str__`方法

```python
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
#  向模型添加 __str__（） 方法非常重要，这不仅是为了在处理交互式提示时方便自己，还因为对象表示在 Django 的自动生成的管理员中使用    
```

## 管理员

### step1:创建管理员用户

```shell
py manage.py createsuperuser
```

### step2:

setting->language下设置语言

### step3:使应用在管理员中可修改 **admin.py**

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## 模板使用

### step1:在项目文件下创建template文件夹

### step2:模板绑定

```python
# setting 下 TEMPLATES
'DIRS': [os.path.join(BASE_DIR, 'template')]
```

### step3:使用模板

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

### render()函数

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

### 抛出404

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

### get_object_or_404()函数

```python
from django.shortcuts import get_object_or_404, render
# 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程。Django 也提供了一个快捷函数
from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```



## 为URL名称添加命名空间

在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。Django 如何分辨重名的 URL 呢？

答案是：在根 URLconf 中添加命名空间。在 `polls/urls.py` 文件中稍作修改，加上 `app_name` 设置命名空间：

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```







### 论坛项目

#### 如果要实现上面我们说到的论坛，那么我们至少需要以下的几个模型：**Board**，**Topic**，**Post**和**User**。

- **Board** : 版块
- **Topic** : 主题
- **Post** : 帖子（用户评论与回复）
- **User** : 用户
- ![image-20201130152712791](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201130152712791.png)
  如下图，`1` 代表一个 Topic 必须与一个 Board 相关联，`0..*` 代表 Board 下面可能会有多个和 0 个 Topic ，也就是一对多的关系。

#### 这个类图强调的是模型之间的关系，当然最后这些线条和箭头都会用字段来进行表示。

- **Board（版块模型）** ：Board 中有 **name** 和 **description** 这两个字段，name 是唯一的，主要是为了避免两个名称重复。description 则是用于描述把这个版块来用干什么的。

- **Topic（主题模型）** ：subject 表示主题内容，last_update 用来定义话题的排序，starter 用来识别谁发起的话题，board 用于指定它属于哪个版块

- **Post（帖子模型）** ： message 字段，用于存储回复的内容，created_at 创建的时间，在排序时候用（最先发表的帖子排最前面），updated_at 更新时间，告诉用户是否更新了内容，同时，还需要有对应的 User 模型的引用，Post 由谁创建的和谁更新的。

- **User（用户模型）** ：这里有 username ，password，email 和 is_superuser 四个字段。

这里值得注意的是，我们在 Django 应用中，不需要创建 User 用户模型，因为在 Django 的 contrib 中已经内置了 User 模型，我们可以直接拿来使用，就没必要重新创建了。

`python manage.py makemigrations`

