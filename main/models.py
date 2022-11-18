from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator


class RecommendationDestinationsModel(models.Model):
    image = models.ImageField(upload_to='destinations/', verbose_name=_('images'))
    where_to = models.CharField(max_length=50, verbose_name=_('where to'))
    date = models.DateField(auto_now=False)
    direct_flight = models.CharField(max_length=50, verbose_name=_('direct flight'))
    company_logo = models.ImageField(upload_to='company-logo/', verbose_name=_('company logo'))
    price = models.PositiveIntegerField(verbose_name=_('price'))

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
    price = models.PositiveIntegerField(verbose_name=_('price'))

    def __str__(self):
        return self.where_to

    class Meta:
        verbose_name = _('cheap flight')
        verbose_name_plural = _('cheap flights')
        ordering = ('-id',)


class MessageModel(models.Model):
    email = models.EmailField(verbose_name=_('email'), validators=[EmailValidator()])
    text = models.TextField(verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('-id',)


class AirCompanyModel(models.Model):
    image = models.ImageField(upload_to='air-company/', verbose_name=_('image of air companies'))
    name = models.CharField(max_length=50, verbose_name=_('name of air companies'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('air company')
        verbose_name_plural = _('air companies')
        ordering = ('-id',)


class TerminalModel(models.Model):
    name = models.CharField(max_length=3, verbose_name=_('name of terminal'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('terminal')
        verbose_name_plural = _('terminals')
        ordering = ('-id',)


class FlightPlaceModel(models.Model):
    destination = models.CharField(max_length=60, verbose_name=_('destination'))

    def __str__(self):
        return self.destination

    class Meta:
        verbose_name = _('flight destination')
        verbose_name_plural = _('flight destinations')
        ordering = ('-id',)