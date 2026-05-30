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
        "answer": "Varanasi is one of the oldest cities in India.\nVaranasi, also known as Kashi and Banaras, is one of the oldest living cities in the world.\n It is located on the banks of the sacred Ganges River in the Indian state of Uttar Pradesh.\nThe name “Varanasi” comes from two rivers:\nVaruna\nAssi\nVaranasi has around 84 ghats, where people perform prayers, rituals, meditation, and holy bathing. The most famous ghats are:\nDashashwamedh Ghat\nAssi Ghat\nManikarnika Ghat\nTulsi Ghat\nThe city is deeply connected with Shiva and is considered the spiritual capital of India.\nIt is a city where ancient traditions and modern life exist together, making it one of the most unique cities in the world.\nVaranasi is also known for:\nclassical music\nSanskriti\nAdhyatm\nMeditation\nYoga\nTantra Mantra\nStreet food\nBanarasi paan\nSilk sarees\nKashik Cloths"
    },

    {
        "question": "explain about the varanasi",
        "answer": "Varanasi, also known as Kashi and Banaras, is one of the oldest living cities in the world.\n It is located on the banks of the sacred Ganges River in the Indian state of Uttar Pradesh.\nThe name “Varanasi” comes from two rivers:\nVaruna\nAssi\nVaranasi has around 84 ghats, where people perform prayers, rituals, meditation, and holy bathing. The most famous ghats are:\nDashashwamedh Ghat\nAssi Ghat\nManikarnika Ghat\nTulsi Ghat\nThe city is deeply connected with Shiva and is considered the spiritual capital of India.\nIt is a city where ancient traditions and modern life exist together, making it one of the most unique cities in the world.\nVaranasi is also known for:\nclassical music\nSanskriti\nAdhyatm\nMeditation\nYoga\nTantra Mantra\nStreet food\nBanarasi paan\nSilk sarees\nKashik Cloths",

    },

    {
        "question": "famous temples in varanasi",
        "answer":  "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",

    },

    {
        "question": "varanasi temple list",
        "answer":     "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",

    },

    {
        "question": "top temple in banaras",
        "answer":     "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",

    },

    # {
    #     "question": "main temple of kashi",
    #     "answer": "Varanasi is the city of temples there are many famous temples."
    # },

    {
        "question": "varanasi ganga ghat",
        "answer":     "There are around 84 ghats in Varanasi, and each ghat has its own history, rituals, and atmosphere.\nPeople come to the ghats for:\nHoly Bathing\nPrayer\nMeditation\nYoga\nBoat Riding\nThis the famous ghatsin kashi where the torist mostly visit\nAssi Ghat, Deshashwmag Ghat, Tulsi Ghat, Ganga Mahal, Harishchandra Ghat, Namo Ghat, Lalita Ghat, Manikarnika Ghat.\nWhich ghat you visit??",

    },

    {
        "question": "varansi famous ghat",
        "answer":     "This are the famous gnnga ghats in varanasi:\n Assi Ghat, Deshashwmag Ghat, Tulsi Ghat.",

    },

    {
        "question": "varanasi holly river",
        "answer": "These rivers in varanasi: Ganga, Varuna, Assi"
    },

    {
        "question": "local food",
        "answer":     "Kashi is famous for its traditional street food culture,tradition including:\nFood:\n Dal Bati Chokha, Dal Chawal Bhujiya Papad Achar\nSnakes:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki,Panir Tikki, Chola Papad\nSweets:\nJalabi, Rabdi, Rabdie with dry fruits, Mallai, Longlatta, Gulab Jamun, Barfi\nDrinks:\nThandai, Aam Panna, Lassi, Sugarcan Juse, Badam Dudh(Winter Special), Malio(Winter Special)",

    },

    {
        "question": "varanasi famous snacks",
        "answer":     "Famosh Snacks in Varanasi/Kashi:\nSnacks:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki, Panir Tikki, Chola Papad",

    },

    {
        "question": "kashi famous sweet",
        "answer":     "Famous Sweets in kashi:\nSweets:\nJalabi, Rabdi, Rabdie with dry fruits, Mallai, Longlatta, Gulab Jamun, Barfi",
    },

    {
        "question": "kashi famous drink",
        "answer":     "Famouus Drinks in kashi:\nDrinks:\nLassi, Aam Panna, sugarcan Juice, Thandai, Badam Dudh(Winter Special), Malio(Winter Special)",

    },

    {
        "question": "hello",
        "answer":     "Hello I am your AI Guide.\nWhich place you visit in varanasi",

    },

    {
        "question": "i am happy",
        "answer": "I think you are happy."
    },

    {
        "question": "i feel boring",
        "answer":   "Ere guru banaras aial our bor ho jaiba hmre rehte to raja ka khak banaras aaila\nawa tohe banaras ke rang dekhai hlka gulabi hlka nila tohar mood bnai tan man tohar astha me dubai.\nawa raja tohe bnaras ghumai\nSbse pehle chauck ja weha sahi pan bhandar se mst metha bnarasi pan kha maghain patta wala raja mood phle thik kera\nagar samay sam ke hw 4-5 ke bich me bina time west kiye baba thandai wale se thandai pia 1 glass our bina soche samjhe noka bihar kere dashaswamagy ghat ja or 84 ghat ka darshan kera.\nHidden place in kashi:\n Temples: Pahupati nath mandir, chandra kup, 12 jyotiling mandir darshan, 9 devi mandir, 84 yoni mandir"

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
