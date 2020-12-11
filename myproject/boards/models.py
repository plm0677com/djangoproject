# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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


class BondFund(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    fund_ratio2020 = models.FloatField(max_length=4)
    fund_ratio2019 = models.FloatField(max_length=4)
    fund_ratio2018 = models.FloatField(max_length=4)
    fund_ratio2017 = models.FloatField(max_length=4)
    fund_ratio2016 = models.FloatField(max_length=4)
    fund_ratio_avg = models.FloatField(max_length=4)
    fund_rate1 = models.FloatField(max_length=4)
    fund_rate2 = models.FloatField(max_length=4)
    fund_rate3 = models.FloatField(max_length=4)
    fund_rate4 = models.FloatField(max_length=4)
    fund_rate_sum = models.FloatField(max_length=4)
    fund_position_shares = models.FloatField(max_length=4)
    fund_position_bond = models.FloatField(max_length=4)
    fund_position_other = models.FloatField(max_length=4)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

