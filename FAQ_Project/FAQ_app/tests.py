import pytest
from django.test import Client
from FAQ_app.models import FAQ
from django.core.cache import cache

"""Test that FAQ model saves and retrieves translations correctly."""


@pytest.mark.django_db(transaction=True)
def test_faq_model():

    faq = FAQ.objects.create(
        question="What is Django?", answer="Django is a web framework for Python."
    )
    faq.save()

    print("\nDEBUG: FAQs after model test:", list(FAQ.objects.values()))

    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework for Python."


"""Test API endpoint to fetch FAQs."""


@pytest.mark.django_db(transaction=True)
def test_faq_api():

    client = Client()
    FAQ.objects.all().delete()
    print("\nDEBUG: FAQs before insertion:", list(FAQ.objects.values()))
    faq = FAQ.objects.create(
        question="What is FAQ?", answer="Frequently Asked Questions."
    )
    faq.save()
    print("\nDEBUG: FAQs after insertion:", list(FAQ.objects.values()))

    response = client.get("/api/faqs/?lang=en")
    print("\nDEBUG: API Response:", response.json())

    assert response.status_code == 200
    assert len(response.json()) > 0, "API returned empty response!"
    assert (
        response.json()[0]["question"] == "What is FAQ?"
    ), f"Unexpected question: {response.json()[0]['question']}"


"""Test automatic translation handling."""


@pytest.mark.django_db
def test_translation_method():
    faq = FAQ.objects.create(question="Hello", answer="This is a test.")

    translation_hi = faq.get_translation("hi")
    translation_bn = faq.get_translation("bn")

    assert translation_hi["question"] != "Hello"
    assert translation_bn["question"] != "Hello"


"""Test if FAQs are stored in the cache correctly."""


@pytest.mark.django_db
def test_cache_mechanism():
    cache_key = "faq_test_cache"
    cache.set(
        cache_key, {"question": "Cached FAQ", "answer": "Cached Answer"}, timeout=60
    )

    cached_data = cache.get(cache_key)
    assert cached_data["question"] == "Cached FAQ"
    assert cached_data["answer"] == "Cached Answer"


"""Test API when no FAQs exist."""


@pytest.mark.django_db
def test_empty_faq_response():
    client = Client()
    response = client.get("/api/faqs/?lang=en")

    assert response.status_code == 200
    assert response.json() == []


"""Test if API returns translated FAQs correctly."""


@pytest.mark.django_db
def test_faq_api_with_translation():
    client = Client()
    faq = FAQ.objects.create(question="What is Django?", answer="A Python framework.")

    response_hi = client.get("/api/faqs/?lang=hi")
    assert response_hi.status_code == 200
    assert len(response_hi.json()) > 0
    assert (
        response_hi.json()[0]["question"] != "What is Django?"
    )  
