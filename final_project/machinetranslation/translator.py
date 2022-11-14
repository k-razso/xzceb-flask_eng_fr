"""this module implements an instance of IBM language translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

""" Following code follows cloud.ibm.com language translator API documentation
 Creates an instance of IBM Watson language translator with personal credentials """

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text):
    """ Function defining a way to translate a given english text into french"""
    translated_text = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translated_text["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """ Function defining a way to translate a given french text into english"""
    translated_text = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translated_text["translations"][0]["translation"]
    return english_text
