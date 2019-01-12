import argparse
import opencv as cv_api

def grey_scale(image):
	return image.convert('LA')

def main():
	print("\nStarting binarization pipeline...")

	parser = argparse.ArgumentParser(description="Binarization pipeline.")
	parser.add_argument('input_image', action='store', help='Input image for pipeline binarization')
	parser.add_argument('output_image', action='store', help='Output image for pipeline binarization')

	args = parser.parse_args()
	print(args)
	print(args.input_image)



	cv_api.opencv_binarization(args.input_image, args.output_image, 127, 255)

	for i in range(0, 255, 4):
		for blur in range(3, 9, 2):
			cv_api.opencv_binarization(args.input_image, args.output_image + "_blur" + str(blur) + "_" + str(i)  + ".png", i, 255, True, blur)
		cv_api.opencv_binarization(args.input_image, args.output_image + "_noblur_" + str(i) + ".png", i, 255, False)

	cv_api.opencv_binarization_otsu(args.input_image, args.output_image + "_otsu")
	for blur in range(3, 9, 2):
		cv_api.opencv_binarization_otsu(args.input_image, args.output_image + "_otsu" + "_blur" + str(blur) + ".png", True, blur)


	cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive.png", 255, 11, 2)
	for window_size in range(3, 19, 2):
		for cst in range(0, 5):
			cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive_noblur" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, False)
			for blur in range(3, 9, 2):
				cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive_blur" + str(blur) + "_" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, True, blur)

	cv_api.opencv_binarization_adaptive_gaussian(args.input_image, args.output_image + "adaptive_gaussian.png", 255, 11, 2)
	for window_size in range(3, 19, 2):
		for cst in range(0, 5):
			cv_api.opencv_binarization_adaptive_gaussian(args.input_image, args.output_image + "_adaptive_gaussian_noblur" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, False)
			for blur in range(3, 9, 2):
				cv_api.opencv_binarization_adaptive_gaussian(args.input_image, args.output_image + "_adaptive_gaussian_blur" + str(blur) + "_" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, True, blur)


	cv_api.opencv_binarization_integral_image(args.input_image, args.output_image + "integral_image.png", 10, 10, False)
	for window_size in range(4, 20, 2):
		for percent in range(10, 90, 10):
			cv_api.opencv_binarization_integral_image(args.input_image, args.output_image + "integral_image_noblur" + str(window_size) + "_" + str(percent)  + ".png", window_size, percent, False)
			for blur in range(3, 9, 2):
				cv_api.opencv_binarization_integral_image(args.input_image, args.output_image + "integral_image_blur" + str(blur) + "_" + str(window_size) + "_" + str(percent)  + ".png", 255, window_size, percent, True, blur)


"""
	im = Image.open(args.input_image)

	greyScaleImage = grey_scale(im)


	greyScaleImage.save(args.output_image)

	print("\nFinishing binarization pipeline...\n")
"""


if __name__ == "__main__":
	main()
