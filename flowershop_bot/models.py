from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    phone_number = PhoneNumberField(verbose_name='Номер клиента',
                                    region='RU',
                                    null=True,
                                    blank=True)

    USER_ROLE_CHOICES = [
        ("C", "Client"),
        ("D", "Delivery man"),
        ("F", "Florist"),
    ]
    role = models.CharField(verbose_name='Роль пользователя',
                            max_length=12,
                            choices=USER_ROLE_CHOICES,
                            default='C')


class Flower(models.Model):
    name = models.CharField(verbose_name='Название цветка',
                            max_length=50)
    color = models.CharField(verbose_name='Цвет',
                             max_length=50,
                             blank=True,
                             null=True)


class Occasion(models.Model):
    name = models.CharField(verbose_name='Повод',
                            max_length=50,
                            blank=True,
                            null=True)


class Bouqet(models.Model):
    occasion = models.ForeignKey(Occasion,
                                 verbose_name='Повод букета',
                                 related_name='bouqets',
                                 on_delete=models.CASCADE)
    flowers = models.ManyToManyField(Flower,
                                     verbose_name='Цветы в букете',
                                     related_name='bouqets',
                                     db_index=True)
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание букета')
    image = models.ImageField(verbose_name='Фото букета',
                              upload_to='images',
                              null=True)


class Order(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Пользователи',
                             related_name='orders',
                             on_delete=models.CASCADE)
    bouqet = models.ForeignKey(Bouqet,
                               verbose_name='Букет в заказе',
                               related_name='orderes',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    recipient_name = models.CharField(verbose_name='Имя получателя',
                                      max_length=250,
                                      null=True,
                                      blank=True)
    delivery_address = models.CharField(verbose_name='Адрес доставки',
                                        max_length=250,
                                        null=True,
                                        blank=True)
    delivery_date = models.DateField(verbose_name='Дата доставки',
                                     null=True,
                                     blank=True)
    delivery_time = models.TimeField(verbose_name='Время доставки',
                                     null=True,
                                     blank=True)

    ORDER_STATUS_CHOICES = [
        ("P", "Placed"),
        ("W", "Waiting for call"),
        ("D", "Delivered"),
    ]
    status = models.CharField(verbose_name='Статус заказа',
                              max_length=16,
                              choices=ORDER_STATUS_CHOICES)
