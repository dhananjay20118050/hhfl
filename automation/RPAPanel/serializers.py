from django.conf import settings
from rest_framework import serializers
from RPAPanel.models import HhflBankStatements, BotUploadedFiles, Apps, Nodes, Hubs, BotApsTracking, \
    BotApsTrackingBranch, BotErrorLogs
from rest_framework.validators import UniqueTogetherValidator


class AppSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Apps
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Nodes
        fields = '__all__'


class HubSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Hubs
        fields = '__all__'


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotApsTrackingBranch
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotApsTrackingBranch
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HhflBankStatements
        fields = '__all__'


class TimelineSerializer(serializers.Serializer):
    list1 = UpdateSerializer(many=True)
    list2 = TrackSerializer(many=True)


class CompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotApsTrackingBranch
        fields = '__all__'


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotErrorLogs
        fields = '__all__'


class FiledataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUploadedFiles
        fields = '__all__'
