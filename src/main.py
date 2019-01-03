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


	cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive.png", 255, 11, 2)
	for window_size in range(3, 19, 2):
		for cst in range(0, 5):
			cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive_noblur" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, False)
			for blur in range(3, 9, 2):
				cv_api.opencv_binarization_adaptive(args.input_image, args.output_image + "_adaptive_blur" + str(blur) + "_" + str(window_size) + "_" + str(cst)  + ".png", 255, window_size, cst, True, blur)


"""
	im = Image.open(args.input_image)

	greyScaleImage = grey_scale(im)


	greyScaleImage.save(args.output_image)

	print("\nFinishing binarization pipeline...\n")
"""


if __name__ == "__main__":
	main()
