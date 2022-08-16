from rest_framework import serializers
from transaction.models import Transaction


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
