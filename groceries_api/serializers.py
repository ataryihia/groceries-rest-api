from rest_framework import serializers
from groceries_api import models



class ProfileSerializer(serializers.ModelSerializer):
    """serialize user items"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class GroceriesItemSerializer(serializers.ModelSerializer):
    """serialize groceries items"""

    class Meta:
        model = models.Groceries

        fields = ('id', 'user_profile', 'name', 'created_on', 'expire_on', 'quantity')
        extra_kwargs= {'user_profile': {'read_only':True}}
