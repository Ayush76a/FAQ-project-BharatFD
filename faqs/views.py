from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')


    cache_key = f"faqs_{lang}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    faqs = FAQ.objects.all()
    serialized_faqs = FAQSerializer(faqs, many=True).data


    for faq in serialized_faqs:
        faq['question'] = faq.get(f'question_{lang}', faq['question'])


    cache.set(cache_key, serialized_faqs, timeout=60 * 15)  # 15 minutes cache

    return Response(serialized_faqs)
