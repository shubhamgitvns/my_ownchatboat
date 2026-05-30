from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

# Custom same meaning words
custom_words = {

    "varanasi": [
        "kashi",
        "banaras",
        "benares",
        "varansi",
        "varanasi"
    ],
    "temples": [
        "mandir",
        "temples",

    ]

}

# Clean words


def clean_words(sentence):

    # lowercase
    sentence = sentence.lower()

    # find the words remove numbers and punctuation and tokenize
    words = re.findall(r"[a-z]+", sentence)



   


    # stopwords
    stop_words = set(stopwords.words("english"))

    filtered = []

    for word in words:

        # remove common words
        if word not in stop_words:

            # custom synonym replace
            for main_word, synonyms in custom_words.items():

                if word in synonyms:

                    word = main_word

            filtered.append(word)
    

    ps = PorterStemmer()
    return [ps.stem(word) for word in filtered]


    # filtered = ps.stem(word)        

    # return filtered


# Find synonyms
def synonyms_of(word):

    words = {word}

    for synset in wn.synsets(word):

        for lemma in synset.lemmas():

            words.add(
                lemma.name().lower().replace("_", " ")
            )

    return words


# Expand sentence words
def expanded_sentence_words(sentence):

    result = set()

    for word in clean_words(sentence):

        result.update(synonyms_of(word))

    return result


# Sentence similarity
def sentence_meaning_score(sentence1, sentence2):

    words1 = expanded_sentence_words(sentence1)

    words2 = expanded_sentence_words(sentence2)

    common = words1.intersection(words2)

    total = words1.union(words2)

    if not total:

        return 0, common

    score = len(common) / len(total)

    return score, common

data = [

    {
        "question": "about the history of varanasi",
        "answer": "Varanasi is one of the oldest cities in India."
    },

    {
        "question": "explain about the varanasi",
        "answer": "Varanasi, also known as Kashi and Banaras, is one of the oldest living cities in the world."
    },

    {
        "question": "famous temples in varanasi",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "varanasi temple list",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "top temple in banaras",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "main temple of kashi",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "varanasi ganga ghat",
        "answer": "There are around 84 ghats in Varanasi."
    },

    {
        "question": "varansi famous ghat",
        "answer": "This are the famous ganga ghats in varanasi."
    },

    {
        "question": "varanasi holly river",
        "answer": "These rivers in varanasi: Ganga, Varuna, Assi"
    },

    {
        "question": "local food",
        "answer": "Kashi is famous for its traditional street food culture."
    },

    {
        "question": "varanasi famous snacks",
        "answer": "Famous snacks in Varanasi: Kachori, Samosha."
    },

    {
        "question": "kashi famous sweet",
        "answer": "Famous sweets in kashi: Jalebi, Rabdi."
    },

    {
        "question": "kashi famous drink",
        "answer": "Famous drinks in kashi: Lassi, Thandai."
    },

    {
        "question": "hello",
        "answer": "Hello I am your AI Guide."
    },

    {
        "question": "i am happy",
        "answer": "I think you are happy."
    },

    {
        "question": "i feel boring",
        "answer": "Ere guru banaras aial our bor ho jaiba."
    }

]


# Chat loop
def get_bot_response(user_input):

    scores = []

    for item in data:

        sentence = item['question']

        score, common = sentence_meaning_score(
            sentence,
            user_input
        )

        scores.append(score)

    max_score = max(scores)

    best_index = scores.index(max_score)

    if max_score == 0 or max_score < 0.2:

        return "Not Understand ??"

    return data[best_index]['answer']