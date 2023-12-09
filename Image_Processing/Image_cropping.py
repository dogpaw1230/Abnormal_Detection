import glob
import cv2
import natsort
import numpy as np

path = './Orig_img/6process/'
file = glob.glob(path + '*.jpg')
img_list = natsort.natsorted(file)

# print(img_list)

for i in img_list:
    # naming code
    files = i.split('OC6S_')[1]
    files1 = files[:].split('.')[0]
    # Image Processing
    img_ori = cv2.imread(i, cv2.IMREAD_COLOR)
    img_gray = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    img_gray = cv2.GaussianBlur(img_gray, (3,3),0)
    img_gray = cv2.dilate(img_gray, (3, 3), iterations=3)
    img_gray = cv2.erode(img_gray, (3, 3), iterations=3)
    ret, thr1 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # contours, hierarchy = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 100, param1=150, param2=50, minRadius=300,
                                maxRadius=400) # small circle
    circles1 = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 100, param1=150, param2=50, minRadius=400, maxRadius=500) # big circle
    # circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 100, None, 200)
    if circles is None:
        print('Cropping is fail : image number %s' % files1)
        continue
    # for cnts in contours:
    #     cv2.drawContours(img_ori, cnts, -1, (0, 255, 0), 3)

    for i in circles[0, :]:
        # cv2.circle(img_ori, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 5)
        # cv2.rectangle(img_ori, (int(i[0])-int(i[1]), 0), (int(i[0])+int(i[1]), 2*int(i[1])), (255, 0, 0), 5)
        # cv2.circle(img_ori, (int(i[0]), int(i[1])), int(i[1]), (255, 0, 0), 5)
        # cv2.circle(img_ori, (int(i[0]), int(i[1])), int((i[1]+i[2])*0.5), (255, 0, 0), 5)

        cv2.circle(img_ori, (int(i[0]), int(i[1])), int(1.23 * (i[2])), (0, 0, 0), -1)


        for j in circles1[0, :]:

            # cv2.circle(img_ori, (int(j[0]), int(j[1])), int(j[2]), (0, 255, 0), 5)
            mask = np.zeros_like(img_ori)
            cv2.circle(mask, (int(j[0]), int(j[1])), int(j[1]), (255, 255, 255), -1)
            masked = cv2.bitwise_and(img_ori, mask)
            final_img = masked[0:2 * int(j[1]), int(j[0]) - int(j[1]):int(j[0]) + int(j[1])]
            cv2.imwrite('./Orig_img/6O_'+str(files1)+'.jpg', final_img)
            # print(final_img.shape)

    # cv2.imshow('img', final_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()