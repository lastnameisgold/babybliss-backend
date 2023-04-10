from rest_framework import serializers
from .models import User, Baby, Diaper, Feeding, Affirmation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    babies = serializers.HyperlinkedRelatedField(
        view_name='baby_detail',
        many=True,
        read_only=True)

    affirmations = serializers.HyperlinkedRelatedField(
        view_name='affirmation_detail',
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'babies', 'affirmations')


class BabySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=False,
        read_only=True)

    diapers = serializers.HyperlinkedRelatedField(
        view_name='diaper_detail',
        many=True,
        read_only=True)

    feedings = serializers.HyperlinkedRelatedField(
        view_name='feeding_detail',
        many=True,
        read_only=True)

    class Meta:
        model = Baby
        fields = ('name', 'age', 'gender', 'user', 'diapers', 'feedings')


class DiaperSerializer(serializers.HyperlinkedModelSerializer):
    baby = serializers.HyperlinkedRelatedField(
        view_name='baby_detail',
        many=False,
        read_only=True)

    class Meta:
        model = Diaper
        fields = ('log', 'diaper', 'rash', 'notes', 'baby')


class FeedingSerializer(serializers.HyperlinkedModelSerializer):
    baby = serializers.HyperlinkedRelatedField(
        view_name='baby_detail',
        many=False,
        read_only=True)

    class Meta:
        model = Feeding
        fields = ('date', 'time', 'duration', 'amount',
                  'breastFed', 'bottleFed', 'notes', 'baby')


class AffirmationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=False,
        read_only=True)

    class Meta:
        model = Affirmation
        fields = ('date', 'message', 'user')
