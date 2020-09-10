import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import numpy as np
import pandas as pd
import pickle

def PredictNote(G1, G2):
    data = pd.read_csv("./student-mat.csv", sep=";")

    data = data[["G1", "G2", "G3"]]

    predict = "G3"
    
    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])


    """
    best = 0

    for i in range(30):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        print(acc)

        if acc > best:
            with open("model.pickle", 'wb') as f:
                pickle.dump(linear, f)


    print(float(best))"""

    with open("model.pickle", 'rb') as f:
        linear = pickle.load(f)

    G1 = int(getNote(G1))
    G2 = int(getNote(G2))
    x_predict = np.array([[G1, G2]])

    prediction = linear.predict(x_predict)

    return toNote(prediction)


def getNote(G):
    NOTES = ["FX", "F", "E", "D", "C", "B", "A"]
    X = 2.85714286
    GRADE = [X*0, X*1, X*2, X*3, X*4, X*5, X*6, X*7]

    return GRADE[NOTES.index(G)]


def toNote(prediction):
    NOTES = ["FX", "F", "E", "D", "C", "B", "A"]
    X = 2.85714286
    return NOTES[int(prediction/X)]

if __name__ == '__main__':
	print(PredictNote(input(">>> "), input(">>> ")))