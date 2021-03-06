# Generated by Django 3.0.6 on 2020-06-02 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ToppingsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isModel', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('pizzaType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.PizzaType')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.Size')),
                ('toppings', models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Topping')),
                ('toppingsType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.ToppingsType')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=64)),
                ('totalPrice', models.FloatField()),
                ('pizzas', models.ManyToManyField(blank=True, related_name='in_order', to='orders.Pizza')),
            ],
        ),
    ]
