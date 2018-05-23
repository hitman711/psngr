"""
"""
import logging
from rest_framework import serializers
from rest_framework.compat import authenticate

logs = logging.getLogger(__name__)


class AuthTokenSerializer(serializers.Serializer):
    """
    """
    username = serializers.CharField(label="username")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get(
                    'request'), username=username, password=password)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(
                        msg, code='authorization')
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
