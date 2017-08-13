from flask import Flask
from xkcdpass import xkcd_password as xp


app = Flask(__name__)

word_list = xp.generate_wordlist()


@app.route('/')
def get_new_password():
    return xp.generate_xkcdpassword(word_list)

if __name__ == '__main__':
    app.run()
