import cv2
import os


image_path = os.path.join('.', 'pic', 'picture.jpg')
img = cv2.imread(image_path)

cv2.imwrite(os.path.join('.', 'pic', 'picture_out.jpg'), img)




#resizing image
resized_img = cv2.resize(img, (480,480))

#cropping image
cropped_img = img[300:400,300:400]


#cvt colorspace
diff_colour_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


#applying blur
k_size= 20
img_blur =cv2.blur(img,(k_size,k_size))

#denoising
img_noisy = cv2.imread(os.path.join('.', 'pic', 'noisy.jpg'))


gaussian = cv2.GaussianBlur(img_noisy, (5,5), 0)
median = cv2.medianBlur(img_noisy, 5)
bilateral = cv2.bilateralFilter(img_noisy, 9, 75, 75)

#cv2.imshow('noisy', img_noisy)
#cv2.imshow('gaussian', gaussian)
#cv2.imshow('median', median)
#cv2.imshow('bilateral', bilateral)

#edge detection
edges = cv2.Canny(img, threshold1=100, threshold2=200)



#thresholding
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY) #convert to gray

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)

print(f'Total objects detected: {len(contours)}')
cv2.imshow('Contours', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
