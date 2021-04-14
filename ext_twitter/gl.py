import random
from random import randint

oldf = open('', 'r', encoding='UTF-8')
newf = open('', 'w', encoding='UTF-8')
n = 0
lv = 0  # 过滤后的数量
j = 0  # 原数量

flag = 0

keywords = ['parade', 'government', 'protesters', 'communist', 'communism',
            'demonstration', 'chief executive', 'conflict', 'democracy',
            'independence', 'independent', 'crisis', 'crimes', 'democratization',
            'revolution', 'protest', 'freedom', 'justice', 'violent', 'violence',
            'thugs', 'demonstrates', 'security', 'democratic', 'demonstrators', 'police',
            'extradition', 'legislative', 'political', 'arrest', 'riot', 'security', 'peace', 'vicious',
            'suppressed', 'authentic', 'administrative secretary', 'mask', 'participants', 'mob', 'authorities',
            'lin zheng', 'ministry', 'one country', 'two systems', 'mess', 'ccp',
            'prc', 'reviving', 'revive',  'restore', 'terrorism', 'freehong kong', 'free hong kong', 'movement',
            'situation', 'citizen',
            'propaganda', 'xi jinping', 'young people', 'demo', 'safety',
            'crackdown', 'gather', 'regulation', 'support', 'turmoil', 'anti delivery', 'retreat', 'march'
            ]

wgwords = ['japan', 'yen', 'disney', 'india', 'taiwan', 'macao', 'soccer game', 'stock market', 'sydney',
           'stock exchange', 'foreign exchange', 'umbrella', 'anmen square', 'london', 'hong kong sim',
           'bonus', 'korean', 'consumption tax', '1989', 'salary', 'world_cup', 'world cup', 'iran', 'thailand',
           'music', 'tourism', 'vacation', 'discount', 'singapore', 'okinawa', 'moscow', 'sign the petition',
           'lithuania', 'economy', 'russia', 'atlanta', 'nepal', 'suvarnabhumi', 'hsbc', 'financial', 'got7',
           'amsterdam', 'tiananmen', 'yokohama', 'exchange rate', 'british', 'busan', 'german', 'korea',
           'iraq', 'syria', 'yokohama', 'seoul', 'munemanteu', 'takunpao', 'shishimaru', 'chikwa', 'sing', 'liuhecai',
           'fast three', 'external model', 'film festuval', 'golden ring award', 'breaking news', 'scmp', 'udn.com',
           'investor', 'mychinanews', 'yomiuri shimbun online', 'smartnews', 'hansen index', 'money 18', 'theinitium',
           'afpbb', 'exploon', 'woachinese', 'lihkg', 'www.3.nhk', 'www.it.com', 'shimenan.xsrv', 'sankei', 'dlvr.it',
           'nikkei', 'on.wsj', 'www.nnews', 'ift.tt', 'nytimes', 'complexmatter', 'www.ntdtv', 'dwnews',
           'headline daily', 'goo.gl', 'rthk', 'lvv2.com', 'goo.gl', 'afp', 'trad.cn.rfi', 'buff.ly', 'bannedbook',
           'talk.ltn', 'sbs.com', 'cctv one minute', 'gnai.co'
           ]


lines = oldf.readlines()
# for i in range(0,len(list(lines)),2):
for i in range(0,len(list(lines))):
    j = j + 1
    flag = 0

    for word in keywords:
        if(word in lines[i].lower()):
            flag = 1
    if(flag == 1):
        for word in wgwords:
            if (word in lines[i].lower()):
                flag = 0

    if(flag == 1):
        num = 0
        text = lines[i]
        words = text.split()
        for wordi in words:
            # print(word)
            num = num + 1
        if (num >= 100):
            flag = 0

    if (flag == 1):
        lv = lv + 1
        newf.write(lines[i])
    elif(flag==0):
        print('*',j)
        print(lines[i])

    # #     newf.write('\n')
    # newf.write(lines[i])
    # newf.write('\n')


# print('j:', j)
# print('lv:', lv)

oldf.close()
newf.close()