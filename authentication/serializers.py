from .models import User

from rest_framework import serializers,status
from rest_framework.validators import ValidationError

from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=True)
    email = serializers.EmailField(max_length=80, allow_blank=False)        # yesari serializers.EmailField garyo vani front end batw yedi email halni thau ma aru nai kei kura halyo vani... serializer le nai request pass huna didaina i.e Invalid Email Field yesto response dincha front end ma.. i.e model le check garnai parena.. serialization mai check vayo invalid email field vanera   
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(allow_blank=False, write_only=True)    # password ko kura database ma matra halincha.. database batw fetch garinna i.e frontend ma dekhaidaina so tehi vayera fetch garna namilos vanera write_only = True gareko

    class Meta:
        model = User
        fields=['id','username', 'email', 'phone_number','password']        # jun jun field ko data lai serialize garne ho tei tei field lai yaha lekhni


    def validate(self, attrs):                                              # views.py ma, serializer.is_valid() check garda yo validate() method execute huncha   # overriding the serializer's inbuilt validate() method
        email = User.objects.filter(email = attrs.get('email')).exists()
        if email:
            raise ValidationError(detail="User with email already exists", code = status.HTTP_403_FORBIDDEN)

        username = User.objects.filter(username = attrs.get('username')).exists()
        if username:
            raise ValidationError(detail="User with username already exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)                                      # returning validated attributes value


    def create(self, validated_data):                                       # views.py ma, serializer.save() garda yo create() method execute huncha
        new_user = User(**validated_data)
        new_user.password = make_password(validated_data.get('password'))
        new_user.save()                                                     # newly created user database ko table ma save vayo

        return new_user                                                     # yo serializer le, newly registered data lai return garcha



