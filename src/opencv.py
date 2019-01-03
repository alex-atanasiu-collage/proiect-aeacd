import cv2 as cv
import numpy as np

def opencv_binarization(input_path, output_path, thr, max, blur = True, blurLevel=5, write_frame=True):
	print(input_path + " -> " + output_path + " with thr_val=" + str(thr) + " and max_val=" + str(max))
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.medianBlur(img, blurLevel)

	ret, result = cv.threshold(img, thr, max, cv.THRESH_BINARY)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(result, "thr=" + str(thr), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)

	cv.imwrite(output_path, result)

def opencv_binarization_adaptive(input_path, output_path, max, window, cst, blur=True, blurLevel=5, write_frame=True):
	img = cv.imread(input_path, 0)
	img = cv.medianBlur(img, 5)

	result = cv.adaptiveThreshold(img, max, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, window, cst)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(result, "win=" + str(window) + ",cst=" + str(cst), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)


	cv.imwrite(output_path, result)




#def opencv_adaptiveBinarization(input_path, output_path, levels, 

"""
img = cv.imread('../data/sample1.png',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]


cv.imwrite('../bin/original.png', img)
cv.imwrite('../bin/binarization1.png', th1)
cv.imwrite('../bin/binarization_adapt_mean.png', th2)
cv.imwrite('../bin/binarization_adapt_gauss.png', th3)

print("done")
"""
