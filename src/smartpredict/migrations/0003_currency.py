# Generated by Django 2.1.5 on 2019-04-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpredict', '0002_auto_20190208_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('USD', 'US Dollar'), ('GBP', 'GB Pound')], default='EUR', max_length=10)),
            ],
        ),
    ]
