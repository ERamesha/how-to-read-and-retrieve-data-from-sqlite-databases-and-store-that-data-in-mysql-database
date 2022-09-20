import blur_detector
import cv2

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier("C:\\Users\\ramesha\\ZI\image\\11113365.jpg")

    img = cv2.imread('1.png', 0)
    blur_map1 = blur_detector.detectBlur(img, downsampling_factor=1, num_scales=3, scale_start=1)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(blur_map1, (x, y), (x + w, y + h), (255, 0, 0), 2)

    img = cv2.imread('2.png', 0)
    blur_map2 = blur_detector.detectBlur(img, downsampling_factor=1, num_scales=3, scale_start=1)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(blur_map2, (x, y), (x + w, y + h), (255, 0, 0), 2)

    img = cv2.imread('3.png', 0)
    blur_map3 = blur_detector.detectBlur(img, downsampling_factor=1, num_scales=3, scale_start=1)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(blur_map3, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('a', blur_map1)
    cv2.imshow('b', blur_map2)
    cv2.imshow('c', blur_map3)
    cv2.waitKey(0)