# ADM Assignments :- Image Classification Algorithms

## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Vivek Limaye | 001051436
|Saurabh Rakesh Satra  | 001059412 

## Claat Link
https://codelabs-preview.appspot.com/?file_id=1Ah66dDsF4vsxcF0eD7_g5TP3RunNjoydytVgaEoNF5M#0


## About Dataset
Cdiscount image dataset contains information about 9 million products. The dataset contains more than 15 million images at 180x180 resolution divided into more than 5000 categories.

The dataset contains the following files:

#### category_names.csv :- 
The file shows the hierarchy of product classification over category levels level 1, level 2 and level 3 with category_id.

#### Train.bson :- 
It contains over 70 lacs dictionaries, one per product. Each dictionary contains product_id, category_id with an image list. The images are in JPEG format.

#### Train_example.bson :- 
It contains the first 100 records of train.bson file.

#### Test.bson :- 
It contains a list of over 17 lacs products with product_id, category_id, and image list.


## Algortihms

### Similarity Search: Cosine Similarity Algorithm
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. Image Similarity detection is used to quantify the degree of visual and semantic similarity of the images.

### Facebook AI Similarity Search using FAISS
FAISS is a library used for efficient similarity search and clustering of dense vectors. It returns all elements that are within a given radius of the query point. The vector representation for images is designed to produce similar vectors for similar images, where similar vectors are defined that are nearby in Euclidean space.

### Annoy-Spotify Method
Annoy (Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for finding approximate nearest neighbors. This algorithm builds an annoy index by appending all image feature vectors stored in the local folder. There are just two main parameters needed to tune Annoy: the number of trees n_trees and the number of nodes to inspect during searching search_k.
