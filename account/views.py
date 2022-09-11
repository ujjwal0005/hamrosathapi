from django.contrib.auth import logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import DoctorProfileSerializer, DoctorSerializer, RegisterSerializer,updateUserSerializer,UserSerializer
from .models import User
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'counseller':user.is_doctor})


obtain_auth_token = ObtainAuthToken.as_view()

@api_view(['POST'])
def create_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user=request.user
    serializer = updateUserSerializer(instance=user,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def _logout(request):
    logout(request)
    return Response({
        'message':'logout successfully'
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def doctor_profileedit(request):
    user = request.user
    if not user.is_doctor:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = DoctorProfileSerializer(instance=user.doctor_profile,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_profile(request):
    user = request.user
    if not user.is_doctor:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = DoctorProfileSerializer(user.doctor_profile)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors(request):
    doctors = User.objects.prefetch_related('doctor_profile').filter(is_doctor=True,doctor_profile__is_verified = True)
    # print(doctors.query)
    serializer = DoctorSerializer(doctors,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getdoctorID(request,id):
    doctors = User.objects.prefetch_related('doctor_profile').filter(is_doctor=True,id=id,doctor_profile__is_verified = True).first()
    serializer = DoctorSerializer(doctors)
    return Response(serializer.data)
    


