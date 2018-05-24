""" """
import logging
import json

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from . import serializers, helpers

logs = logging.getLogger(__name__)


class signIn(APIView):
    """API endpoint for authentication process
    """
    serializer_class = serializers.AuthTokenSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        """
        Authenticate user details

        To pass authentication process user should verify following details

            1. username

            2. password
        """
        response = {
            "token": "",
            "email": "",
            "full_name": ""
        }
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response['token'] = token.key
        response['email'] = user.email
        response['full_name'] = user.get_full_name()
        return Response(response, status=status.HTTP_200_OK)


class signOut(APIView):
    """API endpoint to destroy user token (Destroy API session)
    """

    def delete(self, request):
        token = request.user.auth_token
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataList(APIView):
    """API enpoint to get list of all CSV datasheet details"""

    def get(self, request, *args, **kwargs):
        """
        API endpoint to get list on all CSV details

        Following filters implement in this API

        1. title

        2. description

        """
        csv_file = settings.GET_DATA()
        if csv_file.empty:
            response = {
                'non_field_errors': 'Detail not available'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        csv_file = csv_file[
            csv_file[
                'title'
            ].apply(
                lambda x: request.GET.get('title', '') in x
            ) &
            csv_file[
                'description'
            ].apply(
                lambda x: request.GET.get('description', '') in x
            )
        ]
        response = csv_file.to_json(
            orient="records",
            date_format="epoch",
            double_precision=10,
            force_ascii=True,
            date_unit="ms", default_handler=None)
        response = json.loads(response)
        if settings.SOFT_IMAGE_VALIDATION:
            for x in response:
                x['image'] = helpers.validate_image(x['image'])
        return Response(response, status=status.HTTP_200_OK)


class DynamicDataList(APIView):
    """API enpoint to get list of all CSV datasheet details"""

    @method_decorator(cache_page(60))
    def get(self, request, *args, **kwargs):
        """
        API endpoint to get list on all CSV details

        Following filters implement in this API

        1. title

        2. description

        """
        try:
            limit = int(request.GET.get('limit', 20))
            offset = int(request.GET.get('offset', 20))
        except Exception as e:
            response = {
                'non_field_errors': 'Bad value set for filter field'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        csv_file = helpers.cache_csv_data(
            settings.DB_URL, settings.URL_OUTPUT_TYPE,
            skiprows=[1, offset], nrows=limit
        )
        if csv_file.empty:
            response = {
                'non_field_errors': 'Detail not available'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        csv_file = csv_file[
            csv_file[
                'title'
            ].apply(
                lambda x: request.GET.get('title', '') in x
            ) &
            csv_file[
                'description'
            ].apply(
                lambda x: request.GET.get('description', '') in x
            )
        ]
        response = csv_file.to_json(
            orient="records",
            date_format="epoch",
            double_precision=10,
            force_ascii=True,
            date_unit="ms", default_handler=None)
        response = json.loads(response)
        if settings.SOFT_IMAGE_VALIDATION:
            for x in response:
                x['image'] = helpers.validate_image(x['image'])
        return Response(response, status=status.HTTP_200_OK)
