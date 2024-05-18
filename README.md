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
 conda create -n prudentllm  python=3.9 -y
```

```bash
conda activate prudentllm
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

```ini
# try to get the google api key form the link -[https://aistudio.google.com/app/u/1/apikey]
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```