import argparse
import cv2 as cv
from os import listdir
import evaluation
from random import shuffle

def main():
    print("Voting initiation...")

    parser = argparse.ArgumentParser(description="Binarization evaluation pipeline")
    parser.add_argument('initial_image', action='store', help='Input path for pipeline binarization') 
    parser.add_argument('input_dir', action='store', help='Input path for pipeline binarization')
    parser.add_argument('debug_path', action='store', help='Debug path for pipeline binarization')
    parser.add_argument('output_path', action='store', help='Ouput path for pipeline binarization')
    args = parser.parse_args()
    
    all_images_paths = listdir(args.input_dir)
    all_images = []
    for path in all_images_paths:
        actual_path = args.input_dir + path
        #print(actual_path)
        img = cv.imread(actual_path, 0)
        all_images.append(img)
	
    initialImg = cv.imread(args.initial_image, 0)

    print("We started with " + str(len(all_images)) + " images.")

    # step 1
    all_images = global_trivials(all_images)
    print("After global trivials we have " + str(len(all_images)) + " images left.")

    write_all_images_debug(all_images, args.debug_path + "step1/")
    # step 2
    all_images = local_trivials(all_images, initialImg)

    print("After local trivials we have " + str(len(all_images)) + " images left.")
    write_all_images_debug(all_images, args.debug_path + "step2/")
    #write_all_images_debug(all_images, "debug/step2/")
    # step 3
    all_images = global_tournament(all_images) #TODO UNCOMMENT
    
    #all_images = local_tournament(all_images)
    #all_images = local_tournament(all_images)
    #all_images = global_tournament(all_images)

    #write_all_images_debug(all_images, "debug/step3/")
    # step 4
    final_image = final_vote(all_images)
    cv.imwrite(args.output_path, final_image)

# step 1 - voting trivial globals
def global_trivials(input_list, min_value=0.1, max_value=0.5):
    result = []
    for img in input_list:
        histog = evaluation.histogramImage(img)
        if histog.blackPercent > min_value and histog.blackPercent < max_value:
            result.append(img)

    return result

def localMean(img, w, h, wp, hp):
    hist = cv.calcHist([img],[0],None,[256],[0,256])
    val = 0
    windowsize = (wp - w) * (hp - h)

    for i in range(len(hist)):
        val += i *  hist[i]
    val = val / windowsize
    return val

def local_trivials(input_list, initialImg, window_size=100, min_value=0.1, max_value=0.5):
    result = []
    for img in input_list:
        height, width = img.shape
        include = True
        for w in range(0, width, window_size):
            if include == False:
                break
            wfin = w + window_size
            if wfin > width:
                wfin = width
            for h in range(0, height, window_size):
                if include == False:
                    break
                hfin = h + window_size
                if hfin > height:
                    hfin = height
                subimg = img[h:hfin,w:wfin]

                localM = localMean(initialImg[h:hfin,w:wfin], w, h, wfin, hfin)

                histog = evaluation.histogramImage(subimg)

                thresholded = histog.whitePercent * 255
                greyscaled = localM[0]
                
                #print("ratio=" + str(thresholded / greyscaled))
                #if abs(thresholded - greyscaled) > 0.001:
                #    print("delta=" + str(abs(thresholded - greyscaled)))
                if histog.blackPercent < min_value or histog.blackPercent > max_value:
                    include = False
                #ratio = thresholded / greyscaled
                #print((thresholded, greyscaled))
                #if ratio > 2 or ratio < 0.5:
                #    include = False
                
        if include == True:
            result.append(img)

    return result

def global_tournament(input_list):
    return input_list
    """
    pixel_map = {}

    total = len(input_list)
    crt = 0
    height = 0
    width = 0
    for img in input_list:
        height, width = img.shape
        for w in range(0, width):
            for h in range(0, height):
                if not ((h,w) in pixel_map):
                    pixel_map[(h,w)] = 0
                if img[h,w] == 255:
                    pixel_map[(h,w)] += 1
        print (str(crt) + "/" + str(total))
        crt += 1

    newImg = input_list[0].copy()
    for w in range(0, width):
        for h in range(0, height):
            #print(str(pixel_map[(h,w)]))
            if pixel_map[(h,w)] < total / 2:
                newImg[h,w] = 0
            else:
                newImg[h,w] = 255
    
    return [newImg]
    """

def local_tournament(input_list):
    result = []
    shuffle(input_list)
    for i in range(0,len(input_list), len(input_list)/4):
        result += global_tournament(input_list[i:i+len(input_list)])

    return input_list
    """
    pixel_map = {}

    total = len(input_list)
    crt = 0
    height = 0
    width = 0
    for img in input_list:
        height, width = img.shape
        for w in range(0, width):
            for h in range(0, height):
                if not ((h,w) in pixel_map):
                    pixel_map[(h,w)] = 0
                if img[h,w] == 255:
                    pixel_map[(h,w)] += 1
        print (str(crt) + "/" + str(total))
        crt += 1

    newImg = input_list[0].copy()
    for w in range(0, width):
        for h in range(0, height):
            #print(str(pixel_map[(h,w)]))
            if pixel_map[(h,w)] < total / 2:
                newImg[h,w] = 0
            else:
                newImg[h,w] = 255
    
    return [newImg]
    """

def final_vote(input_list):
    pixel_map = {}

    total = len(input_list)
    crt = 0
    height = 0
    width = 0
    for img in input_list:
        height, width = img.shape
        for w in range(0, width):
            for h in range(0, height):
                if not ((h,w) in pixel_map):
                    pixel_map[(h,w)] = 0
                if img[h,w] == 255:
                    pixel_map[(h,w)] += 1
        print (str(crt) + "/" + str(total))
        crt += 1

    newImg = input_list[0].copy()
    for w in range(0, width):
        for h in range(0, height):
            #print(str(pixel_map[(h,w)]))
            if pixel_map[(h,w)] < total / 2:
                newImg[h,w] = 0
            else:
                newImg[h,w] = 255
    
    return newImg



def write_all_images_debug(input_list, path):
    i = 0
    for img in input_list:
        cv.imwrite(path + str(i) + ".png", img)
        i += 1

if __name__ == "__main__":
    main()