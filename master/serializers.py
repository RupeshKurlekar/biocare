from rest_framework import serializers
from master.models import ReportStatus, Priority, TicketStatus, BodyPart, BodyPartView


class ReportStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportStatus
        fields='__all__'
class PrioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields='__all__'
class TicketStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields='__all__'
class BodyPartSerializers(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields='__all__'
class BodyPartViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = BodyPartView
        fields='__all__'
