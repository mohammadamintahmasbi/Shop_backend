from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    # set_password use to save password hashed in db
    def create(self, validate_data):
        user = User(email=validate_data["email"])
        user.set_password(validate_data["password"])
        user.save()
        return user