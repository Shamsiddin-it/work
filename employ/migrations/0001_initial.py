# Generated by Django 4.2.16 on 2024-11-06 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/category')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/region')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/user')),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images/work')),
                ('video', models.FileField(blank=True, max_length=255, null=True, upload_to='static/videos/work')),
                ('address', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.user')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('HIRED', 'hired'), ('REJECTED', 'rejected'), ('IN PROCESS', 'in process')], max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.user')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.work')),
            ],
        ),
    ]
