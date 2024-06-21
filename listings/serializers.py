# from rest_framework import serializers
# from .models import Item
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _

# class ItemSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#     reserved_by = serializers.PrimaryKeyRelatedField(
#         queryset=get_user_model().objects.all(), 
#         required=False,
#         allow_null=True
#     )

#     user_first_name = serializers.SerializerMethodField()
#     user_last_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Item
#         fields = ['id', 'user', 'user_first_name', 'user_last_name', 'name', 'description', 'category', 'condition', 'image', 'available', 'created_at', 'reserved', 'reserved_by']

#     def get_user_first_name(self, obj):
#         return obj.user.first_name if obj.user else None

#     def get_user_last_name(self, obj):
#         return obj.user.last_name if obj.user else None

    

#     # class Meta:
#     #     model = Item
#     #     fields = '__all__'

#     # def validate_reserved_by(self, value):
#     #     if value == self.context['request'].user:
#     #         raise serializers.ValidationError(_("You cannot reserve your own item."))
#     #     return value


#     def update(self, instance, validated_data):
#         if 'reserved_by' in validated_data:
#             user = self.context['request'].user
#             if validated_data['reserved_by'] == user:
#                 raise serializers.ValidationError(_("You cannot reserve your own item."))
#         return super().update(instance, validated_data)


from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .models import Item  

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    reserved_by = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), 
        required=False,
        allow_null=True
    )

    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)  # Use ImageField to include the URL

    class Meta:
        model = Item
        fields = ['id', 'user', 'user_first_name', 'user_last_name', 'name', 'description', 'category', 'condition', 'image', 'available', 'created_at', 'reserved', 'reserved_by']

    def get_user_first_name(self, obj):
        return obj.user.first_name if obj.user else None

    def get_user_last_name(self, obj):
        return obj.user.last_name if obj.user else None

    def update(self, instance, validated_data):
        if 'reserved_by' in validated_data:
            user = self.context['request'].user
            if validated_data['reserved_by'] == user:
                raise serializers.ValidationError(_("You cannot reserve your own item."))
        return super().update(instance, validated_data)


    # class Meta:
    #     model = Item
    #     fields = '__all__'

    # def validate_reserved_by(self, value):
    #     if value == self.context['request'].user:
    #         raise serializers.ValidationError(_("You cannot reserve your own item."))
    #     return value

    