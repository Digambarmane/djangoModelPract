# Generated by Django 4.1 on 2023-02-13 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auther_bname_alter_auther_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='page',
            field=models.IntegerField(null=True),
        ),
    ]
