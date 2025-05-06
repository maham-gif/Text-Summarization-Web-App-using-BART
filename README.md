# Text-Summarization-Web-App-using-BART
A simple and interactive web application built with Flask that allows users to input long pieces of text and receive concise summaries. This project utilizes the BART-Large-CNN model from Hugging Face's transformers library to generate high-quality summaries in real time.
📝 Text Summarization Web App using BART

A simple Flask-based web application that uses Hugging Face's `facebook/bart-large-cnn` model to summarize long pieces of text into concise summaries.

 🚀 Features

- 📄 Input any long-form text via a web interface
- 🤖 Real-time summarization using a pre-trained transformer model
- 📉 Adjustable summary length via model configuration
- 🧠 Powered by the `facebook/bart-large-cnn` model from Hugging Face
- 🔧 Lightweight and easy to deploy locally



 🛠 Tech Stack

- Backend: Python, Flask
- NLP Model: `facebook/bart-large-cnn` via Hugging Face Transformers
- Frontend: HTML (via Flask templates)

 📦 Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/text-summarizer-app.git
   cd text-summarizer-app


2. Create a virtual environment and activate it (optional but recommended):

   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required packages:

   bash
   pip install flask transformers

4. Run the application:

   bash
   python app.py
   

5. Open in your browser:
   Visit `http://localhost:5000` to use the app.


📂 Project Structure

text-summarizer-app/
│
├── app.py                # Main Flask app
├── templates/            # (Optional if you separate HTML files)
│   └── index.html        # HTML template (if not using render_template_string)
├── static/               # For CSS/JS if needed in future
├── README.md             # Project documentation

🔧 Model Details

Model Name:`facebook/bart-large-cnn`
Task:Text Summarization
Source:[Hugging Face Model Hub](https://huggingface.co/facebook/bart-large-cnn)

💡 Future Improvements

 Add file upload support (PDF, .txt)
 Allow setting summary length via UI
 Provide summarization history
 Add REST API endpoint

 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork the repo and submit improvements.


📄 License

This project is licensed under the MIT License.




Let me know if you want me to create a `requirements.txt` file or help you upload this to GitHub!
