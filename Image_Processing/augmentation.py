import os
import glob
import natsort
import cv2
import time
from PIL import Image
import sys

# 부풀릴 이미지 입력
file = glob.glob('../2nd data(dec)/test/X22/*.jpg')
img_list = natsort.natsorted(file)
print(img_list)

# 결과 저장 폴더 생성
path = '../augmentation/test/X22/'
os.makedirs(path, exist_ok=True)

# # 저장된 파일 개수 카운터
# COUNT = 1
# angle = [120, 240]

for j in img_list:  
    # 숫자 네이밍 용 코드
    files = j.split('X22/')[1]  # file name : 11O_234.jpg
    files1 = files[:].split('_')[0]  # file class : 11O
    files2 = files[:].split('_')[1]  # file label.jpg : 234.jpg
    files3 = files2[:].split('.')[0]  # file lable : 234  
	
	# 부풀릴 이미지 파일 불러오기
    image = Image.open(j)
    Xdim, Ydim = image.size

	# 저장된 파일 개수 카운터
    COUNT = 1
    angle = [120, 240]

	# 리스트 안의 이미지를 모두 읽어와 i도씩 회전
    for i in angle:
        image = Image.open(j)
        # 변환된 파일을 저장하기 위해 새로운 이름 지정
        new_temp_name = "%05d_" % COUNT
        # 사진이 한 장 만들어질때마다 count를 1씩 증가
        COUNT += 1
        # 사진을 회전시킵니다.
        image = image.rotate(i)
        # 이미지 크기 맞추기 -> resize()
        image = image.resize((Xdim, Ydim))
        # 회전 된 이미지 저장
        image.save(path + new_temp_name + files)
        image.close()

        # 결과물 2개 만들기, 더 만들고 싶다면 숫자 변경 요망
        if COUNT > 3:
            break
    print("Process Done.")

