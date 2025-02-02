from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

translator = Translator()


class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question in Hindi"), blank=True, null=True)
    answer_hi = RichTextField(_("Answer in Hindi"), blank=True, null=True)
    question_bn = models.TextField(_("Question in Bengali"), blank=True, null=True)
    answer_bn = RichTextField(_("Answer in Bengali"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest="hi").text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest="bn").text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest="bn").text
        super().save(*args, **kwargs)

    def get_translation(self, lang):
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        translation = {
            "en": {"question": self.question, "answer": self.answer},
            "hi": {"question": self.question_hi, "answer": self.answer_hi},
            "bn": {"question": self.question_bn, "answer": self.answer_bn},
        }.get(lang, {"question": self.question, "answer": self.answer})

        cache.set(cache_key, translation, timeout=3600)
        return translation

    def __str__(self):
        return self.question
