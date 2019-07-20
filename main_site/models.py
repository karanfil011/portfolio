from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=255, blank=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

class AboutMe(models.Model):
    values = models.TextField(blank=True, verbose_name='Ценности')
    goals = models.TextField(blank=False, verbose_name='Цели')
    hobbies = models.TextField(blank=False, verbose_name='Хобби')
    about_me = models.TextField(blank=False, verbose_name='Обо мне')

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

class MySkills(models.Model):
    about_skills = models.TextField(blank=True, verbose_name='Скиллы')
    html_css = models.IntegerField(blank=False, verbose_name='HTML/CSS')
    js = models.IntegerField(blank=False, verbose_name='JS')
    python_django = models.IntegerField(blank=False, verbose_name='Python(Django)')
    sql = models.IntegerField(blank=False, verbose_name='SQL')

    class Meta:
        verbose_name = 'Скиллы'
        verbose_name_plural = 'Скиллы'

class MyEducation(models.Model):
    about_education = models.TextField(blank=True, verbose_name='Об образовании')
    sertificate = models.CharField(max_length=255, blank=False, verbose_name='Диплом')
    degree = models.CharField(max_length=255, blank=False, verbose_name='Место учебы')
    year = models.IntegerField(blank=True, verbose_name='Лет Обучение', default=0)
    start_date = models.DateTimeField(blank=True, auto_now_add=False, auto_now=False)
    end_date = models.DateTimeField(blank=True, auto_now_add=False, auto_now=False)
    about_degree = models.TextField(blank=False, verbose_name='О учебе')

    class Meta:
        verbose_name = 'Образвание'
        verbose_name_plural = 'Образвание'


class MyExperience(models.Model):
    about_experience = models.TextField(blank=True, verbose_name='О работе')
    worked_as = models.CharField(max_length=255, blank=False, verbose_name='Работал')
    place = models.CharField(max_length=255, blank=False, verbose_name='Место работы')
    start_date = models.DateTimeField(blank=True, auto_now_add=False, auto_now=False)
    end_date = models.DateTimeField(blank=True, auto_now_add=False, auto_now=False)
    year = models.IntegerField(blank=True, verbose_name='Лет Работы', default=0)
    about_job = models.TextField(blank=False, verbose_name='О работе')

    class Meta:
        verbose_name = 'Опыт Работы'
        verbose_name_plural = 'Опыт Работы'

class Portfolio(models.Model):
    about_portfolio = models.TextField(blank=True, verbose_name='О портфолио')
    image = models.ImageField(upload_to='media/', blank=False, verbose_name='Изображение')
    link = models.CharField(max_length=500, blank=False, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'