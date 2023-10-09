import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# def generate_prompt(describe):
#     return """describe a dog .

# describe :dog
# describetion : dog is an animal of 4 legs
# describe : parrot
# describetion : parrot is an aniaml  that flys
# describe: {}
# describe:""".format(
#         describe.capitalize()
#     )


def generate_prompt(person):
    return """lavanya works on prowes at age of 24 .
person:jahnavi is working in rightdat at age of 21
json:{
name :jahnavi,
age :21,
company :rightdata
}
person:lavanya works on prowesat age of 24
json :{name :lavanya,
age :24,
company :prowes }
person:""".format(
        person.capitalize()
    )
