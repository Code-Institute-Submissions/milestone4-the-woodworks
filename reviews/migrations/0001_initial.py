# Generated by Django 3.1 on 2020-10-01 19:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0003_remove_product_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(default='', max_length=800)),
                ('reviewer', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
    ]