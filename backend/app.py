from flask import Flask
from app.routes import users, rides
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Register blueprints
app.register_blueprint(users.bp)
app.register_blueprint(rides.bp)

app.config["SECRET_KEY"] = "SECRET_KEY"

@app.route('/')
def index():
    return {"message": "Welcome to the ride-sharing app!"}

if __name__ == "__main__":
    app.run(debug=True)
