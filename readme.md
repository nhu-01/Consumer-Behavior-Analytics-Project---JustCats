# Consumer Behavior Analytics Project

This project will analyze various things about some shopping data.

# Cleaning the Data

Data can be cleaned by using cleaner.py as such.

```
python3 cleaner.py [data.py] [clean.py]
```

# Using K-Nearest Neighbor to Predict Store

The store where a family shopped at can be predicted given Family Size, GeoID, Basket Units, and Basket Dollar by using knn.py as such.

```
python3 knn.py train [clean.csv] [model.csv]
python3 knn.py classify [model.csv] k '{"Family Size": 3, "GeoID": 5, "Basket Units": 20, "Basket Dollar": 90}'
```

(Example values given in for the classification, these can be changed)
