from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, BabySerializer, DiaperSerializer, FeedingSerializer, AffirmationSerializer
from .models import User, Baby, Diaper, Feeding, Affirmation


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
