from src import create_app
from dotenv import load_dotenv
import os

load_dotenv()
"""
    Production -> config.Production
    Development -> config.Development
    Test -> config.Test
"""

if __name__ == "__main__":
    app = create_app('config.Development')
    app.run(host='0.0.0.0', port=5000)