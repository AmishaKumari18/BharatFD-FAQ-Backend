from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer


def home_view(request):
    """Returns a JSON response for the homepage."""
    return JsonResponse(
        {"message": "Welcome to the FAQ API! Use /api/faqs/ to get FAQs."}
    )


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        faqs = FAQ.objects.all().order_by("-id")
        data = [faq.get_translation(lang) for faq in faqs]
        return Response(data)
