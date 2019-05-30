import os
import random
import tqdm

from shutil import copyfile

def create_partition(amount):
    half_amount = amount //2
    #if half_amount > len(poslist):
    #    return(None)
    split = 0
    current_dir = f"data/train{amount}-{split}"
    chosen_pozzies  = random.sample(poslist,half_amount)
    chosen_neggies = random.sample(neglist,half_amount)
    while(True):
        try:
            os.mkdir(current_dir)
            break
        except FileExistsError:
            split += 1
            current_dir = f"data/train{amount}-{split}"
    os.mkdir(current_dir+"/pos")
    os.mkdir(current_dir+"/neg")
    for chosen_element in chosen_pozzies:
        copyfile("data/train/pos/"+chosen_element,current_dir+"/pos/"+chosen_element)
    for chosen_element in chosen_neggies:
        copyfile("data/train/neg/"+chosen_element,current_dir+"/neg/"+chosen_element)
    #print(f"Partition of {amount} elements made in folder {current_dir}.")

def create_partitions(val_amount = 5, partitionlist = [50,100,150,200,500,1000,1500,2000,5000,10000,15000]):
    poslist = []
    neglist = []

    newposlist = []
    newneglist = []

    for filename in os.listdir("data/train/pos"):
        poslist.append(filename)

    for filename in os.listdir("data/train/neg"):
        neglist.append(filename)
    for partition_size in partitionlist:
        print(f"\nCreating {val_amount} partitions of size {partition_size}")
        for validation_size in tqdm.tqdm(range(val_amount)):
            try:
                create_partition(partition_size)
            except ValueError:
                print(f"Not enough data to make a partition of {partition_size}!")
                break

create_partitions()
