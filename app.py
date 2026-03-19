import streamlit as st
from transcribe import transcribe_audio
from summarize import generate_summary, extract_action_items
from fpdf import FPDF

st.set_page_config(page_title="AI Meeting Minutes Generator", page_icon="🧠")

st.title("🧠 AI Meeting Minutes Generator")
st.write("Upload meeting audio and generate transcript, summary and action items.")

# initialize variables

transcript = ""
summary = ""
actions = []

# PDF function

def create_pdf(summary, actions):
 pdf = FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=12)


 pdf.cell(200,10,"AI Meeting Minutes Report", ln=True)

 pdf.cell(200,10,"Meeting Summary:", ln=True)
 pdf.multi_cell(0,8,summary)

 pdf.cell(200,10,"Action Items:", ln=True)

for a in actions:
 pdf.cell(200,8,"- " + a, ln=True)

 pdf.output("meeting_report.pdf")


audio_file = st.file_uploader("Upload Meeting Audio", type=["mp3","wav","m4a"])

if audio_file is not None:


 with open("temp_audio.mp3","wb") as f:
    f.write(audio_file.read())
    

 with st.spinner("Transcribing audio..."):
    transcript = transcribe_audio("temp_audio.mp3")

 with st.spinner("Generating summary..."):
    summary = generate_summary(transcript)

 actions = extract_action_items(transcript)

 st.subheader("Transcript")
 st.write(transcript)

 st.subheader("Meeting Summary")
 st.write(summary)

 st.subheader("Action Items")

 if len(actions) > 0:
    for a in actions:
        st.write("- " + a)
 else:
    st.write("No action items detected.")

 create_pdf(summary, actions)

 with open("meeting_report.pdf","rb") as f:
    st.download_button(
        "Download Meeting Report",
        f,
        file_name="meeting_minutes.pdf",
        mime="application/pdf"
    )

