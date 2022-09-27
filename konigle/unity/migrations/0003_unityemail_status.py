# Generated by Django 4.1.1 on 2022-09-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0002_remove_unityemail_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='unityemail',
            name='status',
            field=models.CharField(choices=[('subs', 'Subscribed'), ('unsubs', 'Unsubscribed')], default='subs', max_length=6),
        ),
    ]