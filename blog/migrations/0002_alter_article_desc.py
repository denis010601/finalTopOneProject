# Generated by Django 4.2.4 on 2023-09-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(),
        ),
    ]
