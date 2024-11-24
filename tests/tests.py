import unittest
from model import *
import joblib
import numpy as np
import pandas as pd


class TestFunctions(unittest.TestCase):

    def testMetric(self):
        model = load_model('Models/modelV1.pkl')
        df = load_data('MarathonData.csv')

        df = preprocess_data(df)
        X = df[['km4week', 'sp4week', 'Wall21', 'Score']].values
        y = df['MarathonTime'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        self.assertTrue(mse<=0.05)
        

if __name__ == "__main__":
    unittest.main()