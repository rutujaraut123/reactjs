from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        file = request.files.get("file")

        # Save the uploaded file (if provided)
        if file:
            file.save(f"uploads/{file.filename}")

        return f"Name: {name}, Age: {age}, File: {file.filename if file else 'No file uploaded'}"

    # Render the main dashboard
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
