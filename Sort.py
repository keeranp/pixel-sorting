import cv2
import numpy as np

def selection_sort(img):
    result = np.zeros((img.shape[0], img.shape[1] * 2, 3), np.uint8)
    result[:,:img.shape[1]] = img
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            max_brightness = -1
            selected_col = j
            for k in range(j, img.shape[1]):
                color = img[i,k]
                brightness = 0.114*color[2] + 0.587*color[1] + 0.299*color[0]
                if brightness > max_brightness:
                    selected_col = k
                    max_brightness = brightness
                    
            pixel = img[i,selected_col]
            img[i,selected_col] = img[i,j]
            img[i,j]= pixel

            if j % int(img.shape[1]/5) == 0:
                result[:,img.shape[1]:] = img
                cv2.imshow('Process', result)
                cv2.waitKey(1)
    cv2.destroyAllWindows()
    return img, result