from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize the limiter using the user's IP address
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/login", methods=["POST"])
# Specific limit for the login page: 5 attempts per minute
@limiter.limit("5 per minute") 
def login():
    # Your logic for checking hashed passwords goes here
    return "Login attempt processed"

if __name__ == "__main__":
    app.run()