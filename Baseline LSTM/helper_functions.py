import torch

def prepare_sequence(seq, to_ix):
    idxs = []
    for w in seq:
        try:
            idxs.append(to_ix[w])
        except KeyError:
            idxs.append(to_ix["<UNK>"])
    return torch.tensor(idxs, dtype=torch.long)

def prepare_sequence2(seq, to_ix):
    idxs = []
    for w in seq:
        try:
            idxs.append(to_ix[w])
        except KeyError:
            idxs.append(to_ix["<UNK>"])
    return torch.tensor([idxs])#, dtype=torch.long)

def label_index_resolver(labelindex, label_dict):
    for labelclass in label_dict.keys():
        if label_dict[labelclass] == labelindex:
            return labelclass
    return None

def add_to_counting_dict(word_dict,word):
    try:
        word_dict[word] += 1
    except KeyError:
        word_dict[word] = 1

def vectorized_labels(labels, label_dict):
    one_hot = [0.0 for i in range(len(label_dict.keys()))]
    for label in labels:
        one_hot[label_dict[label]] = 1.0
    return one_hot
