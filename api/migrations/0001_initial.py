# Generated by Django 4.0.4 on 2022-05-16 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('diary_seq', models.AutoField(primary_key=True, serialize=False)),
                ('diary_title', models.CharField(max_length=64)),
                ('diary_cotent', models.TextField()),
                ('diary_status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_seq', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.EmailField(max_length=32, unique=True)),
                ('user_pw', models.CharField(max_length=512)),
                ('user_nickname', models.CharField(max_length=24)),
                ('user_profile_img', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('ull_seq', models.AutoField(primary_key=True, serialize=False)),
                ('ull_platform', models.CharField(max_length=16)),
                ('ull_last_login', models.DateTimeField(auto_now_add=True)),
                ('ull_user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryPost',
            fields=[
                ('dp_seq', models.AutoField(primary_key=True, serialize=False)),
                ('dp_created', models.DateTimeField(auto_now_add=True)),
                ('dp_updated', models.DateTimeField(auto_now=True)),
                ('dp_diary_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.diary')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryFile',
            fields=[
                ('df_seq', models.AutoField(primary_key=True, serialize=False)),
                ('df_filepath', models.CharField(max_length=256)),
                ('df_filename', models.CharField(max_length=64)),
                ('df_upload_date', models.DateTimeField(auto_now_add=True)),
                ('df_diary_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.diary')),
                ('df_user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='diary_user_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user'),
        ),
        migrations.CreateModel(
            name='AutoUpdate',
            fields=[
                ('au_seq', models.AutoField(primary_key=True, serialize=False)),
                ('au_before', models.CharField(max_length=24)),
                ('au_after', models.CharField(max_length=24)),
                ('au_registed', models.DateTimeField(auto_now_add=True)),
                ('au_updated', models.DateTimeField(auto_now=True)),
                ('au_user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
        ),
    ]
