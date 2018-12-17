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
    + 在项目文件urls.py中添加路由
        ```python
        from gallery import views

        urlpatterns = [
        path('', views.home),
        ]

        ```
    + 在app的views.py中引入models
        ```python
        from gallery.models import GALLERY

        def home(request):
            # 模型中所有对象
            gallerys = GALLERY.objects
            # 传递到html页面
            return render(request, 'home.html', {'gallerys': gallerys}) 
        ``` 
    + 在home.html中使用在后台添加的数据
        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>首页</title>
            </head>
            <body>
                 <h1>我的主页</h1>
                    <!-- 快捷方式：for+tab -->
                    {% for gallery in gallerys.all %}
                    {{ gallery.description }}
                    {% endfor %}
            </body>
        </html>
        ```
