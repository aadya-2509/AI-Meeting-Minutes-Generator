AI Meeting Minutes Generator

This project is an AI-powered application that converts meeting audio into structured meeting minutes, including a summary and action items.

Features

Upload audio recordings of meetings

Convert speech to text using Whisper

Generate concise meeting summaries

Extract key action items

Download results as a PDF report

Simple and interactive UI using Streamlit

Tech Stack

Python

Streamlit

OpenAI Whisper (Speech-to-Text)

Hugging Face Transformers (Text Processing)

FPDF (PDF generation)

FFmpeg (Audio processing)

Project Structure

AI-Meeting-Minutes-Generator/
│── app.py
│── transcribe.py
│── summarize.py
│── action_items.py
│── utils.py
│── requirements.txt
│── README.md
│── screenshots/
│ ├── result.png
│ └── pdf.png

How to Run

Install dependencies:
py -m pip install -r requirements.txt

Install FFmpeg and add it to system PATH

Run the application:
streamlit run app.py

Usage

Open the application in your browser

Upload a meeting audio file

Wait for transcription and processing

View the meeting summary and action items

Download the generated PDF report

Screenshots
Result
App
PDF 

Future Improvements

Speaker identification

Better UI/UX design

Real-time transcription

Integration with meeting platforms

Author

Aadya Sharma

License

This project is for educational purposes.

