# Prudent_Hackathon
## problem Statement
 - Explore the potential of large language model and Generative AI models like GPT for Natural Language Processing Tasks, Such as text Generation, Summarization or Question Answering


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
# make sure the repository does not exist before creating.
 conda create -n prudentllm  python=3.9 -y
```

```bash
conda activate prudentllm
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

```ini
# try to get the google api key form the link -[https://aistudio.google.com/app/u/1/apikey]
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### STEP 04- Try to Ignore the present virtual environment using gitignore
```gitignore
    /.env
    env
```

### STEP 05
    - update the helper.py file
    - update the app.py

### STEP 06 - Running the application on local machine
```bash
# Finally run the following command
streamlit run app.py
```