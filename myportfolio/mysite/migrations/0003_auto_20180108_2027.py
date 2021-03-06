# Generated by Django 2.0.1 on 2018-01-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/skill/')),
                ('is_on_main', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/about/'),
        ),
    ]
