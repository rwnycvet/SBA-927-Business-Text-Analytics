from pathlib import Path

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

dataset = Path("SBA927.txt").read_text(encoding="utf-8").splitlines()

stop_words = set(stopwords.words("english"))
stop_words.difference_update({"no", "not", "nor"})


def preprocess(text):
    normalized = text.lower().strip()
    normalized = normalized.replace("doesn't", "does not")
    tokens = word_tokenize(normalized)

    return [
        token
        for token in tokens
        if token.isalpha() and token not in stop_words
    ]


processed_dataset = [preprocess(passage) for passage in dataset]

print("Processed passage 1:", processed_dataset[0])
print("Processed passage 10:", processed_dataset[9])
print("Passages processed:", len(processed_dataset))

from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("wordnet", quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_dataset = [
    [stemmer.stem(token) for token in passage]
    for passage in processed_dataset
]

lemmatized_dataset = [
    [lemmatizer.lemmatize(token) for token in passage]
    for passage in processed_dataset
]

print("Original tokens, passage 2:", processed_dataset[1])
print("Stemmed, passage 2:", stemmed_dataset[1])
print("Lemmatized, passage 2:", lemmatized_dataset[1])

from nltk import ne_chunk, pos_tag

nltk.download("averaged_perceptron_tagger_eng", quiet=True)
nltk.download("maxent_ne_chunker_tab", quiet=True)
nltk.download("words", quiet=True)

pos_tags_dataset = [
    pos_tag(word_tokenize(passage))
    for passage in dataset
]

ner_results_dataset = []

for tagged_passage in pos_tags_dataset:
    tree = ne_chunk(tagged_passage)
    entities = [
        (" ".join(word for word, tag in subtree.leaves()), subtree.label())
        for subtree in tree
        if hasattr(subtree, "label")
    ]
    ner_results_dataset.append(entities)

print("POS tags, passage 8:", pos_tags_dataset[7])
print("Named entities, passage 8:", ner_results_dataset[7])

from textblob import TextBlob

for passage_number in (5, 8, 12):
    text = dataset[passage_number - 1]
    polarity = TextBlob(text).sentiment.polarity
    print(f"TextBlob passage {passage_number}: polarity={polarity:.3f}")

    with Path("SBA927_results.txt").open("w", encoding="utf-8") as report:
        for i, original in enumerate(dataset):
            print(f"PASSAGE {i + 1}", file=report)
            print(f"Original: {original}", file=report)
            print(f"Processed: {processed_dataset[i]}", file=report)
            print(f"Stemmed: {stemmed_dataset[i]}", file=report)
            print(f"Lemmatized: {lemmatized_dataset[i]}", file=report)
            print(f"POS tags: {pos_tags_dataset[i]}", file=report)
            print(f"Named entities: {ner_results_dataset[i]}", file=report)
            print(file=report)

print("Saved results for all 12 passages to SBA927_results.txt")