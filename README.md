# Ollama Chatbot Project Repository

## Description:

This repository contains a mini-project that enables users to upload a document file and interact with it through a chat interface. 
The application acts as a personal assistant, allowing users to ask questions and receive responses based on the content of the uploaded document.

## Requirements to be Downloaded like below:
### Tools Required:

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-44A833?logo=anaconda&logoColor=white)
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/ollamalogo.png?raw=true" alt="Ollama" width="150">

### To Download Ollama click the link below:  
[![Download Ollama](https://img.shields.io/badge/Website-202020?logo=About.me&logoColor=white)](https://ollama.com/download)

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/ollama_download.png" alt="Ollama Download Page" width="600">

## As soon as you dounload the ollama install it in your Desktop for further use.

### Set-up to start ollama
After installation open command prompt and type
First Command as : Ollama

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/cmd.png" alt="Ollama check" width="600">

- After checking that Ollama is installed properly:
  - Run the following command:
    ```bash
    ollama list
    ```
    - Note: On the first run, you will find nothing.

  - Then type the following command:
    ```bash
    ollama run llama3.2
    ```

  - Now type the list command again:
    ```bash
    ollama list
    ```

  - You will now see `llama3.2` listed as shown in the image below:

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/list.PNG" alt="Ollama list" width="600">

### Create a New Environment in Anaconda Prompt

- Open **Anaconda Prompt**.
- Use the following command to create a new environment:

  ```bash
  conda create --name myenv python=3.12

Replace myenv with your desired environment name.
Replace 3.12 with the Python version you need.

Or else
Open Anacond Navigator
1. click on create + to create the new environment
2. give a proper nae for environment
3. select python and version using list option.
4. click on create to create the environment

```bash
# To activate the environment
conda activate myenv

# To deactivate the environment
conda deactivate

## Change the name of the envrionment as per your environment name

## Libraries need for this project

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-202020?logo=github&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-007ACC?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
