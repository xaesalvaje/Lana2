import json

class Config:
    @staticmethod
    def load_config(file_path):
        with open(file_path, "r") as file:
            config = json.load(file)
        return config

def some_utility_function():
    # Implement utility function
    pass
