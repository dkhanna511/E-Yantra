########################################################################################
#                                                                                       #
# Team Id            eYRC_943                                                           #
# Author List        Hitesh Bhojwani, Dheeraj Khanna, Komal Bagai, Nikunj Kumar Agarwal #
# Filename           task1A_main.py                                                     #
# Theme              Harvester Bot                                                      #
# Fuctions           writecsv, main, angle                                              #
# Modules imported   cv2, numpy, os, math                                               #
########################################################################################


# classes and subclasses to import
import cv2
import numpy as np
import os
import math
import time
start=time.time()
filename='results1A_943.csv'
#################################################################################################
# DO NOT EDIT!!!
##################
# ###############################################################################
# subroutine to write rerults to a csv
def writecsv(color, shape):
    global filename
    # open csv file in append mode
    filep = open(filename, 'a')
    # create string data to write per image
    datastr = "," + color + "-" + shape
    # write to csv
    filep.write(datastr)
    filep.close()


def main(path):

#####################################################################################################
# Write your code here!!!
    contours = {}
    approx = []
    scale = 0.5                                                                                                         #setting font sise for test
    list = []                                                                                                           #creating an epmty list

    def angle(pt1, pt2, pt0):                                                                                           #function to calculate angle for the shape
        dx1 = pt1[0][0] - pt0[0][0]
        dy1 = pt1[0][1] - pt0[0][1]
        dx2 = pt2[0][0] - pt0[0][0]
        dy2 = pt2[0][1] - pt0[0][1]
        return float((dx1 * dx2 + dy1 * dy2)) / math.sqrt(float((dx1 * dx1 + dy1 * dy1)) * (dx2 * dx2 + dy2 * dy2) + 1e-10)

    image = path                                                                                                        #setting image from the ath selected
    list.append(path)                                                                                                   #appeding image in the list
    frame = cv2.imread(image)                                                                                           #reading the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                                                      #converting the image to grayscale
    canny = cv2.Canny(frame, 200, 200)                                                                                  #canny edge detection
    kernel = np.ones([5, 5], "uint8")                                                                                   #creating numpy array


    mask_blue = cv2.inRange(frame, (250,0,0),(255,10,10))                                                              #setting the threshold range for blue mask
    mask_blue = cv2.dilate(mask_blue, kernel)                                                                           #masking for blue color

    mask_red = cv2.inRange(frame, (0,0,250), (255,10,10))                                                                 #setting the threshold range for red mask
    mask_red = cv2.dilate(mask_red, kernel)                                                                             #masking for red color

    mask_green = cv2.inRange(frame, (0,250,0), (10,255,10))                                                           #setting the threshhold range for  green mask
    mask_green = cv2.dilate(mask_green, kernel)                                                                         #masking for green color

    mask_orange = cv2.inRange(frame, (0,50,200), (180,200,255))                                                        #setting the threshold range for orange mask
    mask_orange = cv2.dilate(mask_orange, kernel)                                                                       #masking for orange color

    canny2, contours, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                   #contour detection for blue color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "blue"
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"

        elif (len(approx) == 4):                                                                   #logic for shape having 4 to 6 edges
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                if ar >= 0.99 and ar <= 1.01:                                                                           #logic for square
                    shape = "square"

                else:                                                                                                   #logic for rectangle
                    shape = "rectangle"

        elif (len(approx) == 5):                                                                    #logic for pentagon
            shape = "pentagon"


        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"

        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)
        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape)                                                                             #appending the shapes and colors in the list
        list.append(element)                                                                                            #appending the sublist to the list
        writecsv(color,shape)                                                                                           #calling writecsv function

    canny2, contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                    #contour detection for red color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "red"
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vetices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"

        elif (len(approx) == 4):                                                                                        #logic for shape having 4 to 6 edges
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                           #logic for square
                shape = "square"

            else:                                                                                                   #logic for rectangle
                shape = "rectangle"

        elif (len(approx) == 5):                                                                                            #logic for pentagon
            shape = "pentagon"

        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating the radius of circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"
        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)
        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape)
        list.append(element)                                                                                            #appending the shapes and colors in the list
        writecsv(color,shape)                                                                                           #calling writecsv function

    canny2, contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                  #contour detection for green color
    for i in range(0, len(contours)):                                                                                   #initiating loop
        color = "green"
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"

        elif (len(approx) == 4):                                                                   #logic for shape having 4 to 6 edges
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                           #logic for square
                shape = "square"

            else:                                                                                                   #logic for rectangle(
                shape = "rectangle"

        elif (len(approx) == 5):                                                                                            #logic for pentagon
            shape = "pentagon"

        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius for circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"

        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)
        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape)                                                                             #appending the shapes and colors in the list
        list.append(element)                                                                                            #appending the sublist into the list
        writecsv(color,shape)                                                                                           #calling writecsv function

    canny2, contours, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                 #contour detection for blue color
    for i in range(0, len(contours)):                                                                                   #initiating the loop
        color = "orange"
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True) * 0.04, True)                           #finding the vertices
        if (abs(cv2.contourArea(contours[i])) < 100 or not (cv2.isContourConvex(approx))):
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if (len(approx) == 3):                                                                                          #logic for triangle
            shape = "triangle"

        elif (len(approx) == 4):                                                                   #logic for shape having 4 to 6 edges                                                                                              #logic for shaoe having 4 edges
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.99 and ar <= 1.01:                                                                           #logic for square
                shape = "square"

            else:                                                                                                   #logic for rectangle
                shape = "rectangle"

        elif (len(approx) == 5):
            shape="pentagon"

        else:                                                                                                           #logic for circle
            area = cv2.contourArea(contours[i])
            radius = w / 2                                                                                              #calculating radius of the circle
            if (abs(1 - (float(w) / h)) <= 2 and abs(1 - (area / (math.pi * radius * radius))) <= 0.2):
                shape = "circle"

        cv2.putText(frame, color, (x + w / 3, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,                #putting text color over image
                    cv2.LINE_AA)
        cv2.putText(frame, shape, (x + w / 3, y + (h / 2) + 15), cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), 1,         #putting text shape over image
                    cv2.LINE_AA)
        img = cv2.drawContours(frame, contours, -1, (0, 0, 0), 1)                                                       #drawing contours
        element = []                                                                                                    #creating  a sublist
        element.append(color + "-" + shape)                                                                             #appending the shapes and colors in the list
        list.append(element)                                                                                            #appending the sublist to the list
        writecsv(color,shape)                                                                                           #calling writecsv function


    cv2.imshow("image",frame)                                                                                           #showing the output image
    temp = filter(lambda x: x != "t", path)                                                                             #logic to remove  the word "test" fromt the name of the output image
    temp = filter(lambda x: x != "e", temp)
    temp = filter(lambda x: x != "s", temp)
    temp = filter(lambda x: x != "t", temp)
    output_name= "output" +temp                                                                                         #appending "output" to the number of image with extension .png
    cv2.imwrite(output_name, frame)                                                                                     #saving the output image
    #cv2.waitKey(0)                                                                                                      #wating for the user to print any key
    cv2.destroyAllWindows()                                                                                             #closing all the opened windows
    return list                                                                                                         #returning list when main() is called
#####################################################################################################


#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
# main where the path is set for the directory containing the test images
if __name__ == "__main__":
    mypath = '.'
    # getting all files in the directory
    onlyfiles = []
    for f in os.listdir(mypath):
        if f.endswith(".png"):
            onlyfiles.append(f)
    #onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if f.endswith(".png")]
    # iterate over each file in the directory
    for fp in onlyfiles:
        # Open the csv to write in append mode
        filep = open(filename, 'a')
        # this csv will later be used to save processed data, thus write the file name of the image
        filep.write(fp)
        # close the file so that it can be reopened again later
        filep.close()
        # process the image
        data = main(fp)
        print data
        elapsed_time=time.time()-start
        print elapsed_time
        # open the csv
        filep = open(filename, 'a')
        # make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        # close the file
        filep.close()
