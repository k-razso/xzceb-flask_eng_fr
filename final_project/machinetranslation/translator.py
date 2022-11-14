import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Following code follows cloud.ibm.com language translator API documentation
# Creates an instance of IBM Watson language translator with personal credentials

authenticator = IAMAuthenticator('SRE83uTbWF7bFCrHeoOtlnbc1Mdtgjuhk-jcTSNLJ40W')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/1e35511b-e05f-4d98-98c4-05aa4a2ac83b')


def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation["translations"[0]"translation"]


def frenchToEnglish(frenchText):
    #write the code here
    translatedText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return translation["translations"[0]"translation"]

englishToFrench(Hello)
