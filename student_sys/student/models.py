#########################################
# 作者：小纯洁				#
# 时间：2019.6.8			#
#########################################
from django.db import models

# Create your models here.


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '扶他'),
    ]
    STATUS_ITEMS = [
        (0, '申请中'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(verbose_name="姓名", max_length=128)
    sex = models.IntegerField(verbose_name="性别", choices=SEX_ITEMS)
    profession = models.CharField(verbose_name="职业", max_length=128)
    email = models.EmailField(verbose_name="Email", max_length=254)
    qq = models.CharField(verbose_name="QQ", max_length=128)
    phone = models.CharField(verbose_name="电话", max_length=128)

    status = models.IntegerField(
        verbose_name="审核状态", choices=STATUS_ITEMS, default=0)
    created_time = models.DateTimeField(
        verbose_name="创建时间", editable=False, auto_now_add=True)

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"
