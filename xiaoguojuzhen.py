import sys
import os
import re
import numpy as np
from random import shuffle
import matplotlib.pyplot as plt


text = []
classes = 3

def prepare_data(filename):

    stop_word_list = []

    f = open("english.txt")
    stop_lines = f.readlines()
    for i in range(len(stop_lines)):
        stop_word_list.append(stop_lines[i].strip('\n'))
        # stop_word_list.append(stop_lines[i])
    f.close()

    # print(stop_word_list)
    # input('aaaaa')

    text = open(filename, 'r', encoding='UTF-8')
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

    def __init__(self, datas_all, pred_data):
        self.datas_all = datas_all
        self.pred_data = pred_data
        self.m = 0
        self.V = None
        self.test_data = None
        self.accuracies = None
        self.curr_expt = 1
        self.parameter = None
        self.predict_ratio = None
        self.confusion = None


    def train(self):

        accuracies = []

        train_data = self.datas_all

        if self.curr_expt == 1:
            test_data = self.datas_all[:int(len(self.datas_all)*0.20)]
            # print("len(datas_all)", len(self.datas_all))
            # print("len(test_data)", len(test_data))
            self.test_data = test_data

            train_data = self.datas_all[int(len(self.datas_all)*0.20)+1:]
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

        parameter = [prior_positive, prior_negative, prior_neutral, pos_denominator, neg_denominator, neu_denominator]

        self.parameter = parameter


    def test_accuracy(self):
        parameter = self.parameter
        test_data = self.test_data

        prior_positive, prior_negative, prior_neutral, pos_denominator, neg_denominator, neu_denominator = parameter[:]

        num_correct = 0
        num_total = 0
        a=b=c=d=e=f=x=y=z=0
        for item in test_data:
            num_total += 1
            words = item[:-1]
            label = int(item[-1])

            prob_positive = np.log(prior_positive)  # 先验概率
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

            if (prediction == 1) & (label == 1):  # 这里必须加括号，不加会出问题，不知道为什么
                a += 1
            if (prediction == 1) & (label == 0):
                c += 1
            if (prediction == 1) & (label == -1):
                b += 1
            if (prediction == 0) & (label == 0):
                z += 1
            if (prediction == 0) & (label == 1):
                x += 1
            if (prediction == 0) & (label == -1):
                y += 1
            if (prediction == -1) & (label == 0):
                f += 1
            if (prediction == -1) & (label == 1):
                d += 1
            if (prediction == -1) & (label == -1):
                e += 1

        accuracies = (float(num_correct) / len(self.test_data))
        print(a, b, c, d, e, f, x, y, z)
        print("num_total:", num_total)
        print("num_correct:", num_correct)
        print("a+b+c+d+e+f+x+y+z=", a+b+c+d+e+f+x+y+z)

        self.confusion = [a, b, c, d, e, f, x, y, z]

        # print(accuracies)
        # input("aaa")
        self.accuracies = accuracies


    # Conducts experiment 1
    def experiment1_results(self):
        self.curr_expt = 1
        # self.m = 0
        # self.train()
        # self.test_accuracy()
        # acc0 = self.accuracies
        # print('acc0:', acc0)
        self.m = 1
        self.train()
        self.test_accuracy()
        acc1 = self.accuracies
        confusion = self.confusion
        print('acc1:', acc1)
        return confusion


train_file = 'hb_sici_zhengli.csv'
datas_all = prepare_data(train_file)


def predict_accuracy():
    datas_all = prepare_data(train_file)
    predict_data = None

    NB = NaiveBayes(datas_all, predict_data)
    print('Running experiment1 on the dataset')

    conf = NB.experiment1_results()
    [a, b, c, d, e, f, x, y, z] = conf

    print("abcdefxyz:")
    print(a, b, c, d, e, f, x, y, z)

    accu = (a+e+z)/(a+b+c+d+e+f+x+y+z)

    p1 = a / (a + b + c)
    r1 = a / (a + d + x)
    f1_1 = (2 * p1 * r1) / (p1 + r1)

    p2 = e / (e + d + f)
    r2 = e / (e + b + y)
    f1_2 = (2 * p2 * r2) / (p2 + r2)

    p3 = z / (z + x + y)
    r3 = z / (z + c + f)
    f1_3 = (2 * p3 * r3) / (p3 + r3)

    pm = (p1+p2+p3)/3

    rm = (r1+r2+r3)/3

    fm = (f1_1+f1_2+f1_3)/3

    print("ACCURACU_CAL :", accu)
    print("precision_m:", pm)
    print("recall_m:", rm)
    print("f1:", fm)


predict_accuracy()

