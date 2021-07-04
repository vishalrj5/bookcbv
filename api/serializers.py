#form,modelform
#serializer,modelserializer

from rest_framework import serializers
from bookapp.models import BookModel


class BookSerializer(serializers.Serializer):

    book_name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    pages=serializers.IntegerField()

    def validate(self, validated_data):
        if validated_data["price"]<0:
            raise serializers.ValidationError("Provide valid price")
        if validated_data["pages"]<0:
            raise serializers.ValidationError("Provide Valid number of pages")
        return validated_data

    def create(self, validated_data):
        return BookModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book_name = validated_data.get("book_name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.pages = validated_data.get("pages")
        instance.save()
        return instance

class BookClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
    def validate(self,data):
        if data["price"]<0:
            raise serializers.ValidationError("Provide valid price")
        if data["pages"]<10:
            raise serializers.ValidationError("provide right number of pages")
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    passwords = serializers.CharField()

