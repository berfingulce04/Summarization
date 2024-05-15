import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize,word_tokenize
import heapq
#nltk.downland()
import wikipedia
wikipedia.set_lang("TR")
topic=input("Özetini almak istediğiniz konuyu girin:")
wikipage=wikipedia.summary(topic,sentences=20)
print(wikipage)

wiki_sent=[]
wiki_sent=sent_tokenize(wikipage)

wiki_words=[]
for sent in wiki_sent:
    wiki_words.extend(word_tokenize(sent))


stopwords=stopwords.words("turkish")
tagged_words=nltk.pos_tag(wiki_words)
#tagged ile kelimenin türünün ne olduğu öğrenilir
ner=[]
for word in tagged_words:
    ner.extend(nltk.ne_chunk(tagged_words))
#Named Entity Recognition ile varlık ismini tanımlamaya yardımcı olur.

word_frequencies = {}
for word in wiki_words:
    if word not in stopwords and word.isalpha():
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
print(word_frequencies)
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
print(word_frequencies)

sentence_scores = {}
for sent in wiki_sent:
    for word in wiki_words:
        if word.lower() in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
print(sentence_scores)
print("---------------------------------")

summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print(topic+" ile ilgili özet: "+str(summary))










