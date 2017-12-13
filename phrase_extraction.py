#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import nltk 





with open('phrase_test.txt', 'r') as f:
	sample = f.read()


sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
def extract_entity_names(t):
	entity_names = []

	if hasattr(t, 'label') and t.label:
		print(t.label())
		if t.label() == 'NE':
			print("hahahah")
			entity_names.append(' '.join([child[0] for child in t]))
		else:
			for child in t:
				print(child)
				if child[0]=='NN':
					entity_names.append(' '.join([child[0]]))
				entity_names.extend(extract_entity_names(child))

	return entity_names

entity_names = []
for tree in chunked_sentences:
	# Print results per sentence
	# print extract_entity_names(tree)

	print(tree)
	print("ppp")
	entity_names.extend(extract_entity_names(tree))

# Print all entity names


# Print unique entity names
print set(entity_names)
# text = nltk.word_tokenize(sample)
# tagged_txt=nltk.pos_tag(text)
# chunked_sentences=nltk.ne_chunk_sents(tagged_txt, binary=True)
# print (tagged_txt)


