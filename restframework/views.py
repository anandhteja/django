from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from restframework import serializers

from restframework.serializers import Student_serializer

from admissions.models import Student
# Create your views here.


#read
@api_view()
def rest_read(request):
    stu=Student.objects.all()
    serializer=Student_serializer(stu, many=True)

    return Response({'status':200,'payload':serializer.data})





#create
@api_view(['POST'])
def rest_create(request):
    
    serializer=Student_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({'status':200,'payload':serializer.data})






#update
@api_view(['POST'])
def rest_update(request,id):
    stu=Student.objects.get(id=id)
    
    serializer=Student_serializer(instance=stu,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({'status':200,'payload':serializer.data})






#delete
@api_view(['DELETE'])
def rest_delete(request,id):
    stu=Student.objects.get(id=id)
    
    
    stu.delete()

    return Response('Deleted successfully')