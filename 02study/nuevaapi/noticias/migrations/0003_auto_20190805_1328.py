# Generated by Django 2.1.7 on 2019-08-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='noticias.Autor'),
        ),
    ]
