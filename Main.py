import cv2
from Sort import selection_sort

parrot_img = cv2.imread(r'data/parrot.jpg')
parrot_img = cv2.resize(parrot_img, (int(parrot_img.shape[1]/4), int(parrot_img.shape[0]/4))) #Resized because the image is too big

sorted_parrot, comparison = selection_sort(parrot_img)

cv2.imshow('Result',comparison)
cv2.waitKey()

cv2.imwrite(r'data/sorted_parrot.jpg',sorted_parrot)
cv2.imwrite(r'data/comparison.jpg',comparison)