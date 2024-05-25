from src import create_app
from src.extensions import db
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":

    if os.getenv('ENV') == 'PRODUCTION':
        app = create_app('config.Production')

    elif os.getenv('ENV') == 'DEVELOPMENT':
        app = create_app('config.Development')

    elif os.getenv('ENV') == 'TEST':
        app = create_app('config.Test')

        with app.app_context():
            db.create_all()
            print("Creating all")
    app.run(host='0.0.0.0', port=5000)