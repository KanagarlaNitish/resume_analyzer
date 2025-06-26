import PyPDF2

def extract_text_from_pdf(file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        text = "Error reading PDF: " + str(e)
    return text.lower()
