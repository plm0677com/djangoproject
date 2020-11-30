from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.DO_NOTHING)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.DO_NOTHING)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.DO_NOTHING)


"""
    可以看到，创建的所有模型类，Board ， Topic 和 Post 都是 django.db.models.Model 的子类，它们都将会转化成数据表。
而 django.db.models.Field 的子类（Django 内置的核心类）的实例都会转化为数据表中的列。上面可以看到的 CharField，DateTimeField 等，
都是 django.db.models.Field 的子类，在 Django 项目中都可以直接使用它们。

    在这里，我们仅仅使用了 CharField，TextField，DateTimeField，和 ForeignKey 字段来定义我们的模型（Models） 。
当然，在 Django 中，不仅仅只是提供了这些字段，还提供了更多，更广泛的选择来代表不同类型的数据，
比如还有：IntegerField，BooleanField， DecimalField。我们会根据不同的需求来使用它们。

    有些字段是需要参数的，就好比 CharField ，我们都设定了一个 max_length , 设置一个最大长度。当我们设定了这个字段后，就会作用于数据的。
在 Board 模型（Model）中，在 name 字段中，我们也设置了参数 unique=True，顾名思义，这是为了在数据库中，保证该字段的唯一性。

    在 Post 模型中，created_at 字段有一个可选参数，auto_now_add 设置为 True。这是为了指明 Django 在创建 Post 对象的时候，created_at 使用的是当前的日期和时间。
创建模型与模型之间关系的其中一种方法就是使用 ForeignKey 字段，使用这个字段，会自动创建模型与模型之间的联系，而且会在数据库中也创建它们的关系。使用 ForeignKey 会有一个参数，来表明他与那个模型之间的联系。 例如：

    在 Topic 模型中，models.ForeignKey(Board, related_name='topics')，第一个参数是代表关联的表格（主表），在默认情况下，外键存储的是主表的主键（Primary Key）。
第二个参数 related_name 是定义一个名称，用于反向查询的。Django 会自动创建这种反向关系。 虽然 related_name 是可选参数，但是如果我们不为它设置一个名称的，Django 会默认生成名称 (class_name)_set 。

    例如，在 Board 模型中，Topic 实例将在该 topic_set 属性下可用。而我们只是将其重新命名为topics，使用起来更加自然。

    在 Post 模型中，updated_by 字段设置related_name='+'。这指示 Django 我们不需要这种反向关系。
下面这张图可以很好地看到设计图和源码之间的比较，其中绿线就表示了我们是如何处理反向关系的。
"""
