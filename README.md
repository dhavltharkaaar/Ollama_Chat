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

 - To activate the environment type this code in anaconda prompt:
    ```bash
    conda activate myenv
    ```

  - To deactivate the environment:
    ```bash
    conda deactivate
    ```

###  Libraries needed for the Project:
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-202020?logo=github&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-007ACC?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)

### To install htis libraries into your environment

  - First Activate your environment"
    ```bash
    pip install streamlit ollama pymupdf pandas
    ```
## Or Else Use Below command

  - First Activate your environment"
    ```bash
    conda install streamlit ollama pymupdf pandas
    ```
### By following above steps we have made an environment and established the llama3.2 via ollama

## To start the project we need to follow few steps as mentionaed below:

Note: 
1. Make sure you have done sith ollama download from their websote, then installation process.
2. in command prompt :ollama check and ollama list download.
3. Making an environment in Anaconda Navigator and installing all required libraries

# Lets start the project
1. First open one Anaconda Powersheell Prompt Activate the environment you created and then go to the desired file location where you have store the app.py file.
2. then we will start the ollama server by gining the command to anaconda prompt as below.
3. ollama serve.

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/server1.png" alt="Ollama list" width="600">
4. On some cases ollama serve dont work because of port is alreayy occupied.
5. Use this command instead $env:OLLAMA_HOST ="127.0.0.1:11435
6. then use $env:OLLAMA_HOST
7. In last we will go for ollama serve

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/server%202.png" alt="Ollama list" width="600">

8. for checking ollama is working properly see bow image. You will found the same in your pc or desktop om right bottom.

<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/serverrun.png" alt="Ollama list" width="600">

9. We will open the second anaconda prompt and activeta the environment, then change the path whre th eapp.py is stored.
    
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/app.png" alt="Ollama list" width="600">
10. then run the command streamlit run app.py
11. or you can use python -m streamlit app.py

### Output Screenshots:

### Front or Home Page:
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/output1.png" alt="Ollama list" width="600">

### Conversation between the Assistant and the User without file upload:
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/output2.png" alt="Ollama list" width="600">

### File upload Section:
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/output3.png" alt="Ollama list" width="600">

### Conversation between the chat assistant and user after file uploaded regarding the dov\cument and personal conversation
<img src="https://github.com/dhavltharkaaar/Ollama_Chat/blob/main/images/output4.png" alt="Ollama list" width="600">

## Thank You!!
