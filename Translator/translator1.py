# This script uses googletrans module
# It outputs the translation in the same file as source file

from googletrans import Translator

translator = Translator()

with open('test.txt', mode='r+') as file:
	contents = file.readlines()

	for item in contents:
		if item != contents[-1]:
			result = translator.translate(dest='ja', text=item[:-1])
			file.write('\n')
			file.write(f'The translation of \"{item[:-1]}\" is \"{result.text}\"')
		else:
			result = translator.translate(dest='ja', text=item)
			file.write('\n')
			file.write(f'The translation of \"{item}\" is \"{result.text}\"')


''' Testing translator
# result = translator.translate(dest='ja', text='안녕하세요.')
# print(type(result))
# print(result)
# print(result.text)
'''