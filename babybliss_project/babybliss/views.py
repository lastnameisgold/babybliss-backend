from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View, DetailView
from .serializers import UserSerializer, BabySerializer, DiaperSerializer, FeedingSerializer, AffirmationSerializer
from .models import User, Baby, Diaper, Feeding, Affirmation


class HomeView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {
            'message': 'Welcome to BabyBliss!'},
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response({
                'refresh': str(refresh),
                'access': str(access),
            })
        else:
            return Response(serializer.errors, status=400)


class CreateUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': f'User {user.username} created successfully'}, status=status.HTTP_201_CREATED)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BabyList(generics.ListCreateAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer


class BabyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer


class DiaperList(generics.ListCreateAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializer


class DiaperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diaper.objects.all()
    serializer_class = DiaperSerializer


class FeedingList(generics.ListCreateAPIView):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer


class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer


class AffirmationList(generics.ListCreateAPIView):
    queryset = Affirmation.objects.all()
    serializer_class = AffirmationSerializer


class AffirmationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Affirmation.objects.all()
    serializer_class = AffirmationSerializer
