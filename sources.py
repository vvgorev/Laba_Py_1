import json
from models import Task


class FileTaskSource:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_tasks(self) -> list[Task]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]


class GeneratorTaskSource:
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        tasks = []
        for i in range(1, self.count + 1):
            tasks.append({
                "id": f"gen-{i}",
                "payload": {"action": "generate", "value": i}
            })
        return tasks


class ApiTaskSource:
    def __init__(self, url: str):
        self.url = url

    def get_tasks(self) -> list[Task]:
        print(f"[Mock API] Fetching data from {self.url}...")
        return [
            {"id": "api-1", "payload": "Data from API"},
            {"id": "api-2", "payload": "More API data"}
        ]