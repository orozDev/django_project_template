from rest_framework import serializers

from apps.account.models import User


class ShortDescUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'last_activity',
            'is_public_contacts',
            'allow_notifications',
            'region',
            'password',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions'
        )
