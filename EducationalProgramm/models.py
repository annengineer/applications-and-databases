from django.db import models

# Create your models here.
class EducationProgram(models.Model):
    MODULE = [
        (1, '1 модуль'),
        (2, '2 модуль'),
        (3, '3 модуль'),
        (4, '4 модуль'),
    ]
    COURSE = [
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс')
    ]
    name = models.CharField(max_length=200, verbose_name="Название проекта") 
    year = models.IntegerField(verbose_name="Год Обучения", default=2025) 
    course = models.IntegerField(choices=COURSE, verbose_name="Курс", default=3)
    module = models.IntegerField(choices=MODULE, verbose_name="Модуль")  
    discipline = models.CharField(max_length=200, verbose_name="Название дисциплины", default='')
    is_team = models.BooleanField(default=False, verbose_name="GIS-анализ")
    description = models.TextField(blank=True, verbose_name="Review", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    link = models.URLField('Ссылка на проект', blank=True, default= 'https://hsedesign.ru/designer/LOUD') 


    def __str__(self):
        return f'{self.name} - {self.discipline} - {self.year}'  
    
    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']
