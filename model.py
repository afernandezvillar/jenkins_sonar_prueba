from  sklearn.linear_model import LinearRegression


class TabularRegressor:
    def __init__(self):
        self.model = None

    def train(self, x_train, y_train):
        self.model = LinearRegression()
        self.model.fit(x_train, y_train)

    def predict(self, x_test):
        return self.model.predict(x_test)
