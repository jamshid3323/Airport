from django.db import models
from django.utils.translation import gettext_lazy as _
from main.models import FlightModel


class SeatModel(models.Model):
    CLASS = (
        ('E', _('Ekonom')),
        ('B', _('Biznes')),
        ('P', _('Premum'))
    )
    name = models.CharField(max_length=1, choices=CLASS, verbose_name=_('seat class name'))
    number = models.CharField(max_length=2, verbose_name=_('seat number'))

    def __str__(self):
        return f"num:{self.number}, class:{self.name}"

    class Meta:
        verbose_name = _('seat')
        verbose_name_plural = _('seats')
        ordering = ('-id',)


class TicketModel(models.Model):
    flight = models.ForeignKey(FlightModel, on_delete=models.RESTRICT, related_name='flight', verbose_name=_('flights'))
    seat = models.ForeignKey(SeatModel, on_delete=models.RESTRICT, related_name='seat', verbose_name=_('ticket seat'))
    price = models.PositiveIntegerField(max_length=6, verbose_name=_('ticket price'))

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')
        ordering = ('-id',)
