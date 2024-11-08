from anthropic import Anthropic
from utils.get_key import get_anthropic_api_key

def anthropic_model(system_prompt: str, user_prompt: str, model_config: dict):
    client = Anthropic(api_key=get_anthropic_api_key())
    
    response = client.completions.create(
        model=model_config['name'],
        prompt=f"{system_prompt}\n\nHuman: {user_prompt}\n\nAssistant:",
        max_tokens_to_sample=model_config['max_tokens'],
        temperature=model_config['temperature']
    )
    
    return response.completion