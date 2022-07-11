from translate import Translator

translator = Translator(to_lang="de")

try:
    with open('.\\Documents\\translate.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)

        with open('.\\Documents\\translatedText.txt', mode='w') as translatedFile:
            translatedFile.write(translation)
except FileNotFoundError as err:
    print('File Not Found')