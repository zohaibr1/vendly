from django.views import View
from rest_framework import status, generics
from rest_framework.response import Response
from accounts.serializers.auth_serializers import RegisterSerializer
from accounts.models import User

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
    
    #admin aprroval for vendor
        if user.role=='vendor':
            user.is_active=False
            user.save()
            message="Registration form is submitted!, Wait for admin Approval"
        else:
            message="Registration processed succefully!, You can Login Now!!!"
        
        return Response({'message':message, 'user_id':user.id},status=status.HTTP_201_CREATED)
    
    