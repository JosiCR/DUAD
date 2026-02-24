import json
import os

class Persistence:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.categories_file = os.path.join(self.data_dir, "categories.json")
        self.transactions_file = os.path.join(self.data_dir, "transactions.json")

    def load_all(self):
        data = {}
        data["categories"] = self._load_file(self.categories_file, default=[])
        data["transactions"] = self._load_file(self.transactions_file, default=[])
        return data

    def save_all(self, data: dict):
        self._save_file(self.categories_file, data.get("categories", []))
        self._save_file(self.transactions_file, data.get("transactions", []))

    def _load_file(self, path, default):
        if not os.path.exists(path):
            return default
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default

    def _save_file(self, path, content):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)