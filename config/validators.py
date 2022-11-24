from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def today_validate(date):
    if date < timezone.now().date():
        print(date, timezone.now().date())
        raise ValidationError(_("Iltimos kunni to'g'ri tanlang, ushbu sana o'tib bo'lgan!"))
