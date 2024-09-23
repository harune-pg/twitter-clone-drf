from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SampleAPIView(APIView):
    """常に200_OKを返す"""
    def get(self, request):
        return Response({"message": "Hellow, World"}, status=status.HTTP_200_OK)
