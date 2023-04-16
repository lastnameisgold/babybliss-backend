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

    # diaper_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Diaper.objects.all(),
    #     source='diapers',
    #     many=True,
    # )

    # feeding_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Feeding.objects.all(),
    #     source='feedings',
    #     many=True,
    # )

    class Meta:
        model = Baby
        fields = ('name', 'dob', 'gender', 'user', 'diapers',
                  'feedings')


class DiaperSerializer(serializers.HyperlinkedModelSerializer):
    baby = serializers.HyperlinkedRelatedField(
        view_name='baby_detail',
        many=False,
        read_only=True)

    # baby = BabySerializer(
    #     read_only=True
    # )

    class Meta:
        model = Diaper
        fields = ('log', 'diaper', 'rash', 'notes', 'baby', 'id')


class FeedingSerializer(serializers.HyperlinkedModelSerializer):
    baby = serializers.HyperlinkedRelatedField(
        view_name='baby_detail',
        many=False,
        read_only=True)

    # baby = BabySerializer(
    #     read_only=True
    # )

    # diaper_id = seriarializer.PrimaryKeyRelatedField(
    #     queryset=Diaper.objects.all(),
    #     source='diaper',
    # )

    class Meta:
        model = Feeding
        fields = ('log', 'amount',
                  'method', 'notes', 'baby', 'id')


class AffirmationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=False,
        read_only=True)

    class Meta:
        model = Affirmation
        fields = ('message', 'user')
