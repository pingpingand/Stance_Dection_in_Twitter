fn_gl = [
      'guolvhkx_tweet_trans_119.csv', 'guolvhkx_tweet_trans_118.csv', 'guolvhkx_tweet_trans_117.csv', 'guolvhkx_tweet_trans_116.csv',
      'guolvhkx_tweet_trans_115.csv', 'guolvhkx_tweet_trans_114.csv', 'guolvhkx_tweet_trans_113.csv', 'guolvhkx_tweet_trans_112.csv',
      'guolvhkx_tweet_trans_111.csv', 'guolvhkx_tweet_trans_110.csv', 'guolvhkx_tweet_trans_109.csv', 'guolvhkx_tweet_trans_108.csv',
      'guolvhkx_tweet_trans_107.csv', 'guolvhkx_tweet_trans_106.csv', 'guolvhkx_tweet_trans_105.csv', 'guolvhkx_tweet_trans_104.csv',
      'guolvhkx_tweet_trans_103.csv', 'guolvhkx_tweet_trans_102.csv', 'guolvhkx_tweet_trans_101.csv', 'guolvhkx_tweet_trans_100.csv',
      'guolvhkx_tweet_trans_99.csv', 'guolvhkx_tweet_trans_98.csv', 'guolvhkx_tweet_trans_97.csv', 'guolvhkx_tweet_trans_96.csv',
      'guolvhkx_tweet_trans_95.csv', 'guolvhkx_tweet_trans_94.csv', 'guolvhkx_tweet_trans_93.csv', 'guolvhkx_tweet_trans_92.csv',
      'guolvhkx_tweet_trans_91.csv', 'guolvhkx_tweet_trans_90.csv', 'guolvhkx_tweet_trans_89.csv', 'guolvhkx_tweet_trans_88.csv',
      'guolvhkx_tweet_trans_87.csv', 'guolvhkx_tweet_trans_86.csv', 'guolvhkx_tweet_trans_85.csv', 'guolvhkx_tweet_trans_84.csv',
      'guolvhkx_tweet_trans_83.csv', 'guolvhkx_tweet_trans_82.csv', 'guolvhkx_tweet_trans_81.csv', 'guolvhkx_tweet_trans_80.csv',
      'guolvhkx_tweet_trans_79.csv', 'guolvhkx_tweet_trans_78.csv', 'guolvhkx_tweet_trans_77.csv', 'guolvhkx_tweet_trans_76.csv',
      'guolvhkx_tweet_trans_75.csv', 'guolvhkx_tweet_trans_74.csv', 'guolvhkx_tweet_trans_73.csv', 'guolvhkx_tweet_trans_72.csv',
      'guolvhkx_tweet_trans_71.csv', 'guolvhkx_tweet_trans_70.csv', 'guolvhkx_tweet_trans_69.csv', 'guolvhkx_tweet_trans_68.csv',
      'guolvhkx_tweet_trans_67.csv', 'guolvhkx_tweet_trans_66.csv', 'guolvhkx_tweet_trans_65.csv', 'guolvhkx_tweet_trans_64.csv',
      'guolvhkx_tweet_trans_63.csv', 'guolvhkx_tweet_trans_62.csv', 'guolvhkx_tweet_trans_61.csv', 'guolvhkx_tweet_trans_60.csv',
      'guolvhkx_tweet_trans_59.csv', 'guolvhkx_tweet_trans_58.csv', 'guolvhkx_tweet_trans_57.csv', 'guolvhkx_tweet_trans_56.csv',
      'guolvhkx_tweet_trans_55.csv', 'guolvhkx_tweet_trans_54.csv', 'guolvhkx_tweet_trans_53.csv', 'guolvhkx_tweet_trans_52.csv',
      'guolvhkx_tweet_trans_51.csv', 'guolvhkx_tweet_trans_50.csv', 'guolvhkx_tweet_trans_49.csv', 'guolvhkx_tweet_trans_48.csv',
      'guolvhkx_tweet_trans_47.csv', 'guolvhkx_tweet_trans_46.csv', 'guolvhkx_tweet_trans_45.csv', 'guolvhkx_tweet_trans_44.csv',
      'guolvhkx_tweet_trans_43.csv', 'guolvhkx_tweet_trans_42.csv', 'guolvhkx_tweet_trans_41.csv', 'guolvhkx_tweet_trans_40.csv',
      'guolvhkx_tweet_trans_39.csv', 'guolvhkx_tweet_trans_38.csv', 'guolvhkx_tweet_trans_37.csv', 'guolvhkx_tweet_trans_36.csv',
      'guolvhkx_tweet_trans_35.csv', 'guolvhkx_tweet_trans_34.csv', 'guolvhkx_tweet_trans_33.csv', 'guolvhkx_tweet_trans_32.csv',
      'guolvhkx_tweet_trans_31.csv', 'guolvhkx_tweet_trans_30.csv', 'guolvhkx_tweet_trans_29.csv', 'guolvhkx_tweet_trans_28.csv',
      'guolvhkx_tweet_trans_27.csv', 'guolvhkx_tweet_trans_26.csv', 'guolvhkx_tweet_trans_25.csv', 'guolvhkx_tweet_trans_24.csv',
      'guolvhkx_tweet_trans_23.csv', 'guolvhkx_tweet_trans_22.csv', 'guolvhkx_tweet_trans_21.csv', 'guolvhkx_tweet_trans_20.csv',
      'guolvhkx_tweet_trans_19.csv', 'guolvhkx_tweet_trans_18.csv', 'guolvhkx_tweet_trans_17.csv', 'guolvhkx_tweet_trans_16.csv',
      'guolvhkx_tweet_trans_15.csv', 'guolvhkx_tweet_trans_14.csv', 'guolvhkx_tweet_trans_13.csv', 'guolvhkx_tweet_trans_12.csv',
      'guolvhkx_tweet_trans_11.csv', 'guolvhkx_tweet_trans_10.csv', 'guolvhkx_tweet_trans_9.csv', 'guolvhkx_tweet_trans_8.csv',
      'guolvhkx_tweet_trans_7.csv', 'guolvhkx_tweet_trans_6.csv', 'guolvhkx_tweet_trans_5.csv', 'guolvhkx_tweet_trans_4.csv',
      'guolvhkx_tweet_trans_3.csv', 'guolvhkx_tweet_trans_2.csv', 'guolvhkx_tweet_trans_1.csv', 'guolvhkx_tweet_trans_0.csv'
         ]
import sys
import os
import re
import numpy as np
from random import shuffle
import matplotlib.pyplot as plt



curr_dataset = None
text = []
folds = 10
classes = 3


def prepare_data_pred(filename):
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

    for i in range(0, len(list(lines))):
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

        # print(tokenized_sentence_clean)
        # input("1111111")
        datas_all.append(tokenized_sentence_clean)

    shuffle(datas_all)
    # print(temp_fold)
    # input("11111")

    return datas_all

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


    def train(self):

        accuracies = []

        train_data = self.datas_all

        if self.curr_expt == 1:
            test_data = self.datas_all[:int(len(self.datas_all)*0.15)]
            # print(len(test_data))
            self.test_data = test_data

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
        for item in test_data:
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

        accuracies = (float(num_correct) / len(self.test_data))

        # print(accuracies)
        # input("aaa")
        self.accuracies = accuracies


    def predict(self):
        parameter = self.parameter
        pred_data = self.pred_data

        predict_result = []

        prior_positive, prior_negative, prior_neutral, pos_denominator, neg_denominator, neu_denominator = parameter[:]

        num_correct = 0
        p_1 = 0
        p0 = 0
        p1 = 0
        for item in pred_data:
            words = item[:-1]

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
                p1 += 1
            elif (prob_negative > prob_positive) & (prob_negative > prob_neutral):
                prediction = -1
                p_1 += 1
            elif (prob_neutral > prob_positive) & (prob_neutral > prob_negative):
                prediction = 0
                p0 += 1

            predict_result.append(prediction)

        # print("-1:", p_1, "p0:", p0, "1:", p1)
        # print(p_1/(p_1+p0+p1), p0/(p_1+p0+p1), p1/(p_1+p0+p1))

        predict_ratio_f1 = p_1/(p_1+p0+p1)
        predict_ratio_0 = p0/(p_1+p0+p1)
        predict_ratio_1 = p1/(p_1+p0+p1)

        self.predict_ratio = [predict_ratio_f1, predict_ratio_0, predict_ratio_1]

        # fl = open('list.txt', 'w')
        # for i in predict_result:
        #     print(i)
        #     fl.write(str(i))
        #     fl.write("\n")



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
        print('acc1:', acc1)
        return acc1

    def experiment3_results(self):
        self.curr_expt = 3
        self.m = 1
        self.train()
        self.predict()
        ratio_f1 = self.predict_ratio[0]
        ratio_0 = self.predict_ratio[1]
        ratio_1 = self.predict_ratio[2]
        return ratio_f1, ratio_0, ratio_1


train_file = 'hb_sici_zhengli.csv'
datas_all = prepare_data(train_file)


def predict_accuracy():
    datas_all = prepare_data(train_file)
    predict_data = None

    NB = NaiveBayes(datas_all, predict_data)
    print('Running experiment1 on the dataset')

    NB.experiment1_results()
    for i in range(10):
        datas_all = prepare_data(train_file)
        NB = NaiveBayes(datas_all, predict_data)
        NB.experiment1_results()


rf1_list = [0.5345208505937586, 0.5160521955260977, 0.4681783536585366, 0.49069148936170215, 0.5107624954396206, 0.5260170293282876, 0.5045207956600362, 0.4861685214626391, 0.4747624703087886, 0.5111706881143878, 0.5073147711184521, 0.447178002894356, 0.5210954848260547, 0.5024920706841867, 0.4647845468053492, 0.4766269477543538, 0.4709531866892273, 0.47898230088495575, 0.47728965003723006, 0.44594594594594594, 0.5062146892655367, 0.48965383871591567, 0.49015920772220134, 0.5134370579915134, 0.512549537648613, 0.49944227551589515, 0.5140466228332337, 0.5309184046834979, 0.5061258278145695, 0.4884070416487763, 0.485185963437697, 0.503844305622297, 0.5874913773281214, 0.5531496062992126, 0.5220390954388655, 0.4768186958160573, 0.48587990487514865, 0.4920522783468739, 0.4663299663299663, 0.47956173619890435, 0.5235474006116208, 0.5386306001690617, 0.5346146894016991, 0.4932447397563677, 0.4421357180431352, 0.4556383746092811, 0.4716054976589639, 0.49182115594329334, 0.5340926581499154, 0.5130414349494792, 0.5480846289469467, 0.49129821260583256, 0.5038366874185609, 0.5070115300716734, 0.5372710492687776, 0.5020655822359927, 0.5020840012824623, 0.5047435517343611, 0.5188082556591211, 0.535514888337469, 0.543314808761033, 0.5525075732076742, 0.5275932858350441, 0.5167890438082666, 0.4848583258910449, 0.4487339403766995, 0.471332577013701, 0.5325979176995538, 0.541505146370806, 0.5879507475813545, 0.5571942863778887, 0.5462734272846143, 0.5551839464882943, 0.5747078464106845, 0.5645680147058824, 0.5603571428571429, 0.54728208427147, 0.5470992822966507, 0.5335509611896989, 0.5924161934420223, 0.5591878172588832, 0.5430844012372956, 0.5480838756326826, 0.5428176795580111, 0.49288537549407113, 0.4802494802494803, 0.5151759333870535, 0.5021694450787851, 0.5133938454726589, 0.538442643085237, 0.5401404151404151, 0.5465933784992969, 0.5593514765489288, 0.5379393253659571, 0.4887997652352538, 0.48729747245625404, 0.510999594484996, 0.5038581391897907, 0.5182887237573046, 0.5116024518388792, 0.5049496981891348, 0.5028028028028028, 0.49783680450749573, 0.5292311326325735, 0.5243398823676636, 0.5071206767319841, 0.49870649106302917, 0.5415691462297751, 0.49163963064636884, 0.4796242993485835, 0.4902483747291215, 0.4805988771054273, 0.42458923512747876, 0.4072372999304106, 0.405982905982906, 0.4400352733686067, 0.46873207114170967, 0.4949684062719401, 0.4448927585474623, 0.5029013539651838]

r0_list = [0.28099972383319527, 0.2998135874067937, 0.33822408536585363, 0.33643617021276595, 0.3381977380518059, 0.3088930936613056, 0.32802893309222425, 0.3220985691573927, 0.3922209026128266, 0.3605898123324397, 0.3058046248230297, 0.3661360347322721, 0.307920059215396, 0.28998640688717714, 0.31441307578008915, 0.29605866177818513, 0.3102086858432036, 0.3301991150442478, 0.3060312732688012, 0.3396805896805897, 0.2934086629001883, 0.24269967124347322, 0.27165601103171616, 0.2788442109517074, 0.2758696609423162, 0.29866146123814835, 0.2691771269177127, 0.24222466154409075, 0.26490066225165565, 0.2739373121511378, 0.28136163059466274, 0.2808745795290726, 0.22280984134283743, 0.2736220472440945, 0.25162897661939443, 0.29023746701846964, 0.2684304399524376, 0.2741080890144825, 0.29924242424242425, 0.2726506531816266, 0.2768603465851172, 0.24885883347421808, 0.24745435922154607, 0.2995016611295681, 0.2503945291951604, 0.2648473190670834, 0.2715601872828878, 0.2549462533104845, 0.23980298599353547, 0.28769483825487585, 0.2583747395415932, 0.28269049858889933, 0.26842333864195744, 0.2873169211592396, 0.26338208149936104, 0.2402530338239091, 0.2382173773645399, 0.2697895048917877, 0.2761318242343542, 0.26054590570719605, 0.29993461915658715, 0.26144395826321104, 0.21645936481101316, 0.25930203778566124, 0.3239425184704068, 0.41536734439316453, 0.37097477964918407, 0.2850768468021815, 0.2677449538831707, 0.2075637642919965, 0.2329578446173499, 0.24640418422199623, 0.24154589371980675, 0.2303839732888147, 0.25965073529411764, 0.2342857142857143, 0.23222901254422643, 0.23190789473684212, 0.2537178092129126, 0.23685656713683825, 0.2564467005076142, 0.24635439681838267, 0.24078091106290672, 0.23362273086029992, 0.23794466403162054, 0.26964656964656963, 0.2506043513295729, 0.2996117835122174, 0.29444321452291344, 0.26062392532547285, 0.21214896214896214, 0.21027738719161446, 0.21077012159814706, 0.23845555476981825, 0.27222928690208353, 0.3054439403758911, 0.28720600162206, 0.2686600385813919, 0.257412885073227, 0.2449649737302977, 0.2509456740442656, 0.2602602602602603, 0.24418955629338968, 0.23940002362111729, 0.23726692529095234, 0.23214476924724275, 0.24400282220131703, 0.2585733184084665, 0.27451959071624654, 0.26905014391758825, 0.28104684114019, 0.2797255146600125, 0.2753541076487252, 0.2691718858733472, 0.3497698882314267, 0.2911816578483245, 0.25817555938037867, 0.267727591855839, 0.2677850923763007, 0.24177949709864605]

r1_list = [0.1844794255730461, 0.18413421706710853, 0.19359756097560976, 0.17287234042553193, 0.1510397665085735, 0.1650898770104068, 0.1674502712477396, 0.1917329093799682, 0.1330166270783848, 0.1282394995531725, 0.18688060405851817, 0.18668596237337193, 0.17098445595854922, 0.20752152242863617, 0.22080237741456166, 0.22731439046746105, 0.2188381274675691, 0.19081858407079647, 0.21667907669396871, 0.21437346437346438, 0.20037664783427495, 0.2676464900406111, 0.2381847812460825, 0.20771873105677915, 0.2115808014090709, 0.2018962632459565, 0.2167762502490536, 0.22685693377241126, 0.22897350993377483, 0.23765564620008586, 0.23345240596764025, 0.21528111484863047, 0.18969878132904117, 0.1732283464566929, 0.22633192794174012, 0.23294383716547304, 0.24568965517241378, 0.2338396326386436, 0.23442760942760943, 0.24778761061946902, 0.19959225280326198, 0.2125105663567202, 0.21793095137675483, 0.20725359911406424, 0.30746975276170435, 0.2795143063236355, 0.2568343150581483, 0.2532325907462222, 0.22610435585654917, 0.19926372679564502, 0.19354063151146017, 0.2260112888052681, 0.2277399739394817, 0.20567154876908694, 0.19934686923186143, 0.2576813839400981, 0.25969862135299776, 0.22546694337385118, 0.20505992010652463, 0.203939205955335, 0.15675057208237986, 0.18604846852911477, 0.25594734935394275, 0.2239089184060721, 0.19119915563854833, 0.13589871523013597, 0.15769264333711494, 0.18232523549826474, 0.19074989974602327, 0.20448548812664907, 0.20984786900476135, 0.20732238849338952, 0.2032701597918989, 0.19490818030050083, 0.17578125, 0.20535714285714285, 0.22048890318430364, 0.22099282296650719, 0.21273122959738847, 0.1707272394211394, 0.18436548223350255, 0.2105612019443217, 0.2111352133044107, 0.22355958958168903, 0.2691699604743083, 0.2501039501039501, 0.23421971528337363, 0.1982187714089975, 0.1921629400044277, 0.2009334315892901, 0.24771062271062272, 0.2431292343090886, 0.22987840185292416, 0.2236051198642246, 0.23897094786266262, 0.20725858716785484, 0.20179440389294404, 0.22748182222881733, 0.2242983911694683, 0.2434325744308231, 0.2441046277665996, 0.23693693693693693, 0.2579736391991146, 0.2313688437463092, 0.23839319234138406, 0.2607345540207731, 0.2572906867356538, 0.19985753536175843, 0.2338407786373846, 0.2513255567338282, 0.22870478413068845, 0.2396756082345602, 0.30005665722379604, 0.3235908141962422, 0.24424720578566733, 0.2687830687830688, 0.27309236947791166, 0.23730400187222092, 0.287322149076237, 0.2553191489361702]



def draw_picture():
    # datas_all = prepare_data(train_file)
    # for file in fn_gl:
    #     predict_data = prepare_data_pred('./predict/all/' + file)
    #     NB = NaiveBayes(datas_all, predict_data)
    #     rf1, r0, r1 = NB.experiment3_results()
    #     rf1_list.append(rf1)
    #     r0_list.append(r0)
    #     r1_list.append(r1)
    # print("-1比例")
    # print(rf1_list)
    # print("0比例")
    # print(r0_list)
    # print("1比例")
    # print(r1_list)

    flag_list = []
    for i in range(0,120):
        flag_list.append(str(119-i))

    fig = plt.figure(figsize=(25,4))
    plt.tick_params(axis='x', labelsize=8)
    plt.bar(flag_list, r1_list)
    plt.show()


rf1_list_santian = []
r0_list_santian = []
r1_list_santian = []

pred_file = ['guolvhkx_tweet_trans_913_915.csv', 'guolvhkx_tweet_trans_916_918.csv']

def predict_qianhousantian():
    datas_all = prepare_data(train_file)
    for file in pred_file:
        predict_data = prepare_data_pred('./predict/santian/' + file)
        NB = NaiveBayes(datas_all, predict_data)
        rf1, r0, r1 = NB.experiment3_results()
        rf1_list_santian.append(rf1)
        r0_list_santian.append(r0)
        r1_list_santian.append(r1)

    print('-1,0,1:',rf1_list_santian,r0_list_santian,r1_list_santian)

# predict_accuracy()
# draw_picture()
predict_qianhousantian()



