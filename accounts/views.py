from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    """
    Logout View.
    """

    def post(self, request):
        """
        Delete token to perform the respective logout.
        """
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)
