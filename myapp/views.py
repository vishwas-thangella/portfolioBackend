from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp import models
from .serializer import Homeserializer,SkillSerializer,Projectserialzer,EducationSerializer,ExperienceSerializer,ContactSerializer

# Create your views here.

@api_view(["GET"])
def Home(request):
    homedata = models.HomeData.objects.all()
    skills = models.Skills.objects.all()
    projects = models.Projects.objects.all()
    homeserializerData = Homeserializer(homedata,many = True)
    skillserializerData = SkillSerializer(skills,many=True,context={"request":request})

    data = {
        'homedata':homeserializerData.data[0],
        'skills':skillserializerData.data,
    }

    return Response(data)

@api_view(["GET"])
def Projects(request):
    projects = models.Projects.objects.all()
    serializedData = Projectserialzer(projects,many=True,context={"request":request})
    return Response(serializedData.data)


@api_view(["GET"])
def About(request):
    education = models.Education.objects.all()
    experiences = models.Experience.objects.all()
    serializedEducation = EducationSerializer(education,many=True)
    serialzedExperiences = ExperienceSerializer(experiences,many=True)
    data = {
        'education' : serializedEducation.data,
        'experiences' : serialzedExperiences.data
    }
    return Response(data)

@api_view(["POST"])
def Contact(request):
    if request.method == "POST":
        data = request.data
        contact = ContactSerializer(data=data)
        if contact.is_valid():
            contact.save()
            return Response({'success':True})
        else:
            return Response({'success':False})