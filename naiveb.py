import sys
import os
import re
import numpy as np
from random import shuffle

curr_dataset = None
text = []
folds = 10
classes = 3


def prepare_data():

    stop_word_list = []

    f = open("english.txt")
    stop_lines = f.readlines()
    for i in range(len(stop_lines)):
        stop_word_list.append(stop_lines[i].strip('\n'))
        # stop_word_list.append(stop_lines[i])
    f.close()

    # print(stop_word_list)
    # input('aaaaa')

    text = open('hb_sanci.csv', 'r', encoding='UTF-8')
    lines = text.readlines()
    datas_all = []

    for i in range(0, len(list(lines)), 2):
        tweet = lines[i]
        # print(tweet)
        # input("1111111")

        tokenized_sentence_clean = []

        # Convert to lower case
        tweet = tweet.lower()
        # Replaces URLs with the word URL
        tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' ', tweet)
        # Replace @handle with the word USER_MENTION
        tweet = re.sub(r'@[\S]+', ' ', tweet)
        # Replaces #hashtag with hashtag
        tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
        # Remove RT (retweet)
        tweet = re.sub(r'\brt\b', '', tweet)
        # Replace 2+ dots with space
        tweet = re.sub(r'\.{2,}', ' ', tweet)
        # Strip space, " and ' from tweet
        tweet = tweet.strip(' "\'')
        # Replace multiple spaces with a single space
        tweet = re.sub(r'\s+', ' ', tweet)

        words = tweet.split()

        for word in words:
            word = preprocess_word(word)
            if is_valid_word(word):
                if word not in stop_word_list:
                    tokenized_sentence_clean.append(word)

        label = int(lines[i+1])
        tokenized_sentence_clean.append(label)

        # print(tokenized_sentence_clean)
        # input("1111111")
        datas_all.append(tokenized_sentence_clean)

    shuffle(datas_all)
    # print(temp_fold)
    # input("11111")

    return datas_all


def preprocess_word(word):
    # Remove punctuation
    # word = word.strip('\'"?!,.():;')
    word = word.strip(',./;[]`-=<>?:"~!@#$%^&*()_+\'""')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


class NaiveBayes:

    def __init__(self, datas_all):
        self.datas_all = datas_all
        self.m = 0
        self.V = None
        self.test_data = None
        self.accuracies = None
        self.curr_expt = 1

    def test(self):

        accuracies = []
        x = range(1, 11)
        if self.curr_expt == 2:
            x = range(1, 2)

        test_data = self.datas_all[:int(len(self.datas_all)*0.15)]
        # print(len(test_data))

        train_data = self.datas_all[int(len(self.datas_all)*0.15)+1:]
        # print(len(train_data))
        # input("a")

        V = [{}, {}, {}]

        # Build vocabulary
        for item in train_data:
            words = item[:-1]
            # print(words)

            label = int(item[-1])  # 标签为 -1,0，1
            # print(label)
            # input('asdfgasdfgasdfg')

            for word in words:
                if word not in V[label]:
                    V[label][word] = 1

                else:
                    V[label][word] += 1

        self.test_data = test_data

        self.V = V
        # print(self.V[-1])
        # input('*' * 30)

        positive_vocab_count = len(self.V[1])
        negative_vocab_count = len(self.V[-1])
        neutral_vocab_count = len(self.V[0])

        num_positive_count = sum(self.V[1].values())
        num_negative_count = sum(self.V[-1].values())
        num_neutral_count = sum(self.V[0].values())

        # print(positive_vocab_count, negative_vocab_count, num_positive_count, num_negative_count)
        # input('aqqqqqqqqq')

        neg = 0
        pos = 0
        neu = 0
        i = 0
        for item in train_data:
            i += 1
            label = int(item[-1])

            if label == -1:
                neg += 1
            elif label == 0:
                neu += 1
            elif label == 1:
                pos += 1

        prior_positive = pos/i
        prior_negative = neg/i
        prior_neutral = neg/i

        pos_denominator = num_positive_count + self.m * (positive_vocab_count + negative_vocab_count + neutral_vocab_count)
        neg_denominator = num_negative_count + self.m * (positive_vocab_count + negative_vocab_count + neutral_vocab_count)
        neu_denominator = num_neutral_count + self.m * (positive_vocab_count + negative_vocab_count + neutral_vocab_count)

        # print(pos_denominator, neg_denominator)
        # input('@'*60)



        num_correct = 0
        for item in test_data:
            words = item[:-1]
            label = int(item[-1])

            prob_positive = np.log(prior_positive)  # 先验概率，在这里正负向各五百条，所以是0.5
            prob_negative = np.log(prior_negative)
            prob_neutral = np.log(prior_neutral)
            prediction = 0
            for word in words:
                if word in self.V[1]:
                    prob_positive += np.log((self.V[1][word] + self.m) / pos_denominator)
                else:
                    if self.m > 0:
                        prob_positive += np.log(self.m / pos_denominator)
                    else:
                        prob_positive -= np.log(pos_denominator)

                if word in self.V[-1]:
                    prob_negative += np.log((self.V[-1][word] + self.m) / neg_denominator)
                else:
                    if self.m > 0:
                        prob_negative += np.log(self.m / neg_denominator)
                    else:
                        prob_negative -= np.log(neg_denominator)

                if word in self.V[0]:
                    prob_neutral += np.log((self.V[0][word] + self.m) / neu_denominator)
                else:
                    if self.m > 0:
                        prob_neutral += np.log(self.m / neu_denominator)
                    else:
                        prob_neutral -= np.log(neu_denominator)

            # print(prob_negative, prob_neutral, prob_positive)
            # input('aaaaaaaaaaaa')

            if (prob_positive > prob_negative) & (prob_positive > prob_neutral):
                prediction = 1
            elif (prob_negative > prob_positive) & (prob_negative > prob_neutral):
                prediction = -1
            elif (prob_neutral > prob_positive) & (prob_neutral > prob_negative):
                prediction = 0

            if prediction == label:
                num_correct += 1

        accuracies = (float(num_correct) / len(self.test_data))

        # print(accuracies)
        # input("aaa")
        self.accuracies = accuracies


    # Conducts experiment 1
    def experiment1_results(self):
        self.curr_expt = 1
        self.m = 0
        self.test()
        acc0 = self.accuracies

        print('acc0:', acc0)
        self.m = 1
        self.test()
        acc1 = self.accuracies
        print('acc1:', acc1)

    def predict(self):
        self.curr_expt = 1
        self.m = 1


datas_all = prepare_data()

NB = NaiveBayes(datas_all)
print('Running experiment1 on the dataset')

NB.experiment1_results()
