from django.db import models

import locale

class Event(models.Model):
    name = models.CharField(max_length=150, unique=True )
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    place = models.CharField(max_length=150, unique=True )
    capacity = models.PositiveIntegerField(default=0)
    remaining_capacity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)

    class Meta:
        db_table = 'Event'
        
    def __str__(self):
        return self.name
    
    def formatted_start_time(self):
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        formatted_date = self.start_time.strftime('%-d %B %Y')
        locale.setlocale(locale.LC_TIME, '')
        return formatted_date

