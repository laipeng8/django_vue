# coding=gb2312
import time

from django.test import TestCase

# Create your tests here.
# Chinese   English
from translate import Translator

from translate import Translator

# 英语翻译中文
# translator = Translator(to_lang="chinese")
# translation = translator.translate("Do you believe")
# print(translation)
#
# # 中文翻译成英文
# translator = Translator(from_lang="chinese",to_lang="english")
# translation = translator.translate("开心快乐每一天！")
# print (translation)

class Get_translation:
    def get_str(self,from_lang,to_lang,in_str):
        translator = Translator(from_lang = from_lang,to_lang=to_lang)
        translation = translator.translate(f'{in_str}')
        return translation
class Translate:
    """函数重载，根据不同参数，调用不同方法"""
    def china_english(self,in_translation,to_translation,class_translation):
        pass
    def english_china(self,in_translation,to_translation,class_translation):
        pass