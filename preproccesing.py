from nltk.stem import *
from nltk import word_tokenize
import pymorphy2

from nltk.stem.snowball import SnowballStemmer

def stemmerRus(texts):
    """ДЛЯ РУССКОГО ЯЗЫКА
    Функция принимающая список текстов и возвращающая его после стемминга
    texts - исходный текст
    stem_texts - список текстов со стеммингом
    """
    stemmer = SnowballStemmer("russian")
    stem_texts = []
    for text in texts:
        tokens = text.split()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        stem_texts.append(' '.join(stemmed_tokens))
    return stem_texts

def stemmer(texts):
    """Функция принимающая список текстов и возвращающая его после стемминга
    texts - исходный текст
    stem_texts - список текстов со стеммингом
    """
    porter_stemmer = PorterStemmer()
    stem_texts = []
    for text in texts:
        nltk_tokens = word_tokenize(text)
        line = ''
        for word in nltk_tokens:
            line += ' ' + porter_stemmer.stem(word)
        stem_texts.append(line)
    return stem_texts


#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
_morph = pymorphy2.MorphAnalyzer()
_lemmatizer = WordNetLemmatizer()    # для английского текста
def lemmatize(texts):
    """Функция лемматизации для списка текстов
    text - исходный текст
    res - список лемматизированных текстов
    """
    res = list()
    for text in texts:
        nltk_tokens = word_tokenize(text) # разбиваем текст на слова
        line = ''
        for word in nltk_tokens:
            parse = _morph.parse(word)[0]  # Это было для русских слов
            # дальше обрабатываем все части речи
            # lemm_word = _lemmatizer.lemmatize(word, pos='n')
            # lemm_word = _lemmatizer.lemmatize(lemm_word, pos='v')
            # lemm_word = _lemmatizer.lemmatize(lemm_word, pos='r')
            # lemm_word = _lemmatizer.lemmatize(lemm_word, pos='a')
            # lemm_word = _lemmatizer.lemmatize(lemm_word, pos='s')
            # line += ' ' + lemm_word
            line += ' ' + parse.normal_form
        res.append(line) # lemmatize для английских слов
    return res



from nltk.corpus import stopwords

def del_stopWords(texts):
    "texts - список текстов для удаления стоп-слов"
    russian_stop_words = set(stopwords.words('russian'))
    res = list()
    for text in texts:
        nltk_tokens = word_tokenize(text) # разбиваем текст на слова
        line = ''
        for stopW in list(russian_stop_words):
            while True:
                try:
                    del nltk_tokens[nltk_tokens.index(stopW)]
                except:
                    break
        line += ' '.join(nltk_tokens)
        res.append(line)
    return res