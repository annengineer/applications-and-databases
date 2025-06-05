from django.db import models

# Create your models here.
class Members(models.Model):
    
    name = models.CharField(max_length=200, verbose_name="Имя") 
    image = models.ImageField(upload_to='program_images/', blank=True, null=True)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон')
    resume = models.TextField('Резюме')
    portfolio_link = models.URLField('Ссылка на портфолио', blank=True)


    
    def __str__(self):
        return f'{self.name}'  
    
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

class Management(models.Model):
    name =  models.CharField(max_length=200, verbose_name="Имя") 
    image = models.ImageField(upload_to='managers_images/', blank=True, null=True)
    post = models.CharField(verbose_name="Должность")
    email = models.CharField()

    def __str__(self):
        return f'{self.name}'  
    
    class Meta:
        verbose_name = "Руководители"
        verbose_name_plural = "Руководители"

class EP(models.Model):
    name  = models.CharField(max_length=200, verbose_name="ОП")
    direct = models.CharField(verbose_name="Направление")
    education_material = models.TextField('Что изучают студенты')
    advantage = models.TextField('Преимущества')
    persp = models.TextField('Перспективы')
    link = models.URLField('Ссылка на ОП', blank=True)     
    
    def __str__(self):
        return f'{self.name}'  
    
    class Meta:
        verbose_name = "ОП"
        verbose_name_plural = "ОП"
  



        
