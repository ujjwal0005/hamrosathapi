from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'password', 'password2', 'email', 'number','gender','dob','image','is_doctor')
        extra_kwargs = {
            'number': {'required': True},
            'name': {'required': True},
            'image':{'required':False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def to_representation(self, instance):
        user = super().to_representation(instance)
        user.pop('password',{})
        user.pop('password2',{})
        token,_ = Token.objects.get_or_create(user=instance)
        user['token']=token
        return user

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            number=validated_data['number'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            dob=validated_data['dob'],
            is_doctor = validated_data['is_doctor'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class updateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'number','gender','dob','image')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'number','gender','dob','image')
        