import cv2 as cv
import argparse

class HistogramData:
    def __init__(self, black, white):
        self.black = black
        self.white = white
        self.total = black + white

        if self.total == 0:
            self.blackPercent = 0.0
            self.whitePercent = 0.0
        else:
            self.blackPercent = float(self.black) / self.total
            self.whitePercent = float(self.white) / self.total

def histogram(image_path):
    img = cv.imread(image_path, 0)
    hist = cv.calcHist([img],[0],None,[256],[0,256])

    return HistogramData(int(hist[0][0]), int(hist[-1][0]))

def main():
    parser = argparse.ArgumentParser(description="Binarization pipeline.")
    parser.add_argument('input_image', action='store', help='Input image for pipeline binarization')
	
    args = parser.parse_args()
    histog = histogram(args.input_image)

    #print("Black: " + str(histog.black) + "Whilte: " + str(histog.white))
    #print("Total: " + str(histog.total))
    print(args.input_image + "," + str(histog.blackPercent) + "%," + str(histog.whitePercent) + "%")


if __name__ == "__main__":
    main()