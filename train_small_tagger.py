import cowparser as cp

train_sents = []
test_sents = []

gen = cp.sentences_for_dir(separate=False)
for i, (metadata, data) in enumerate(gen):
    train_sents.append([(a,b) for a,b,c in data])
    if i == 2000000:
        break

for i, (metadata, data) in enumerate(gen):
    test_sents.append([(a,b) for a,b,c in data])
    if i == 5000:
        break

from nltk.tag.perceptron import PerceptronTagger
pt = PerceptronTagger(load=False)
pt.train(train_sents,'model2.perc.dutch_tagger')
print(pt.evaluate(test_sents))
