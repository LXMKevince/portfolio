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
    + 再次修改models.py让其在后台添加后显示名称，每次修改models都需要迁移到数据库
        ```python
        img = models.ImageField(default='default.png', upload_to='images/')
        title = models.CharField(default='作品标题', max_length=50)

        # 在后台显示标题
        def __str__(self):
             return self.title
        ```
    + 在settings.py中添加媒体路径
        ```python
        # 添加媒体的路径

        MEDIA_URL = '/media/'

        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        ```
    + 修改url.py添加媒体路由
        ```python
        from django.conf.urls.static import static
        from django.conf import settings

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.home),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    + 在前端页面显示加入的媒体（image）
        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>首页</title>
            </head>
            <body>
                <h1>我的主页</h1>
                    {% for gallery in gallerys.all %}
                    {{ gallery.description }}
                    <img src="{{ gallery.img.url }}" alt="">
                    {% endfor %}
            </body>
        </html>
        ```
---
    + 处理静态文件，并进行分分类
        ```python
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'portfolio/static/'),
            # os.path.join(BASE_DIR, 'blog/static/'),
        ]
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        ```
    + 收集静态文件
        >`python manage.py collectstatic`