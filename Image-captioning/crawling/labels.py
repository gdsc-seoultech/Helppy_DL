import glob
import os

def label(foldername, label, food):
    filelist = glob.glob(foldername + '/*.txt')

    if not os.path.isdir('trans_'+food):
        os.mkdir('trans_'+food)
    
    for filename in filelist:
        with open(filename, 'r') as f:
            txtlines = ''
            lines = f.readlines()
            for line in lines:
                first_blank = line.find(' ')
                pre_num = line[0:first_blank]
                rm_pre_num = line.lstrip(pre_num)
                after_line = str(label) + rm_pre_num
                txtlines += after_line
            filename = filename[23:]
            with open('trans_' + filename, 'w') as f2:
                f2.write(txtlines)

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

for food in foods.keys():
    path = 'crawling/preprocessing/' + food
    label(path, foods[food], food)

