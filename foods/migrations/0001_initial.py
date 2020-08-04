from django.db import migrations, models
import django.db.models.deletion
import foods.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_created_datetime', models.DateTimeField(auto_now_add=True,
                                                                verbose_name='Дата и время создания заказа')),
                ('delivery_datetime', models.DateTimeField(blank=True, null=True,
                                                           verbose_name='Дата и время доставки')),
                ('delivery_address', models.CharField(max_length=50, verbose_name='Адрес доставки')),
                ('status', models.CharField(choices=[(foods.models.StatusChoice['CREATED'], 'created'),
                                                     (foods.models.StatusChoice['DELIVERED'], 'delivered'),
                                                     (foods.models.StatusChoice['PROCESSED'], 'processed'),
                                                     (foods.models.StatusChoice['CANCELLED'], 'cancelled')],
                                            default=foods.models.StatusChoice['CREATED'],
                                            max_length=20, verbose_name='Статус')),
                ('product_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders',
                                                  to='foods.ProductSets', verbose_name='Набор продуктов')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders',
                                                to='foods.Recipient', verbose_name='Получатель')),
            ],
        ),
    ]
