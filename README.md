- sublime插件
    + Djaneiro 快速生成models
- Django使用
    + 创建Djaingo项目
       >`django-admin startproject 项目名称`
    + 创建APP应用
        >`python manage.py startapp 应用名称`
    + 启动Django项目
        >`python manage.py runserver 端口`
    + 修改setting.py
        ```python
        INSTALLED_APPS = [
            # 注册自己的app
            'gallery.apps.GalleryConfig',
        ]
        TEMPLATES = [
            {
                # 添加模板路径
                'DIRS': ['templates'],
            },
        ]
        ```
    + 编写app中models.py
        >`快捷方式：Model+tab`
        ```python
           class GALLERY(models.Model):
             # 快捷方式：mc+tab，生成模型
              description = models.CharField(max_length=100)
        ```
    + 编写app中admin.py注册models
        ```python
        from .models import GALLERY
        # 注册model
        admin.site.register(GALLERY)
        ```
    + 迁移到数据库
        >`python manage.py makemigrations`
        >`python manage.py migrate`
    + 创建超级管理员
        >`python manage.py createsuperuser`

