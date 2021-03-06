from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from django.http import Http404

class UserList(APIView):
	
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	
	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class UserRegister(APIView):
	
	def post(self, request, format=None):
		serializer = UserRegisterSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(
				serializer.data,
				status=status.HTTP_201_CREATED
			)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_vaild():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class DiaryList(APIView):
	
	def get_object(self, pk):
		try:
			return Diary.objects.get(pk=pk)
		except Diary.DoesNotExist:
			raise Http404

		def get(self, request, pk, format=None):
			diary= self.get_object(pk)
			serializer = DiarySerializer(diary)
			return Response(serializer.data)

		def post(self, request, format=None):
			image_data = self.context['request'].FILES
			diary = Diary.objects.create(**validated_data)
			return diary
