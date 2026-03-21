# Consumer Behavior Analytics Project

This project will analyze various things about some shopping data.

# Cleaning the Data

Data can be cleaned by using cleaner.py as such:

```
python3 cleaner.py [data.py] [clean.py]
```

# Splitting the Data

The data can be split into training and testing data as such:

```
python3 splitData.py [clean.csv]
```

# Using K-Nearest Neighbor to Predict Store

The store where a family shopped at can be predicted given Family Size, GeoID, Basket Units, and Basket Dollar by using knn.py as such:

```
python3 knn.py train [train.csv] [model.csv]
python3 knn.py classify [model.csv] k '{"Family Size": 3, "GeoID": 5, "Basket Units": 20, "Basket Dollar": 90}'
```
or
```
python3 knn.py train [train.csv] [model.csv]
python3 knn.py test [model.csv] k [test.csv]
```
