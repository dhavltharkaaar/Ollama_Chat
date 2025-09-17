import streamlit as st
from ollama import chat
import fitz  # PyMuPDF for PDFs
import pandas as pd

# Page setup
st.set_page_config(page_title="📄 Doc Chat", page_icon="💬")
st.title("📄 Document Q&A with LLaMA 3.2")

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "doc_context_added" not in st.session_state:
    st.session_state.doc_context_added = False

# File upload
uploaded_file = st.file_uploader("Upload a PDF or Excel file", type=["pdf", "xlsx"])

# PDF text extraction
def extract_pdf_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

# Excel text extraction
def extract_excel_text(file):
    xls = pd.ExcelFile(file)
    return "\n\n".join(df.to_string(index=False) for _, df in xls.parse(sheet_name=None).items())

# Process uploaded file
if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext == "pdf":
        text = extract_pdf_text(uploaded_file)
    elif ext == "xlsx":
        text = extract_excel_text(uploaded_file)
    else:
        text = ""

    st.session_state.doc_text = text
    st.session_state.doc_context_added = False  # Reset on new file upload
    st.success("✅ Document processed successfully.")
    st.text_area("Extracted Document Text", text, height=300)

# Display past chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Accept new user input
prompt = st.chat_input("Your message")

if prompt:
    # Inject document context once as a system message
    if (
        st.session_state.doc_text
        and not st.session_state.doc_context_added
    ):
        st.session_state.messages.insert(0, {
            "role": "system",
            "content": f"You are a helpful assistant. Use the following document content to answer questions:\n\n{st.session_state.doc_text}"
        })
        st.session_state.doc_context_added = True

    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare assistant message UI container
    with st.chat_message("assistant"):
        response_box = st.empty()
        full_response = ""

        try:
            response = chat(
                model="llama3.2:latest",
                messages=st.session_state.messages,
                stream=True
            )

            for chunk in response:
                content = chunk.get("message", {}).get("content", "")
                full_response += content
                response_box.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error from model: {e}"
            response_box.error(full_response)

        # Save assistant response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response
        })
