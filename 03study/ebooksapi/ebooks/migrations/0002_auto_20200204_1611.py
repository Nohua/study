# Generated by Django 2.1.7 on 2020-02-04 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='descipcion',
            new_name='descripcion',
        ),
    ]