
class MLModel:
    def __init__(self):
        self.data = []

    def train(self, training_data):
        self.data = training_data
        print(f"{self.__class__.__name__} trained with {training_data}")

    def predict(self, test_data):
        pass

class LinearModel(MLModel):
    def predict(self, test_data):
        avg = sum(self.data) / len(self.data)
        return [avg * x for x in test_data]

class DecisionTreeModel(MLModel):
    def predict(self, test_data):
        threshold = sum(self.data) / len(self.data)
        return ["High" if x > threshold else "Low" for x in test_data]

class KNNModel(MLModel):
    def predict(self, test_data):
        results = []
        for x in test_data:
            closest = min(self.data, key=lambda t: abs(t - x))
            results.append(closest)
        return results

training_data = [10, 20, 30, 40, 50]
test_data = [15, 35, 60]
models = [LinearModel(), DecisionTreeModel(), KNNModel()]
for model in models:
    model.train(training_data)
    print("Predictions:", model.predict(test_data))
    print()
