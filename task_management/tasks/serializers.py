from rest_framework import serializers
from .models import CustomUser as User, TaskModel as Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Ensure the password is hashed before saving the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        # Validate the status and completed_at logic
        if data.get('status') == 'Completed' and not data.get('completed_at'):
            raise serializers.ValidationError(
                "A task marked as 'Completed' must have a 'completed_at' timestamp."
            )
        if data.get('status') != 'Completed' and data.get('completed_at'):
            raise serializers.ValidationError(
                "'completed_at' should be None unless the task is 'Completed'."
            )
        return data
        