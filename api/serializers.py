from rest_framework import serializers
from .models import User, Diary, DiaryPost, DiaryFile
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_seq', 'user_id', 'user_pw', 'user_nickname')

		validators = [
			UniqueTogetherValidator(
				queryset = User.objects.all(),
				fields=['user_id']
			)
		]

	def post(self, validated_data, instance):
		instance.user_pw = validated_data.get('user_pw', instance.user_id)
		instance.user_nickname = validated_data.get('user_nickname', instance.user_nickname)
		instance.user_profile_img = validated_data.get('user_profile_img', instance.user_profile_img)
		return instance
		
class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_seq', 'user_id', 'user_pw', 'user_nickname')
	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		return user


class DiarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Diary
		fields = ('diary_seq', 'diary_title', 'diary_content', 'diary_status', 'diary_user_pk')
		

	def create(self, validated_data):
		return Diary.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.diary_title = validated_data.get('diary_title', instance.diary_title)
		instance.diary_content = validated_data.get('diary_content', instance.diary_content)
		instance.diary_status = validated_data.get('diary_status', instance.diary_status)
		instance.save()
		return instance

class DiaryPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiaryPost
		fields = ('dp_seq', 'dp_created', 'dp_updated', 'dp_diary_pk')

	def create(self, validated_data):
		return DiaryPost.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.dp_updated = validated_data.get('dp_updated', instance.dp_updated)
		instance.save()
		return instance
class DiaryFileSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiaryFile
		fields = ('df_seq', 'df_filepath', 'df_filename', 'df_upload_date', 'df_user_pk', 'df_diary_pk')

		def create(self, validated_data):
			return DiaryFile.objects.create(**validated_data)
		
		def update(self, instance, validated_data):
			instance.df_filename = validated_data.get('df_filename', instance.df_filename)
			instance.df_diary_pk = validated_data.get('df_diary_pk', instance.df_diary_pk)
			instance.save()
			return instance

class AuthLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserLoginLog
		fields = ('ull_seq', 'ull_platform', 'ull_last_login', 'ull_user_pk')

		def create(self, validated_data):
			return UserLoginLog.objects.create(**validated_data)
