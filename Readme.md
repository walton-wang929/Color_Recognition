# Color Recognition

This repo contains Kmeans and HSV pixel range Color Recognition methods.

## Kmeans

to cluster domianant color of a given box, input is box coordinate(x,y,w,h), return is color name

Advantage: accurate

Disadvantage: Time-consuming

Reference:  [K-Means Clustering in OpenCV](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html)

## HSV pixel range

set up a HSV color look up table first. then compare each pixel of roi image with the look up table, then the largest distribution of color is the dominant.

## demo
![color Recognition](https://github.com/walton-wang929/Color_Recognition/raw/master/demo/Color_recognition.gif)
