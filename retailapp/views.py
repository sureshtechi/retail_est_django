from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import retail_info

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = retail_info.objects.all()
        serializer = TaskSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = TaskSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_200_OK)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreatePost(APIView):
# 	permission_classes = [permissions.IsAuthenticated]

# 	def post(self, request, format=None):
# 		print(request.data)
# 		serializer = TaskSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_200_OK)
# 		else:
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def Create(request):
# 	serializer = TaskSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()
# 		print(serializer.data)
# 		return Response(serializer.data)
# 	else:
# 		print(serializer.errors)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def RetailList(request):
# 	tasks = retail_info.objects.all().order_by('-email')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)
	

# def service_worker(request):
#     sw_path = settings.BASE_DIR / "retail/build" / "sw.js"
#     response = HttpResponse(open(sw_path).read(), content_type='application/javascript')
#     return response

