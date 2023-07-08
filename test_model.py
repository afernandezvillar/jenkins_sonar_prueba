from model import TabularRegressor


def test_tabular_regressor():
    regressor = TabularRegressor()
    x_train = [[1, 2], [3, 4]]
    y_train = [5, 6]

    regressor.train(x_train, y_train)
    y_prediction = regressor.predict([[5, 6], [7, 8]])

    assert len(y_prediction) == 2
