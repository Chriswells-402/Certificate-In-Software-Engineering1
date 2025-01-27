# Generated by Django 4.2 on 2023-04-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=22)),
                ('lastname', models.CharField(max_length=22)),
                ('gender', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=22)),
                ('state', models.CharField(max_length=22)),
                ('town', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=22)),
                ('zipcode', models.CharField(max_length=22)),
                ('num1', models.IntegerField(blank=True, default=0, null=True)),
                ('num2', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
