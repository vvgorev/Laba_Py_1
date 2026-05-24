from typing import Protocol, runtime_checkable
from models import Task

@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        pass

def validate_source(source: object) -> TaskSource:
    if not isinstance(source, TaskSource):
        raise TypeError(f"Объект {type(source).__name__} не реализует контракт TaskSource")
    return source
