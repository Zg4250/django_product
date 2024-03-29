# Generated by Django 2.0 on 2019-03-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('addedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_item', to='my_app.User')),
                ('wishlist', models.ManyToManyField(related_name='wishlist', to='my_app.User')),
            ],
        ),
    ]
