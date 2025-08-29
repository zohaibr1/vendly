from django.contrib.auth                    import authenticate
from rest_framework.views                   import APIView
from rest_framework.response                import Response
from rest_framework                         import status, permissions
from rest_framework_simplejwt.tokens        import RefreshToken
from accounts.serializers.auth_serializers  import LoginSerializer
from accounts.serializers.user_serializers  import UserSerializer

class LoginView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            user=authenticate(username=username, password=password)
            if user:
                refresh=RefreshToken.for_user(user)
                return Response({"refresh":str(refresh),"access":str(refresh.access_token),"user":UserSerializer(user).data},status=status.HTTP_200_OK)
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    