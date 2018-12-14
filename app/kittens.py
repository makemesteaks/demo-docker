import json
import random
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def kittens():
    def print_kittens():
        cats = ["grumpy", "approaching", "tubby", "confused",
                "playful", "thoughtful", "delighted", "nyan", "resting"]
        random_cat = random.choice(cats)

        with open('app/cats.json', 'r') as cat_file:
            cats_dict = json.loads(cat_file.read())
            for i in cats_dict[random_cat]:
                yield i + '\n'
    return Response(print_kittens(), mimetype="text/plain")


#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
