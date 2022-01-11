from django.contrib.auth import authenticate, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apiAssignment import settings
from users.models import User
from users.permission import IsSelf
from users.serializer import UserSerializer
import jwt

class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["post"])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Key Error"})
        user = authenticate(email=email, password=password)
        # 장고의 authenticate function을 활용하여, email과 password가 일치하면 user 반환
        # 정보가 하나라도 없다면, key error 메시지 전송

        # 정보가 일치하다면 token 발행
        if user is not None:
            encode_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encode_jwt})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action( detail=False, methods=['get'])
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


