from modeltranslation.translator import TranslationOptions, translator

from tests.models import Category


class CategoryOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Category, CategoryOptions)
