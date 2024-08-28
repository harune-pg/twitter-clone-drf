from django.urls import path

from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
# from dj_rest_auth.jwt_auth import get_refresh_view

from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # TODO: あとで
    # path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    # FIXME: ログイン確認用（暫定）
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
]
