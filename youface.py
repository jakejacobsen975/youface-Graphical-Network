# std imports
import time

# installed imports
import flask
import timeago
import tinydb
import sys
import os

# handlers
from handlers import friends, login, posts
API_KEY = ""
app = flask.Flask(__name__)

@app.template_filter('convert_time')
def convert_time(ts):
    """A jinja template helper to convert timestamps to timeago."""
    return timeago.format(ts, time.time())

app.register_blueprint(friends.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(posts.blueprint)

app.secret_key = 'mygroup'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True, host='0.0.0.0',port=5000)

if __name__ == "__main__":
    # Check if a string argument is provided
    if len(sys.argv) > 1:
        API_KEY = sys.argv[1]
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Write the API key to a file in the handlers subdirectory
        file_path = os.path.join(current_dir, 'handlers', 'api_key.txt')
        with open(file_path, 'w') as file:
            file.write(API_KEY)
    else:
        print("Please provide a string as an argument.")
