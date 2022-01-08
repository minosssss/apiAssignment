import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework import authentication, exceptions
from users.models import User


#header에서 token을 이용하기 위한 인증
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, token = token.split(" ")
            decode = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decode.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except ValueError:
            return None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed(detail="JWT format invalid")