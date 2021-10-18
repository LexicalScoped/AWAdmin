from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello, World\n"


# In case of direct app debugging, uncomment below.
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
