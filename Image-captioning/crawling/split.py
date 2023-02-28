import os
import glob
import shutil
import random
import pickle
import numpy as np

def name2num():
    if not os.path.isdir('imgs'):
        os.mkdir('imgs')
    if not os.path.isdir('labels'):
        os.mkdir('labels')

    foods = ['감자탕', '김치찜', '도시락', '돈까스', '떡볶이', '볶음밥', '삼겹살 구이', '짜장면', '치킨', '토마토파스타', '피자', '햄버거']
    new = 0

    for food in foods:
        path_i = 'crawling/data/' + food + '/*.jpeg'
        path_l = 'crawling/trans_preprocessing/trans_' + food + '/*.txt'
        img = sorted(glob.glob(path_i))
        label = sorted(glob.glob(path_l))
        i = 0

        print(food)
        for j in range(len(img)):
            before_img = img[j]
            after_img = 'imgs/' + str(j+new) + '.jpeg'
            shutil.copy(before_img, after_img)  

            before_label = label[i]
            after_label = 'labels/' + str(j+new) + '.txt'  
            shutil.copy(before_label, after_label)  
            
            i += 1
        new += len(img)

def train_test_split():
    test = random.sample(range(930), 100)
    train = [i for i in range(930) if i not in test]
    data = {
        'split': {
            'train': train,
            'test': test
        }
    }

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def captionAndbox():
    data = {'caption':{}, 'boxes':{}}

    foods = {'감자탕': 'a bowl of gamjatang', 
        '김치찜': 'a bowl of kimchi stew',
        '도시락': 'a set of lunch boxes', 
        '돈까스': 'a plate of pork cutlet', 
        '떡볶이': 'a bowl of tteokbokki',
        '볶음밥': 'a boul of fired rice', 
        '삼겹살 구이': 'a bowl of grilled pork belly', 
        '짜장면': 'a bowl of jajangmyeon', 
        '치킨': 'a plate of chicken', 
        '토마토파스타': 'a plate of pasta', 
        '피자': 'a plate of pizza', 
        '햄버거': 'a set of hamburgers'}
    new = 0

    for food in foods.keys():
        print(food)
        path = 'crawling/preprocessing/' + food + '/*.txt'
        filelist = sorted(glob.glob(path))

        for j in range(len(filelist)):
            with open(filelist[j], 'r') as f:
                lines = f.readlines()
                for line in lines:
                    first_blank = line.find(' ')
                    pre_num = line[0:first_blank]
                    box = np.array(list(map(float, line.lstrip(pre_num).split())))
                    caption = str(foods[food])
                data['boxes'][str(j+new)] = box
                data['caption'][str(j+new)] = caption
        new += len(filelist)
    print(len(data['boxes']), len(data['caption']))
    with open('./region.pkl', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
captionAndbox()
