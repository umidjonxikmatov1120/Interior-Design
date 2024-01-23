from modeltranslation import translator
from modeltranslation.translator import TranslationOptions
from pages.models import AboutModel, ServiceModel, ImagesModel, BlogModel


@translator.register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@translator.register(ImagesModel)
class ImagesTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@translator.register(ServiceModel)
class ServiceTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@translator.register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ['title', 'description']