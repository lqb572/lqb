from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Student)


################################################################
# 批量注册app名为api下的models到admin后台
################################################################

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
app_models = apps.get_app_config("oj").get_models()  # 获取app:api下所有的model,得到一个生成器
# 遍历注册model
for model in app_models:
    try:
        print(model)
        admin.site.register(model)
    except AlreadyRegistered:
        pass
