from typing import Any

class fake_collection:
    def __init__(self, *_obj: Any) -> None:
        pass

    def append(self, item):
        ...

    def add(self, item):
        ...

    def remove(self, item):
        ...

    def pop(self) -> Any:
        ...

    def insert(self, item, index):
        ...
