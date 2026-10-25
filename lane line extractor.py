import cv2
import numpy as np
img = cv2.imread("road.png")
x = cv2.resize(img,(800,600))

def orig_img():
    small = cv2.resize(img,(800,600))
    print(img.shape)
    cv2.imshow("Road Image", small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def hsv_img():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    small = cv2.resize(hsv,(800,600))
    cv2.imshow("HSV Image", small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    lower_white = (0, 0, 180)
    upper_white = (180, 60, 255)

    mask = cv2.inRange(small, lower_white, upper_white)

    cv2.imshow("White Lane Mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blur_img():
    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Blurred Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def canny_img():
    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 150,200)

    cv2.imshow("Canny Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def roi_img():
    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)

    height, width = edges.shape

    mask = edges.copy() * 0

    points = np.array([[
    (0, height - 1),
    (width - 1, height - 1),
    (int(width * 0.85), int(height * 0.55)),
    (int(width * 0.15), int(height * 0.55))
    ]], dtype=np.int32)



    cv2.fillPoly(mask, points, 255)

    roi = cv2.bitwise_and(edges, mask)

    cv2.imshow("ROI Edges", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():

   while True:
    choice = int(input("1-original,2-hsv,3-blur,4-canny,5-roi,-1-exit::"))
    print("\n")

    if choice==1:
        orig_img()

    elif choice==2:
        hsv_img()

    elif choice==3:
        blur_img()

    elif choice==4:
        canny_img()

    elif choice==5:
        roi_img()


    elif choice==-1:
        break


main()