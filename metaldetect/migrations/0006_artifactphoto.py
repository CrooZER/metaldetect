# Generated by Django 4.0.2 on 2022-02-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metaldetect', '0005_rename_atrifacttype_artifacttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='artifacts')),
                ('description', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
