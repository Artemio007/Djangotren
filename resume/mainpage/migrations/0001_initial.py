# Generated by Django 4.1 on 2022-10-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='piprev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='оценка')),
                ('rev', models.TextField(verbose_name='отзыв')),
            ],
        ),
    ]
