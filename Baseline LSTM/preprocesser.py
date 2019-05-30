import json
from tqdm import tqdm
import os
import spacy
import pickle
from helper_functions import *

nlp = spacy.blank('nl')

token_dict = {} # stores tokens and their number
token_counter = {"<UNK>":0}

sup_dict = {"train": "data/train/", "test": "data/test/"}
unsup_dir = "data/test"
data_dict = {"train":  [], "test": []} # stores raw data
labels = ["pos","neg"]

vectorized_data = {"train": [],"test": []} # stores vectorized data

def read_data():
    print("\nReading data (4 progress bars will be shown):")
    for key in sup_dict.keys():
        for label in labels:
            for file in tqdm(os.listdir(sup_dict[key]+label)):
                text = []
                with open(sup_dict[key]+label+"/"+file, encoding="utf-8") as fp:
                    text = fp.readlines()
                data_dict[key].append([text,label])


def find_tokens(datalist):
    print("\nFinding tokens:")
    for data_index in tqdm(range(len(datalist))):
        for excerpt_index in range(len(datalist[data_index][0])):
            excerpt = nlp(datalist[data_index][0][excerpt_index])
            for token in [t.lemma_ for t in excerpt]:
                add_to_counting_dict(token_counter,token.lower())

    print("Amount of tokens: ",len(token_counter.keys()))

def remove_hls():
    i = 1
    for token in token_counter.keys():
        if not(token == "<UNK>"):
            if token_counter[token] == 1:
                add_to_counting_dict(token_counter,"<UNK>")
            else:
                token_dict[token] = i
                i += 1
    token_dict["<UNK>"] = i
    print(str(len(token_dict.keys())) + " tokens in set after discarding hapax legomena.\n")

def vectorize_excerpt(excerpt):
    vectorized_excerpt = []
    doc = nlp(excerpt)
    for w in [t.lemma_ for t in doc]:
        try:
            vectorized_excerpt.append(token_dict[w.lower()])
        except KeyError:
            vectorized_excerpt.append(token_dict["<UNK>"])
    return(vectorized_excerpt)

def vectorize_label(label):
    if label == "pos":
        return(1)
    elif label == "neg":
        return(0)
    # else:
    #     return(0)

def vectorize(datalist):
    print("Vectorizing a datalist")
    vectorized_datalist = []
    for [text,label] in tqdm(datalist):
        vectext = []
        for excerpt in text:
            vectext.append(vectorize_excerpt(excerpt))
        vectorized_datalist.append([vectext,vectorize_label(label)])
    return(vectorized_datalist)

def create_training():
    print("\nCreating training set: ")
    for i in tqdm(range(len(data))):
        text = []
        labels = []
        for token in [t.lemma_ for t in nlp(data[i]['text'])]:
                text.append(token)
        for label in data[i]['labels']:
                labels.append(label)
        training_data.append((text, vectorized_labels(labels)))

# READ DATA
# read_data()
# pickle_out = open("pickles/data.pickle","wb")
# pickle.dump(data_dict,pickle_out)
# pickle_out.close()

pickle_in = open("pickles/data.pickle","rb")
data_dict = pickle.load(pickle_in)


# FIND TOKENS
# find_tokens(data_dict["train"])
# remove_hls()
# pickle_out = open("pickles/tokens.pickle","wb")
# pickle.dump(token_dict,pickle_out)
# pickle_out.close()

pickle_in = open("pickles/tokens.pickle","rb")
token_dict = pickle.load(pickle_in)

find_tokens(data_dict["train"])

print("after", len(token_dict))


# VECTORIZE
# for setkind in ["train","test"]:
#     print("Vectorizing",setkind,"ing set.")
#     vectorized_data[setkind] = vectorize(data_dict[setkind])
#
# pickle_out = open("pickles/vectorized_data.pickle","wb")
# pickle.dump(vectorized_data,pickle_out)
# pickle_out.close()

pickle_in = open("pickles/vectorized_data.pickle","rb")
vectorized_data = pickle.load(pickle_in)
