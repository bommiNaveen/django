from django.shortcuts import render
from .serializers import studentserializers
from .models import student
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def studentdetails(request):
    queryset = student.objects.all() #query set
    serializer = studentserializers(queryset,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_student(request):
    queryset = student.objects.all()
    serializer = studentserializers(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)

@api_view(['post'])
def update_student(request,id):
    queryset = student.objects.get(id = id)
    serializer = studentserializers(instance=queryset,data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)

@api_view(['DELETe'])
def delete_student(request,id):
    queryset = student.objects.get(id = id)
    queryset.delete()
    return Response('book is delete')


# class studentViewSet(viewsets.ModelViewSet):
#     serializer_class = studentserializers
#     queryset = student.objects.all()