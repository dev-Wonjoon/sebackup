from django.db import models

class User(models.Model):
	user_seq = models.AutoField(primary_key=True)
	user_id = models.EmailField(max_length=32, unique=True)
	user_pw = models.CharField(max_length=512)
	user_nickname = models.CharField(max_length=24)

class Diary(models.Model):
	diary_seq = models.AutoField(primary_key=True)
	diary_title = models.CharField(max_length=64)
	diary_cotent = models.TextField()
	diary_status = models.IntegerField(default=1)
	diary_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class DiaryPost(models.Model):
	dp_seq = models.AutoField(primary_key=True)
	dp_created = models.DateTimeField(auto_now_add=True)
	dp_updated = models.DateTimeField(auto_now=True)
	dp_diary_pk = models.ForeignKey(Diary, on_delete=models.DO_NOTHING)

class DiaryFile(models.Model):
	df_seq = models.AutoField(primary_key=True)
	df_filepath = models.ImageField(upload_to="diary_images/", null=True, blank=True)
	df_filename = models.CharField(max_length=64)
	df_upload_date = models.DateTimeField(auto_now_add=True)
	df_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	df_diary_pk = models.ForeignKey(Diary, on_delete=models.DO_NOTHING)

class AutoUpdate(models.Model):
	au_seq = models.AutoField(primary_key=True)
	au_before = models.CharField(max_length=24)
	au_after = models.CharField(max_length=24)
	au_registed = models.DateTimeField(auto_now_add=True)
	au_updated = models.DateTimeField(auto_now=True)
	au_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class UserLoginLog(models.Model):
	ull_seq = models.AutoField(primary_key=True)
	ull_platform = models.CharField(max_length=16)
	ull_last_login = models.DateTimeField(auto_now_add=True)
	ull_user_pk = models.ForeignKey(User, on_delete=models.DO_NOTHING)
