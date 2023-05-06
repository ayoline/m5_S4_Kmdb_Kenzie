from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "bio",
            "is_critic",
            "updated_at",
        ]
        extra_kwargs = {"password": {"write_only": True}}

        read_only_fields = [
            "is_superuser",
            "is_active",
        ]

    def create(self, validated_data: dict):
        return Account.objects.create_user(**validated_data)


class CriticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
