#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
An expandable, flexible, image recognition system written in Python.

All images (data set and unknown images) must be of the same dimensions.
'''

import ntpath
import difflib
from PIL import Image
import operator

def generator(path):
    '''Take a file path and return a matrix.

    Args:
        path: A relative file path to a target image.

    Returns:
        flat_matrix: A flattened list of pixel values from the image.

    '''

    image = Image.open(path, 'r')
    matrix = list(image.getdata())
    flat_matrix = [x for sets in matrix for x in sets]

    return flat_matrix

def generate_data_set(file_paths):
    '''Generate a labelled data set from a list of file paths.

    Args:
        file_paths: A list of file paths to labelled images.

    Returns:
        data_set: A labelled data set.

    '''

    data_set = {}

    for path in file_paths:
        matrix = generator(path)
        label = ntpath.basename(path)
        data_set[label] = matrix

    return data_set



def main(target_path, data_set={}):
    '''Generate / load a data set and compare to a target image.

    Args:
        target_path: A relative file path to a target image.
        data_set: A labelled data set.

    Returns:
        comparison: A dictionary of each image in the data set and the percentage similarity to the target image.

    '''

    target = generator(target_path)

    comparison = {}

    if data_set:
        for key, value in data_set.items():
            similarity = difflib.SequenceMatcher(None, value, target)
            comparison[key] = similarity.ratio()

    return comparison

if __name__ == '__main__':
    data_set_paths = [
        'dataset/1.png',
        'dataset/2.png',
        'dataset/3.png',
        'dataset/4.png',
        'dataset/5.png',
        'dataset/6.png',
        'dataset/7.png',
        'dataset/8.png',
        'dataset/9.png',
    ]
    target_image_path = 'dataset/unknown5.png'

    data_set = generate_data_set(data_set_paths)

    percentage_comparisons = main(target_image_path, data_set)
    print(percentage_comparisons)

    closest_comparison = max(percentage_comparisons.items(), key=operator.itemgetter(1))[0]
    print("Closest comparison: {}".format(closest_comparison))
