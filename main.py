from googletrans import Translator
translator = Translator()
language = input('Idioma: Escribe es para Español, en minúsculas.\nLanguage: Write en for English, in lowercase\n')
if language == 'es':
    while True:
        text = input('Introduce el texto\n')
        languages = ['ja', 'et', 'tl', 'hu', 'hmn', 'ga', 'ku', 'ps', 'gd', 'eo', 'af', 'az', 'ny', language]
        for i in range(len(languages)):
            try:
                text = (translator.translate(text, dest=languages[i], src=languages[i-1])).text
            except: 
                text = (translator.translate(text, dest=languages[i], src=language)).text
                
        print(text)
        quit = input('¿Quieres salir?\n')
        if quit == 'Si' or quit == 'si' or quit == 'Sí' or quit == 'sí':
            break
elif language == 'en':
    while True:
        text = input('Input text\n')
        languages = ['ja', 'et', 'tl', 'hu', 'hmn', 'ga', 'ku', 'ps', 'gd', 'eo', 'af', 'az', 'ny', language]
        for i in range(len(languages)):
            try:
                text = (translator.translate(text, dest=languages[i], src=languages[i-1])).text
            except: 
                text = (translator.translate(text, dest=languages[i], src=language)).text
                
        print(text)
        quit = input('Do you want to quit?\n')
        if quit == 'yes' or quit == 'Yes':
            break