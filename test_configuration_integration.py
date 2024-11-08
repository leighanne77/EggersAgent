# test_config_integration.py
import os
import yaml
import unittest
from utils.get_key import load_config

class TestConfigIntegration(unittest.TestCase):
    def setUp(self):
        """Set up test case by storing the config path"""
        self.config_path = os.path.join(os.path.dirname(__file__), 'configs', 'config.yaml')
        
    def test_config_file_exists(self):
        """Test if config file exists"""
        self.assertTrue(os.path.exists(self.config_path), f"Config file not found at {self.config_path}")

    def test_config_file_readable(self):
        """Test if config file is readable and has valid YAML"""
        try:
            with open(self.config_path, 'r') as file:
                config = yaml.safe_load(file)
            self.assertIsInstance(config, dict, "Config file should load as dictionary")
        except yaml.YAMLError as e:
            self.fail(f"Failed to parse YAML: {e}")
            
    def test_load_config_function(self):
        """Test if load_config function properly loads environment variables"""
        # Load the config
        load_config(self.config_path)
        
        # Read expected values directly from yaml
        with open(self.config_path, 'r') as file:
            expected_config = yaml.safe_load(file)
        
        # Check each key in config is properly set in environment
        for key, expected_value in expected_config.items():
            env_value = os.getenv(key)
            self.assertIsNotNone(env_value, f"Environment variable {key} not set")
            self.assertEqual(env_value, str(expected_value), 
                           f"Environment variable {key} has value {env_value}, expected {expected_value}")

    def test_anthropic_api_key_loaded(self):
        """Test specifically for ANTHROPIC_API_KEY"""
        load_config(self.config_path)
        api_key = os.getenv('ANTHROPIC_API_KEY')
        self.assertIsNotNone(api_key, "ANTHROPIC_API_KEY not found in environment")
        self.assertTrue(len(api_key) > 0, "ANTHROPIC_API_KEY is empty")
        # Optional: Check if it has expected format
        self.assertTrue(api_key.startswith('sk-'), "ANTHROPIC_API_KEY should start with 'sk-'")

    def test_no_empty_values(self):
        """Test that no empty values are loaded from config"""
        with open(self.config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        empty_keys = [k for k, v in config.items() if not v]
        self.assertEqual(len(empty_keys), 0, 
                        f"Found empty values for keys: {empty_keys}")

if __name__ == '__main__':
    unittest.main(verbosity=2)