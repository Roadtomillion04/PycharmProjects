from translate import Translator
translator = Translator(to_lang="ja")

with open("test.txt", mode="r") as my_file:
	text = my_file.read()
	translation = translator.translate(text)
	print(translation)

	with open('translated.txt', mode = "w") as new_file:
		new_file.write(translation)