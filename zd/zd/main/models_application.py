# main/models_application.py
from django.db import models
from django.conf import settings
from decimal import Decimal

class Application(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В обработке'),
        ('approved', 'Одобрена'),
        ('rejected', 'Отклонена'),
    ]
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    #Навыки
    skill_list = models.TextField('Ваши навыки', default='JS, REACT, TypeScript')

    # Организация
    organization_name = models.CharField('Наименование организации', max_length=255, default='NewOrg')
    organization_inn = models.CharField('ИНН организации', max_length=12, default='1000000000')
    organization_website = models.URLField('Сайт организации', blank=True, default='http://NewOrg.com')
    
    # Предлагаемое решение
    solution_name = models.CharField('Краткое наименование решения', max_length=255, default='-')
    solution_description = models.TextField('Описание предлагаемого решения', default='-')
    solution_experience = models.TextField('Релевантный опыт применения', default='-')

    # Контакты
    contact_first_name = models.CharField('Имя', max_length=100, default='Тимур')
    contact_last_name = models.CharField('Фамилия', max_length=100, default='Шокиров')
    contact_middle_name = models.CharField('Отчество', max_length=100, blank=True)
    contact_phone = models.CharField('Телефон', max_length=20, default='+79879879292')
    contact_email = models.EmailField('Электронная почта', default='ya@gmail.com')
    
    # Системные поля
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    #РЕСУРС-ЦЕНА
    requirement_name = models.TextField('Название ресурса', max_length=255, default='Ноут')
    requirement_price = models.CharField('Цена ресурса', default=10000, max_length=255)
    
    
    # Связь с пользователем
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Пользователь'
    )
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Заявка от {self.organization_name} ({self.created_at.strftime('%d.%m.%Y')})"

