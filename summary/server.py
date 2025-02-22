from flask import Flask, request, jsonify
from generate_summary import generate_summary

# Initialize a Flask server 
app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    # Obtain the JSON data from the HTTPS request
    data = request.get_json()

    # Extract the HTML data from request
    page_html = data.get("html", "")

    # Generate summary for the webpage
    summary = generate_summary()

    # Return summary in JSON format
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)

