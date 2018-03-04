from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    lastime=models.TimeField(auto_now=True)
    createtime=models.TimeField(auto_now=True)
    def __str__(self):
        return self.gname
    class Meta:
        db_table="grades"
        ordering=['id']


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

class Students(models.Model):
    #自定义模型管理器
    #当自定义模型管理器，objects就不存在了
    stuObj=models.Manager()
    stuObje2=StudentsManager()
    sname=models.CharField(max_length=20)
    sgrade=models.ForeignKey('Grades',on_delete='descase')
    scontend=models.CharField(max_length=20)
    def __str__(self):
        return self.sname
    lastime = models.TimeField(auto_now=True)
    createtime = models.TimeField(auto_now=True)
    class Meta:
        db_table="students"
        ordering=['id']