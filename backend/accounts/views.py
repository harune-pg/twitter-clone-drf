from rest_framework.generics import CreateAPIView

from .serializers import UserCreateSerializer


class SignupView(CreateAPIView):
    """ユーザーの情報を受け取り、ユーザーを作成する"""
    serializer_class = UserCreateSerializer
