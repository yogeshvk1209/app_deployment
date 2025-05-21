from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the root route
@app.route('/')
def hello_world():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
