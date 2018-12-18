from django.db import models

# Create your models here.


class GALLERY(models.Model):

    description = models.CharField(default='在这里写作品的简介', max_length=100)
    img = models.ImageField(default='default.jpg', upload_to='images/')
    title = models.CharField(default='作品标题', max_length=50)

    # 在后台显示标题
    def __str__(self):
        return self.title
