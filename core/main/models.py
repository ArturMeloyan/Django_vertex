from django.db import models

# Create your models here.
class HomeBG(models.Model):
    img = models.ImageField('BG image', upload_to='media')

class Info(models.Model):
    name = models.CharField('Info name', max_length=30)
    about = models.TextField('Info text')
    img = models.ImageField('Info image', upload_to='media')
    date = models.DateField('Info date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'        
