from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from restframework import serializers

from restframework.serializers import Student_serializer

from admissions.models import Student

from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin



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







class Studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=Student_serializer
    def get(self, request):
        return self.list(request)
  
    def post(self, request):
        return self.create(request)





class Studentdelupdate(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=Student_serializer
    def get(self, request,**kwargs):
        return self.retrieve(request,**kwargs)

    def put(self, request,**kwargs):
        return self.update(request,**kwargs)


    def delete(self, request,**kwargs):
        return self.destroy(request,**kwargs)





class Studentlistapi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer




class Studentcreateapi(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer



class Studentretrieveapi(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer





class Studentupdateapi(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer






class Studentdestroyapi(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer





class Studentlc(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer




class Studentru(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer




class Studentrd(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer






class Studentrud(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer