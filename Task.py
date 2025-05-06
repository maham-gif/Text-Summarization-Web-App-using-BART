from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

# Load the summarization model at startup
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Text Summarizer</title>
</head>
<body>
    <h1>Text Summarizer</h1>
    <form method="POST">
        <label for="text">Enter text to summarize:</label><br>
        <textarea name="text" rows="10" cols="50" required></textarea><br>
        <input type="submit" value="Summarize">
    </form>
    {% if summary %}
        <h2>Summary:</h2>
        <p>{{ summary }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = None
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            result = summarizer(text, max_length=100, min_length=30, do_sample=False)
            summary = result[0]['summary_text']
    return render_template_string(html_template, summary=summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
