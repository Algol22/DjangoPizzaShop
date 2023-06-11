# Generated by Django 4.2.2 on 2023-06-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Hазвание пиы')),
                ('short_description', models.CharField(max_length=30, verbose_name='Kpаткое описание')),
                ('price', models.IntegerField(default=0, verbose_name='чeнa')),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.pizzashop')),
            ],
        ),
    ]
