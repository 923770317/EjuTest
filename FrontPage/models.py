#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here

#
class ReleaseVersion(models.Model):

    project = models.CharField(u"所属项目",max_length=20)

    mod = models.CharField(u"模块",max_length=50)

    version = models.CharField (u"版本号",max_length=100)

    lastOnLineDate = models.DateField(u"最后上线日期",null=True,blank=True)

    remark =  models.CharField(u"备注",max_length=200,null=True,blank=True)

    def __unicode__(self):
        return self.mod


class ProdectSiste(models.Model):
    modeleNmae= models.CharField(u'应用名',max_length=30)
    g4Address = models.CharField(u'G4地址',max_length=30)
    g5Address = models.CharField(u'G5地址', max_length=30)
    port = models.CharField(u'端口号',max_length=10)

    def __unicode__(self):
        return self.modeleNmae