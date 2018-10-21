import argparse
from PIL import Image

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

	im = Image.open(args.input_image)
	
	greyScaleImage = grey_scale(im)
	
	
	greyScaleImage.save(args.output_image)

	print("\nFinishing binarization pipeline...\n")


if __name__ == "__main__":
	main()
