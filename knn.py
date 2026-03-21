'''
Student Names: Zach, Nhu
Date:
'''

import pandas as pd
import sys
import math
import json

dtype: dict = {
    "HHID": int,
    "GeoID": int,
    "Trans Date": str,
    "Distinct Pro": int,
    "Basket Units": int,
    "Basket Dollar": float,
    "Day-of-Week": str,
    "Family Size": int,
    "Race": str,
    "Income": int,
    "Home Ownership": str,
    "Male Education": str,
    "Male Occupation": str,
    "Female Age": str,
    "Female Work": str,
    "Chldrn 0-5": str,
    "Chldrn 6-11": str,
    "Chldrn 12-17": str,
    "Markets": str,
    "Chains": str,
    "Outlets": str,
    "UPC": str,
    "UPC Description": str,
    "Category": str,
    "Vendor": str,
    "Brand": str,
    "SKU Dollars": str,
    "SKU Units": str,
    "Size": float,
    "SizeUnit": int
}

class KNN:
    def __init__(self, k: int, evaluator) -> None:
        self.k: int = k
        self.evaluator = evaluator
        self.data: list = []

    def train(self, data: pd.DataFrame):
        self.data = list(
            map(
                lambda x: (self.evaluator(x[1]), x[1]),
                data.iterrows()
            )
        )
        
        self.data.sort(key=lambda x: x[0])

    def load_from_csv(self, filename: str) -> None:
        df = pd.read_csv(filename)
        self.data = list(
            map(
                lambda x: (x[1]["position_value"], x[1]),
                df.iterrows()
            )
        )

    def save_to_csv(self, filename: str) -> None:
        data: list = list(map(
            lambda x: dict({"position_value": x[0]}, **x[1]),
            self.data
        ))

        pd.DataFrame(data=data).to_csv(filename, index=False)

    def classify(self, datapoint: dict, answerer):
        point_value = self.evaluator(datapoint)

        step_size = len(self.data) // 2
        list_pos = step_size

        while point_value != self.data[list_pos][0] and step_size > 1:
            step_size = step_size // 2
            if self.data[list_pos][0] > point_value:
                list_pos -= step_size
            else:
                list_pos += step_size

        neighbors: list = []
        left_move: int = 1
        right_move: int = 0

        while len(neighbors) < self.k:
            if list_pos - left_move >= 0:
                left_dist: int = abs(
                    self.data[list_pos - left_move][0] - point_value
                )
            else:
                left_dist: int = sys.maxint

            if list_pos + right_move < len(self.data):
                right_dist: int = abs(
                    self.data[list_pos + right_move][0] - point_value
                )
            else:
                right_dist: int = sys.maxint

            if right_dist < left_dist:
                neighbors.append(self.data[list_pos + right_move])
                right_move += 1
                continue

            neighbors.append(self.data[list_pos - left_move])
            left_move += 1

        return answerer(neighbors)

    def test(self, df: pd.DataFrame, answerer) -> float:
        total: int = df.size
        correct: int = 0
        
        for row in df.iterrows():
            ans = self.classify(row[1], answerer)
            if ans == row[1]["UPC"]:
                correct += 1

        return correct / total

def largest_of(d: dict) -> str:
    largest: tuple[str, int] = ("none", 0)

    for key in d:
        if d[key] > largest[1]:
            largest = (key, d[key])
        elif d[key] == largest[1]:
            largest = ("tie", d[key])

    return largest

def answerer(neighbors):
    d: dict = {}
    largest: tuple[str, int] = ("none", 0)

    while largest[0] == "none" or largest[0] == "tie":
        d = {}
        for neighbor in neighbors:
            upc: str = neighbor[1]["UPC"]
            if upc not in d:
                d[upc] = 0
            d[upc] += 1
        largest = largest_of(d)
        neighbors = neighbors[:-1]

    return largest[0]

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"This file is used like this: 'python3 {__file__} train [data.csv] [model.csv]'")
        print(f"or like: python3 {__file__} classify [model.csv] k '{{\"Family Size\":3,\"GeoID\":5,\"Basket Units\":20,\"Basket Dollar\":90}}'")
        print(f"or like: python3 {__file__} test [model.csv] k [test.csv]")
        quit()
    
    match sys.argv[1]:
        case "train":
            knn: KNN = KNN(0, lambda x: math.sqrt(
                x["Family Size"] ** 2 +
                x["GeoID"] ** 2 +
                x["Basket Units"] ** 2 +
                x["Basket Dollar"] ** 2
            ))

            print("Training will take a moment!")
            
            knn.train(pd.read_csv(sys.argv[2]))
            knn.save_to_csv(sys.argv[3])

            print(f"Output {sys.argv[3]}")

        case "classify":
            knn: KNN = KNN(int(sys.argv[3]), lambda x: math.sqrt(
                x["Family Size"] ** 2 +
                x["GeoID"] ** 2 +
                x["Basket Units"] ** 2 +
                x["Basket Dollar"] ** 2
            ))

            knn.load_from_csv(sys.argv[2])

            print(knn.classify(
                json.loads(sys.argv[4]),
                answerer
            ))

        case "test":
            knn: KNN = KNN(int(sys.argv[3]), lambda x: math.sqrt(
                x["Family Size"] ** 2 +
                x["GeoID"] ** 2 +
                x["Basket Units"] ** 2 +
                x["Basket Dollar"] ** 2
            ))

            knn.load_from_csv(sys.argv[2])

            print(f"""Accuracy: {knn.test(
                pd.read_csv(sys.argv[4]),
                answerer
            )}""")
