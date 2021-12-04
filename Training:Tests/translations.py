from googletrans import Translator
translator = Translator()
translation = translator.translate('안녕하세요')
print(translation.src)
print(translation.dest)
print(translation.text)
