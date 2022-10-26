from django.db import models
from django.utils.translation import gettext_lazy as _


class RecommendationDestinationsModel(models.Model):
    image = models.ImageField(upload_to='destinations/', verbose_name=_('images'))
    where_to = models.CharField(max_length=50, verbose_name=_('where to'))
    date = models.DateField(auto_now=False)
    direct_flight = models.CharField(max_length=50, verbose_name=_('direct flight'))
    company_logo = models.ImageField(upload_to='company-logo/', verbose_name=_('company logo'))
    price = models.PositiveIntegerField(max_length=4, verbose_name=_('price'))

    def __str__(self):
        return self.where_to

    class Meta:
        verbose_name = _('destination')
        verbose_name_plural = _('destinations')
        ordering = ('-id',)


class DiscoverModel(models.Model):
    image = models.ImageField(upload_to='discover/', verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('discover')
        verbose_name_plural = _('discovers')
        ordering = ('-id',)


class CheapFlightModel(models.Model):
    image = models.ImageField(upload_to='cheap-flight/', verbose_name=_('images'))
    where_to = models.CharField(max_length=50, verbose_name=_('where to'))
    date = models.DateField(auto_now=False)
    direct_flight = models.CharField(max_length=50, verbose_name=_('direct flight'))
    company_logo = models.ImageField(upload_to='company-logo/', verbose_name=_('company logo'))
    price = models.PositiveIntegerField(max_length=4, verbose_name=_('price'))

    def __str__(self):
        return self.where_to

    class Meta:
        verbose_name = _('cheap flight')
        verbose_name_plural = _('cheap flights')
        ordering = ('-id',)
