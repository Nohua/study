# Generated by Django 2.1.7 on 2020-02-04 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0002_auto_20200204_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resena',
            name='autor_resena',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
