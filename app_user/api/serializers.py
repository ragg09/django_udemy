from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirmation',
        ]
        extra_kwargs = {
            'password' : {
                'write_only': True,
            }
        }
     
    # overwrtie save function since we are now passing a custom field, the password_confirmation and email   
    def save(self):
        # password validator
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirmation']
        if(password != password_confirmation):
            raise serializers.ValidationError('Passwords are not the same')
        
        # email validator
        if(User.objects.filter(email=self.validated_data['email']).exists()):
            raise serializers.ValidationError('Email already exists')
        
        # actual registration
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        account.set_password(password)
        account.save()
        
        return account
        
        
            
            
    