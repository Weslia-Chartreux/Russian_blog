from django.utils import timezone


def year(request):
    year_now = timezone.now().strftime('%Y')
    return {
        'year_now': year_now,
    }



