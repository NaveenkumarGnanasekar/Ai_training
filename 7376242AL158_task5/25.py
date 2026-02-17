from abc import ABC, abstractmethod
class InferenceStrategy(ABC):

    def preprocess(self, data):
        print("Preprocessing data...")
        return data.strip().lower()

    @abstractmethod
    def infer(self, data):
        pass

    def postprocess(self, result):
        print("Postprocessing result...")
        return f"Final Output: {result}"
class RuleBasedStrategy(InferenceStrategy):
    def infer(self, data):
        print("Using Rule-Based Inference...")
        if "error" in data:
            return "Issue detected"
        return "No issues found"
class MLStrategy(InferenceStrategy):
    def infer(self, data):
        print("Using ML Model Inference...")
        return f"Predicted class for '{data}'"
class InferenceEngine:
    def __init__(self, strategy: InferenceStrategy):
        self.strategy = strategy

    def run(self, data):
        data = self.strategy.preprocess(data)
        result = self.strategy.infer(data)
        return self.strategy.postprocess(result)
data = "System ERROR occurred"


engine1 = InferenceEngine(RuleBasedStrategy())
print(engine1.run(data))
engine2 = InferenceEngine(MLStrategy())
print(engine2.run(data))
