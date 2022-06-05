""" English and French translator by using IBM AI """
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

""" get the translator instance"""
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

def englishToFrench(english_text):
    """takes in English text and returns French text"""
    trans_result = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = trans_result['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """takes in French text and returns English text"""
    trans_result = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = trans_result['translations'][0]['translation']
    return english_text

#test_e2f = englishToFrench("Good Morning!")
#print(test_e2f)
#test_f2e = frenchToEnglish("Bonjour!")
#print(test_f2e)
