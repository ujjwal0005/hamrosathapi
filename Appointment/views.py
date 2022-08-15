from distutils.log import error
from django.contrib.auth import logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Appointment.serializer import AppointmentSerializer
from .models import Appointment, User
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_appointment(request):
    data = request.data.copy()
    data.update({'user':request.user.id})
    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_appointment(request,id):
    try:
        print(request.user)
        data = request.data.copy()
        if request.user.is_doctor:
            appointment = Appointment.objects.get(id=id,doctor=request.user)
        else:
            appointment = Appointment.objects.get(id=id,user=request.user)
            if data.get('is_verified'):
                data.pop('is_verified')
        print(data)
        serializer = AppointmentSerializer(instance=appointment,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_appointment(request):
    appointment = Appointment.objects.filter(user=request.user)
    return Response(AppointmentSerializer(appointment,many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointment(request):
    if request.user.is_doctor:
        appointment = Appointment.objects.filter(doctor=request.user,is_cancelled=False)
        return Response(AppointmentSerializer(appointment,many=True).data)
    return Response({'detail':'Access denied'},status= status.HTTP_403_FORBIDDEN)