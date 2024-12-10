from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    RefreshTokenView,
    CheckVerificationView,
    GetUserDataView,
    CheckTokenView,
    GetProfileView,
    UpdateImageView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh_token/', RefreshTokenView.as_view(), name='refresh_token'),
    path('check_verification/', CheckVerificationView.as_view(),
         name='check_verification'),
    path('user_data/', GetUserDataView.as_view(),
         name='user_data'),
    path('check_token/', CheckTokenView.as_view(), name='check_token'),
    path('get_profile/', GetProfileView.as_view(), name='get_profile'),
    path('update_image/', UpdateImageView.as_view(), name='update_image'),
]
