from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='姓名')
    no = models.IntegerField(null = True,blank = True,verbose_name='学号')
    password = models.CharField(max_length = 400,null = True,blank = True,verbose_name='密码')

    class Meta:
        verbose_name = "学生管理"
        verbose_name_plural = "学生管理"

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='班级名')
    class Meta:
        verbose_name = "班级管理"
        verbose_name_plural = "班级管理"

    def __str__(self):
        return self.name    

class Teacher(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='姓名')
    class Meta:
        verbose_name = "教师管理"
        verbose_name_plural = "教师管理"

    def __str__(self):
        return self.name