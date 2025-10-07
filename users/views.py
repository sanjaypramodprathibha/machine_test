from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


@api_view(['POST'])
def register_user(request):
    """
    User registration endpoint with validation
    """
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        # Return user data without password
        user_serializer = UserSerializer(user)
        return Response({
            'message': 'User registered successfully',
            'user': user_serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'message': 'Registration failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    """
    GET /users/ - Get all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveDestroyAPIView):
    """
    GET /users/{id}/ - Get user by ID
    DELETE /users/{id}/ - Delete user by ID
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'