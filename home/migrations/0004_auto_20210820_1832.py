# Generated by Django 3.1.13 on 2021-08-20 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210811_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='item',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='comprador',
            name='usuario_comprador',
        ),
        migrations.AddField(
            model_name='comprador',
            name='contraseña',
            field=models.CharField(default=1234, max_length=15, verbose_name='Contraseña'),
        ),
        migrations.AddField(
            model_name='comprador',
            name='imagen',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='comprador',
            name='tipo_documento',
            field=models.CharField(choices=[('TI', 'Tarjeta de identidad'), ('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=2, verbose_name='Tipo de documeto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='disponibilidad',
            field=models.CharField(choices=[('S', 'En stock'), ('N', 'Agotado')], default='S', max_length=1, verbose_name='Disponibilidad'),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='documento',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='No. de documento'),
        ),
        migrations.AlterField(
            model_name='envio',
            name='pedido',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='comprador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.comprador'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(verbose_name='Cantidad en inventario'),
        ),
        migrations.DeleteModel(
            name='Usuario_comprador',
        ),
    ]
