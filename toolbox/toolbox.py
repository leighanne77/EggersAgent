from typing import Dict, Callable

class ToolBox:
    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def add_tool(self, name: str, func: Callable):
        self.tools[name] = func

    def get_tool(self, name: str) -> Callable:
        return self.tools.get(name)

    def get_tool_descriptions(self) -> str:
        descriptions = []
        for name, func in self.tools.items():
            descriptions.append(f"{name}: {func.__doc__}")
        return "\n".join(descriptions)