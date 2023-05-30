import spacy

nlp = spacy.load("en_core_web_md")

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#What I find most interesting is that the similarity knows that monkeys have a diet of bananas
#And therefore knows to give it a higher similarity than if you were to compare a monkey and an apple

tokens = nlp('lynx zebra lion shrew ')
#Here we see that lynx and lion have a similarity above 0.5. This could definitely be that
#It knows that the lion and lynx are both of the cat family.
#Alternatively we also see high similarities on lynx->shrew (0.73) and lion->zebra (0.71) denoting
#that it can see that these are the types of creatures the lion and lynx most commonly hunt

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)