from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers.auth_serializers import LogoutSerializer

class LogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        serializer=LogoutSerializer(data=request.data)
        if serializer.is_valid():
            try:
                refresh_token=serializer._validated_data['refresh_toke']
                token= RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message':'Successfully logout'},status=status.HTTP_205_RESET_CONTENT)
            except Exception:
                return Response ({"error":"invalid token"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)