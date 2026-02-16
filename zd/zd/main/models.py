from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from .models_application import Application

class CustomUserManager(BaseUserManager):
    """Менеджер для кастомной модели пользователя"""
    
    def create_user(self, email, username=None, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным email, username и паролем.
        """
        if not email:
            raise ValueError('Email обязателен')
        
        email = self.normalize_email(email)
        
        
        if not username:
            username = email.split('@')[0]
            
            import re
            username = re.sub(r'[^a-zA-Z0-9_]', '', username)
            
            if not username:
                import random
                import string
                username = 'user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        
        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
  
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    email = models.EmailField('Электронная почта', unique=True)
    # profile_image = models.ImageField()

    phone_regex = RegexValidator(
        regex=r'^\+7\d{10}$',
        message="Номер телефона должен быть в формате: '+79991234567'"
    )
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_regex],
        max_length=12,
        blank=True,
        null=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        
        if self.email:
            self.email = self.email.lower()
        
        
        if self.phone_number == '':
            self.phone_number = None
        
        super().save(*args, **kwargs)