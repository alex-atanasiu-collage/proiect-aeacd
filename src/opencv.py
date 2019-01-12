import cv2 as cv
import numpy as np

def opencv_binarization_otsu(input_path, output_path, blur = True, blurLevel=5, write_frame=False):
	print(input_path + " -> " + output_path)
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.GaussianBlur(img,(blurLevel,blurLevel),0)

	thr, result = cv.threshold(img,125,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		# cv.putText(result, "thr=" + str(thr), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)

	cv.imwrite(output_path, result)
	
def opencv_binarization(input_path, output_path, thr, max, blur = True, blurLevel=5, write_frame=False):
	print(input_path + " -> " + output_path)
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.medianBlur(img, blurLevel)

	ret, result = cv.threshold(img, thr, max, cv.THRESH_BINARY)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(result, "thr=" + str(thr), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)

	cv.imwrite(output_path, result)

def opencv_binarization_adaptive(input_path, output_path, max, window, cst, blur=True, blurLevel=5, write_frame=False):
	print(input_path + " -> " + output_path)
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.medianBlur(img, blurLevel)

	result = cv.adaptiveThreshold(img, max, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, window, cst)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(result, "win=" + str(window) + ",cst=" + str(cst), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)


	cv.imwrite(output_path, result)

def opencv_binarization_adaptive_gaussian(input_path, output_path, max, window, cst, blur=True, blurLevel=5, write_frame=False):
	print(input_path + " -> " + output_path)
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.medianBlur(img, blurLevel)

	result = cv.adaptiveThreshold(img, max, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, window, cst)

	if write_frame:
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(result, "win=" + str(window) + ",cst=" + str(cst), (0, 20), font, 0.8, (128, 128,128), 2, cv.LINE_AA)


	cv.imwrite(output_path, result)

	
def opencv_binarization_integral_image(input_path, output_path, window, percent, blur=True, blurLevel=5, write_frame=False):
	print(input_path + " -> " + output_path)
	img = cv.imread(input_path, 0)
	if blur:
		img = cv.medianBlur(img, blurLevel)
		
	
	intImg = cv.integral(img)
	intImg = intImg[1:,1:]
	
	result = img
	
	width, height = intImg.shape[:2]
	for i in range(0, width):
		for j in range(0, height):
			
			x1 = i - window / 2
			if x1 < 0:
				x1 = 0
				
			x2 = i + window / 2
			if x2 > width - 1:
				x2 = width - 1
			
			y1 = j - window / 2
			if y1 < 0:
				y1 = 0
			
			y2 = j + window / 2
			if y2 > height - 1:
				y2 = height - 1

			count  = (x2 - x1) * (y2 - y1)
			
			sum = intImg[x2, y2] - intImg[x2, y1] - intImg[x1, y2] + intImg[x1, y1]
			# print (img[i, j], count, sum)
			if img[i, j] * count <= sum * ((100 - percent) / float(100)):
				result[i, j] = 0
			else:
				result[i, j] = 255
				
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