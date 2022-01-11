from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apiAssignment import settings
from users.models import User
from users.serializer import UserSerializer
import jwt

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Key Error"})
        user = authenticate(email=email, password=password)
        #장고의 authenticate function을 활용하여, email과 password가 일치하면 user 반환
        #정보가 하나라도 없다면, key error 메시지 전송

        #정보가 일치하다면 token 발행
        if user is not None:
            encode_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encode_jwt})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class MeView(APIView):
    #각 클래스마다 전부 사용한다면 사용(개별로는 사용하기 어렵다)
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        #partial은 전체가 아닌 일부수정
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if request.user.is_admin:
            try:
                user = User.objects.get(pk=pk)
                return Response(UserSerializer(user).data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message": "Only admin can do this "})

