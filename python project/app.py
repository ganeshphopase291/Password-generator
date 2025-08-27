from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Route for Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_upper = request.form.get("uppercase")
        use_lower = request.form.get("lowercase")
        use_digits = request.form.get("digits")
        use_special = request.form.get("special")
        
        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if characters:
            password = "".join(random.choice(characters) for _ in range(length))
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)