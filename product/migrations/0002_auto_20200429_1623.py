# Generated by Django 3.0.5 on 2020-04-29 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurewatch',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.AddField(
            model_name='braceletfind',
            name='bezel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Bezel'),
        ),
        migrations.AddField(
            model_name='braceletfind',
            name='bracelet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Bracelet'),
        ),
        migrations.AddField(
            model_name='braceletfind',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material'),
        ),
        migrations.AddField(
            model_name='braceletfind',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size'),
        ),
        migrations.AddField(
            model_name='bezelfind',
            name='bezel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Bezel'),
        ),
        migrations.AddField(
            model_name='bezelfind',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material'),
        ),
        migrations.AddField(
            model_name='bezelfind',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size'),
        ),
    ]