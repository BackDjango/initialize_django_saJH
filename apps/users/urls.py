from django.urls import path

from apps.users.apis import RefreshTokenAPI, SignInAPI, SignUpAPI

urlpatterns = [
    path("/signup", SignUpAPI.as_view(), name="signup"),
    path("/signin", SignInAPI.as_view(), name="signin"),
    path("/token/refresh", RefreshTokenAPI.as_view(), name="refresh-token"),
]
