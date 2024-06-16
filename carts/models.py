from django.db import models

from users.models import User
from events.models import Event

class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.events_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Пользователь')
    event = models.ForeignKey(to=Event,on_delete=models.CASCADE, verbose_name = 'Мероприятия')
    quantity = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    objects = CartQueryset().as_manager()

    def events_price(self):
        return round(self.event.sell_price() * self.quantity, 2)


    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.event.name} | Количество {self.quantity}'
    

    