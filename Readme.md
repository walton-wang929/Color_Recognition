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

## reference
1.[node-colour-extractor: Extract colour palettes from images](https://github.com/josip/node-colour-extractor)

2.[Color Thief: Grabs the dominant color or a representative color palette from an image.](https://github.com/lokesh/color-thief/)

3.[Color Extractor:a library and a CLI tool to extract the dominant colors of the main object of an image](https://github.com/algolia/color-extractor)

4.[How We Tackled Color Identification?--a blog](https://blog.algolia.com/how-we-handled-color-identification/)

5.[Image Background Removal](https://making.lyst.com/2014/02/13/background-removal/)

6.[Opencv: Interactive Foreground Extraction using GrabCut Algorithm](https://docs.opencv.org/3.4.0/d8/d83/tutorial_py_grabcut.html)
