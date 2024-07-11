from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager
from utils.models import TimeStampAbstractModel
from uuid import uuid4


class User(AbstractUser):
    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
        ordering = ('-date_joined',)

    avatar = ResizedImageField(_('аватарка'), size=[500, 500], crop=['middle', 'center'],
                               upload_to='avatars/', force_format='WEBP', quality=90, null=True, blank=True)
    phone = PhoneNumberField(_('номер телефона'), unique=True, null=True)
    email = models.EmailField(_('электронная почта'), blank=True, null=True, unique=True)
    last_activity = models.DateTimeField(_('последнее действие'), blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    get_full_name.fget.short_description = _('полное имя')

    def __str__(self):
        return f'{self.get_full_name or str(self.phone)}'


def password_reset_key_expire_default():
    return timezone.now() + timezone.timedelta(days=settings.EXPIRE_DAYS)


class UserResetPassword(TimeStampAbstractModel):
    class Meta:
        verbose_name = _('Ключ для сброса пароля')
        verbose_name_plural = _('Ключи для сброса пароля')
        ordering = ('-created_at', '-updated_at')

    user = models.OneToOneField('account.User', on_delete=models.CASCADE, related_name='rest_password',
                                verbose_name=_('пользователь'))
    key = models.UUIDField(_('ключ'), default=uuid4, editable=False)
    expire_date = models.DateTimeField(_('срок действия'), default=password_reset_key_expire_default)

    def __str__(self):
        return f'{self.user}'

# Create your models here.
