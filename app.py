from flask import Flask
 
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello from the new feature branch!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)