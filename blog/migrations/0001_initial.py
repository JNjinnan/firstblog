# Generated by Django 3.2.6 on 2021-08-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='新闻标题', max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.CharField(default='新闻正文', max_length=500)),
            ],
        ),
    ]
