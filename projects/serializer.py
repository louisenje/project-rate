from rest_framework import serializers
from .models import Profile,webapps

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        
        fields = ('profile_pic','bio','phone_no','user','gender')

class WebappSerializer(serializers.ModelSerializer):
    class Meta:
        model=webapps

        fields=('title','main_picture','link','description','pub_date')