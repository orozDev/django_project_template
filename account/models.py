from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager

  
class User(AbstractUser):
    
    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
        ordering = ('-date_joined',)
        
        
    avatar = ResizedImageField(size=[500, 500], crop=['middle', 'center'],
        upload_to='avatars/', force_format='WEBP', quality=90, verbose_name=_('аватарка'), null=True, blank=True) 
    phone = PhoneNumberField(max_length=100, unique=True, verbose_name=_('номер телефона'))
    email = models.EmailField(blank=True, verbose_name=_('электронная почта'), unique=True)
    last_activity = models.DateTimeField(blank=True, 
        null=True, verbose_name=_('последнее действие'),)
  
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'
    get_full_name.fget.short_description = _('полное имя')    

    def __str__(self):
        return f'{self.get_full_name or str(self.phone)}'

# Create your models here.