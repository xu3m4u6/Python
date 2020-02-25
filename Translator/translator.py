# This script uses translate module 
# It outputs the translation in seperate files

from translate import Translator

translator= Translator(from_lang = 'autodetect', to_lang='ja')

with open('./test.txt', mode='r') as file:
	contents = file.readline()

	while contents:
		result = translator.translate(contents)
		with open('./text-ja2.txt', mode='a') as new:
			new.write('\n')
			new.write(result)

		contents = file.readline()



''' Testing translator
print(translator.from_lang)
result = translator.translate("This is a pen.")
print(result)
print(type(result))
'''