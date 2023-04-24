from rest_framework.serializers import ModelSerializer
from marketplace.models import Item

from django.contrib.auth.models import User
from rest_framework import serializers

class MarketSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'desc', 'author', 'image', 'price', 'market_status', 'condition', 'category', 'location']
    
    def __str__(self):
        return str(self.author)



# class ProfilesSerializer(ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'first_name', 'last_name', 'user', 'bio', 'email', 'country', 'avatar', 'friends']

#         def __str__(self):
#             return str(self.first_name)
        
# class ProfilesSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

#     class Meta:
#         model = Profile
#         fields = '__all__'

#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         instance = super().update(instance, validated_data)
#         instance.user = self.context['request'].user
#         instance.save()
#         return instance
  