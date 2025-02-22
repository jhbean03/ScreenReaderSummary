from flask import Flask, request, jsonify

# Initialize a Flask server 
app = Flask(__name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    # Obtain the JSON data from the HTTPS request
    data = request.get_json()

    # Extract the HTML data from request
    page_html = data.get("html", "")

    # TODO: Place call to summary function here
    summary = "Summary goes here!"

    # Return summary in JSON format
    return jsonify({"summary": summary})

# Set up debug mode option
if __name__ == '__main__':
    app.run(debug=True)

