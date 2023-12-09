from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img
import os
import glob
import natsort
import cv2
import PIL

datagen = ImageDataGenerator(
        rotation_range=40,
        horizontal_flip=True,
        fill_mode='constant')

file = glob.glob('./gray_6O/*.jpg')
csv_list = natsort.natsorted(file)
print(csv_list)


for j in csv_list:
    # 숫자 네이밍 용 코드
    files = j.split('6O_')[1]
    files1 = files[:].split('.')[0]
    img = load_img(j)  # PIL 이미지
    x = img_to_array(img)  # ex. (3, 150, 150) 크기의 NumPy 배열
    x = x.reshape((1,) + x.shape)  # ex. (1, 3, 150, 150) 크기의 NumPy 배열

    # 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
    # 지정된 `preview/` 폴더에 저장합니다.
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                            save_to_dir='./gray_6O_gen/', save_prefix=str(files1), save_format='jpg'):

        i += 1
        if i > 1:
            break  # 이미지 20장을 생성하고 마칩니다
            
