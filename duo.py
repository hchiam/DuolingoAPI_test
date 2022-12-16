import duolingo

lingo = duolingo.Duolingo('your_username_here', 'your_password_here')


def get_word_and_pronunciation(word):
    return word['word_string'] + '\t' + word['normalized_string']


lang = 'hi'
vocab = lingo.get_vocabulary(language_abbr=lang)['vocab_overview']
output = '\n'.join(list(map(get_word_and_pronunciation, vocab))) + '\n'

print(output)

f = open("duolingo_api_output.txt", "w")
f.write(output)
f.close()
