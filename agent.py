from anthropic import Anthropic
from prompts.prompts import agent_system_prompt_template
from model.model import anthropic_model
from toolbox.toolbox import ToolBox
from tools.real_quotes import search_eggers_quotes
from tools.fake_quotes import generate_fake_eggers_quotes
from utils.get_key import get_anthropic_api_key, get_model_config
from typing import Dict, List

class EggersQuoteAgent:
    def __init__(self):
        api_key = get_anthropic_api_key()
        self.anthropic = Anthropic(api_key=api_key)
        self.toolbox = ToolBox()
        self.toolbox.add_tool("search_eggers_quotes", search_eggers_quotes)
        self.toolbox.add_tool("generate_fake_eggers_quotes", generate_fake_eggers_quotes)
        self.model_config = get_model_config()

    def get_quote(self, query: str) -> Dict:
        prompt = agent_system_prompt_template.format(
            tool_descriptions=self.toolbox.get_tool_descriptions()
        )
        
        response = anthropic_model(
            system_prompt=prompt,
            user_prompt=query,
            model_config=self.model_config
        )

        tool_choice = response["tool_choice"]
        tool_input = response["tool_input"]

        if tool_choice == "no tool":
            return {"result": tool_input}
        
        tool = self.toolbox.get_tool(tool_choice)
        result = tool(tool_input)
        return result

if __name__ == "__main__":
    agent = EggersQuoteAgent()
    query = input("Enter your query about Dave Eggers quotes: ")
    result = agent.get_quote(query)
    print(result)