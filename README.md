#  Spicy Image Recognition
An expandable, flexible, image recognition system written in Python.

Original code, completely written from scratch. Works best with binary (ie.: two) color images, as current method of comparison lacks capability to deal with colour.

### Theory
1. Take a labelled data set, e.g.: a series of photos of each letter of the alphabet.
2. Convert this data set into a set of matrices.
3. Take an unlabelled photo and convert it into a matrix.
4. Compare each item in the data set with the unknown image, and determine percentage similarity.

 - All images are converted to black and white binary matrices.