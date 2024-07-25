from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app1.models import *
from app1.serializers import *
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def index(request):
    return Response({"ss":"helio   bro "})


@api_view(['GET','POST'])
def Studentcreate(request):
    if request.method=='GET':
        query_set=Student.objects.all()
        serializer=Studentserializer(query_set,many=True)
        return Response({"status":True,"data":serializer.data})
    elif request.method=='POST':
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response(serializer.errors)

@api_view(['GET','PUT','PATCH','DELETE'])
def Studentupdate(request,pk=None):
    if request.method=='GET':
        if pk:
            query_set=get_object_or_404(Student,pk=pk)
        else:
            query_set=Student.objects.all()
        
        serializers=Studentserializer(query_set)
        return Response(serializers.data)
    
    elif request.method=='PUT':
        query_set=get_object_or_404(Student,pk=pk)
        serializers=Studentserializer(query_set,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method=='PATCH':
        query_set=get_object_or_404(Student,pk=pk)
        serializers=Studentserializer(query_set,request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method=='DELETE':
        query_set=get_object_or_404(Student,pk=pk)
        query_set.delete()
        return Response({"message":"delete"})
        


class StudentAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            query_set=get_object_or_404(Student,pk=pk)
            serializer=Studentserializer(query_set)
        else:
            query_set=Student.objects.all()
            serializer=Studentserializer(query_set,many=True)

        return Response (serializer.data) 
    
    def post(self,request):
        serializer=Studentserializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put (self,request,pk):
        query_set=Student.objects.get(pk=pk)
        serializer=Studentserializer(query_set,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def patch (self,request,pk):
        query_set=get_object_or_404(Student,pk=pk)
        serializer=Studentserializer(query_set,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
        query_set=get_object_or_404(Student,pk=pk)
        query_set.delete()
        return Response("delete suceesfully ")



# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list')

        if not subject or not message or not recipient_list:
            return Response({'error': 'Subject, message, and recipient list are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Ensure recipient_list is a list
            if isinstance(recipient_list, str):
                recipient_list = [recipient_list]

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return Response({'error': 'Failed to send email.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success': 'Email sent successfully.'}, status=status.HTTP_200_OK)

