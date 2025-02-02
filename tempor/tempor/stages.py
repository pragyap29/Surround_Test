from surround import Estimator, SurroundData, Validator


class TemporData(SurroundData):
    input_data = None
    output_data = None


class ValidateData(Validator):
    def validate(self, surround_data, config):
        if not surround_data.input_data:
            raise ValueError("'input_data' is None")

class Main(Estimator):
    def estimate(self, surround_data, config):
        surround_data.output_data = surround_data.input_data

    def fit(self, surround_data, config):
        print("TODO: Train your model here")
