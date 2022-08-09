from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from Blog.serializer import CommentSerializer,BlogSerializer
from account.models import User
from Blog.models import Blog,Comment

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    data = request.data
    data.update({'user':request.user.id})
    serializer = BlogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH','GET','DELETE'])
@permission_classes([IsAuthenticated])
def update_blog(request,id):
    try:
        blog = Blog.objects.filter(id=id,user=request.user)
        if request.method=='GET':
            blog=blog.latest('id')
            serializer = BlogSerializer(blog)
            return Response(serializer.data,status=status.HTTP_200_OK)        
        elif request.method=='PATCH':
            blog=blog.latest('id')
            serializer = BlogSerializer(data=request.data,instance=blog,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        else:
            blog.delete()
            return Response(status=status.HTTP_200_OK)     
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail':e.args},status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_userblog(request):
    blog = Blog.objects.filter(user=request.user)
    serializer = BlogSerializer(blog,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_blogs(request):
    blog = Blog.objects.filter(is_verified=True)
    serializer = BlogSerializer(blog,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    