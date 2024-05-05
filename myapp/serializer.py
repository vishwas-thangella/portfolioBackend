from rest_framework import serializers
from myapp import models

class Homeserializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeData
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'
    
    def get_image_url(self,obj):
        request = self.context.get("request")
        image_uri = obj.fingerprint.url
        return request.build_absolute_uri(image_uri)
    
class Projectserialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'

    def get_image_url(self,obj):
        request = self.context.get("request")
        image_uri = obj.fingerprint.url
        return request.build_absolute_uri(image_uri)
    
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'