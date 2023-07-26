#pip install SpeechRecognition reportlab

import speech_recognition as sr
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as audio_file:
        audio_data = recognizer.record(audio_file)

        try:
            transcribed_text = recognizer.recognize_google(audio_data)
            return transcribed_text
        except sr.UnknownValueError:
            return "Error: Could not understand the audio."
        except sr.RequestError as e:
            return f"Error: {e}"

def save_to_pdf(transcribed_text, output_file_path):
    doc = SimpleDocTemplate(output_file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    content = [Paragraph(transcribed_text, styles["Normal"])]
    doc.build(content)

if __name__ == "__main__":
    audio_file_path = "path_to_audio_file.wav"  # Replace with the path to your audio file
    output_file_path = "output_transcription.pdf"  # Replace with your desired output PDF file path

    result = transcribe_audio(audio_file_path)
    print("Transcription Result:")
    print(result)

    # Save the transcription to a PDF file
    save_to_pdf(result, output_file_path)
    print(f"Transcription saved to {output_file_path}")
