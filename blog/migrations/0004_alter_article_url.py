# Generated by Django 4.2.4 on 2023-09-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_date_alter_article_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True, verbose_name='Доп.источник'),
        ),
    ]