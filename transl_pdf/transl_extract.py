'''
Translator Extractor
Yokyu Liu
'''
from google_trans_new import google_translator
import textract

class TranlsExtract:
    def transl_file(file):
        #File Extraction
        text = textract.process(file)

        #Translate extracted text
        tr = google_translator()
        translate_text = tr.translate(text, lang_tgt='zh-tw')


        return translate_text

    def transl_text(text):
        #Translate form Text Area
        tr = google_translator()
        translate_text = tr.translate(text, lang_tgt='zh-tw')
        return translate_text