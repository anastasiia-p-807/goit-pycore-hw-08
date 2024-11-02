import json


class Config:
    def __init__(self):
        self._config_file = "config.json"
        self.load_config()

    def load_config(self):
        with open(self._config_file, 'r') as file:
            config = json.load(file)
            self.filename = config.get('FileName')

    @property
    def FileName(self) -> str:
        return self.filename
