# Generated by Django 4.1.7 on 2023-04-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electionapp', '0003_commentmodel_verify_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='presidentmodel',
            name='assignedto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
