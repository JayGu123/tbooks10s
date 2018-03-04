from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    def __str__(self):
        return self.gname
    lastime=models.TimeField(auto_now=True)
    createtime=models.TimeField(auto_now=True)
    class Meta:
        db_table="grades"
        ordering=['id']

class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgrade=models.ForeignKey('Grades',on_delete='descase')
    def __str__(self):
        return self.sname
    lastime = models.TimeField(auto_now=True)
    createtime = models.TimeField(auto_now=True)
    class Meta:
        db_table="students"
        ordering=['id']