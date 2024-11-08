import os
import yaml
from dotenv import load_dotenv

def load_config():
    with open(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml'), 'r') as config_file:
        return yaml.safe_load(config_file)

def get_anthropic_api_key():
    load_dotenv()  
    config = load_config()
    api_key_env_var = config['anthropic']['api_key_env_var']
    api_key = os.getenv(api_key_env_var)
    
    if not api_key:
        raise ValueError(f"Anthropic API key not found. Please set the {api_key_env_var} environment variable.")
    
    return api_key

def get_model_config():
    config = load_config()
    return config['model']

def get_tool_config():
    config = load_config()
    return config['tools']

def get_fake_quote_config():
    config = load_config()
    return config['fake_quotes']