import os
import glob
import unicodedata

foods = ['감자탕', '김치찜', '도시락', '돈까스', '떡볶이', '볶음밥', '삼겹살 구이', '족발', '짜장면', '삼겹살 구이', '짜장면', '치킨', '토마토파스타', '피자', '햄버거']

print('start')

for food in foods:
    path_i = 'crawling/data/' + food + '/*.jpeg'
    path_l = 'crawling/preprocessing/' + food + '/*.txt'
    imgs = sorted(glob.glob(path_i))
    labels = sorted(glob.glob(path_l))

    print(f'Images: {len(imgs)} Labels: {len(labels)}')

    if len(imgs) != len(labels):
        while len(imgs) != len(labels):
            labels.append('nothing')

    result = []
    i = 0
    for img in imgs:
        label = unicodedata.normalize('NFC', labels[i][27:-4])
        if img[18:-5] == label:
            i += 1
        else:
            result.append(img[18:-5])
            os.remove(img)
    print(f'Removed: {len(result)}')

print('done')

