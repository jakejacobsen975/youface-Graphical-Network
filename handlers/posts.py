import flask
import openai, os
import requests
import base64
import logging
from db import posts, users, helpers


current_dir = os.path.dirname(os.path.abspath(__file__))

# Read the API key from the file in the handlers subdirectory
file_path = os.path.join(current_dir, 'api_key.txt')
with open(file_path, 'r') as file:
    API_KEY = file.read().strip()

blueprint = flask.Blueprint("posts", __name__)
openai.api_key = API_KEY


@blueprint.route('/post', methods=['POST'])
def post():
    """Creates a new post."""
    db = helpers.load_db()


    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    # prompt generation
    meme = flask.request.form.get('post')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": generate_prompt(meme)}],
        temperature=.8,
    )
    response = response['choices'][0]['message']['content']

    if "Top text" in response and "Bottom text" in response:
    # Remove "Top text" and "Bottom text" from the response
        response = response.replace("Top text: ", "").replace("Bottom text: ", ";")

    # image generation 
    imageGen = ImageGenerator()
    imageGen.generateImage(
    Prompt = str(response),
    ImageCount = 1,
    ImageSize = '512x512'
    )
    image = imageGen.downloadImage()

    posts.add_post(db, user, response, image)

    return flask.redirect(flask.url_for('login.index'))

def generate_prompt(meme):
    return """Suggest a top text and bottom text for an absurdist meme.

Subject: Minion
text: Did you fall?; Noo I attacked the floor
Subject: POV
text: POV: your are at a Taylor Swift concert; and she's introducing a new song
Subject: {}
text:""".format(
        meme
    )

@blueprint.route('/rate', methods=['POST'])
def postrate():
    db = helpers.load_db()

    rating = int(flask.request.form.get('sum_rating'))
    post_id = flask.request.form.get('post_id')
    
    posts.rate_post(db, post_id, rating)
    print("someone rated a thing", rating)
    return flask.redirect(flask.url_for('login.index'))


@blueprint.route('/comment', methods=['POST'])
def postComment():
    db = helpers.load_db()

    comment = str(flask.request.form.get('commentPostID'))
    post_id = flask.request.form.get('post_id')

    posts.commentOnPost(db, post_id, comment)
    print("A comment was added on", post_id)
    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/like', methods=['POST'])
def likePost():
    db = helpers.load_db()

    post_id = flask.request.form.get('post_id')
    
    posts.like_post(db, post_id)
    print("someone liked a post")
    return flask.redirect(flask.url_for('login.index'))

class ImageGenerator:
    def __init__(self):
        self.image_url = []
        openai.api_key = API_KEY
        self.APIKey = openai.api_key
        self.image = None

    def generateImage(self, Prompt, ImageCount, ImageSize):
        if not Prompt:
            raise ValueError("Prompt cannot be empty.")
        if ImageSize != "512x512":
            raise ValueError("Size is not 512x512")
        try:
            self.APIKey
            response = openai.Image.create(
                prompt=Prompt,
                n=ImageCount,
                size=ImageSize,
            )
            self.image_url = [image["url"] for image in response["data"]]
            return self.image_url
        except openai.error.InvalidRequestError as e:
            raise e
        except openai.error.APIError as e:
            raise e
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)




    def downloadImage(self):
        try:
            for url in self.image_url:
                response = requests.get(url)
                if response.status_code == 200:
                    b64data = base64.b64encode(response.content)
                    return b64data.decode("utf-8")
                #Error downloading image from URL
                return ValueError
        except Exception as e:
            #An error occurred while downloading image)
            return ValueError
        return None


