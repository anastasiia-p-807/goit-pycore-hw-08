import pickle
import json
from dataclasses import dataclass
from AddressBook import AddressBook
from Config import Config


@dataclass
class AddressBookFileManager:
    config: Config
    filename: str = None

    def __post_init__(self):
        self.filename = self.config.FileName

    def save_data(self, data):
        if not self.filename:
            raise ValueError("Filename is not set in configuration.")
        with open(self.filename, "wb") as f:
            pickle.dump(data, f)
        print("Log Info: address book was saved successfully.")

    def load_data(self):
        if not self.filename:
            raise ValueError("Filename is not set in configuration.")
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
            print("Log Info: address book was loaded successfully.")
            return data
        except FileNotFoundError:
            return {} # not the best option, but ok for testing and reviewing hw