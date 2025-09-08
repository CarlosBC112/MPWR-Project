# MPWR Project - FastAPI + Deepgram + Claude

This project is a simple FastAPI app that:
- Accepts audio files and transcribes them using **Deepgram**.
- Sends the transcript to **Claude (Anthropic)** and returns an AI-generated response.
- Provides a small demo web form for file uploads.
- There are two Sections, Section 1 and section 2
- Section 1	Integrating PyCharm + Python + UV + Fast API
- First, download PyCharm, and IDE for Python
https://www.jetbrains.com/pycharm/?source=google&medium=cpc&campaign=AMER_en_US-CST_PyCharm_Branded&term=pycharm&content=698987581563&gad_source=1&gad_campaignid=14127625568&gbraid=0AAAAADloJzgjLF7MC_7Em09_F7yKwPyCO&gclid=CjwKCAjw2vTFBhAuEiwAFaScwj8HlvUFJxgpCZYmRPGNyRNO6DAK1Ru8tu1bFOIIArstDulPRU-ZlhoCrgEQAvD_BwE
After PyCharm is downloaded, open the folder and gain access to PyCharm
After PyCharm is open, Click Create a new Project, a new section should be visible and look similar to the image below 
<img width="598" height="431" alt="image" src="https://github.com/user-attachments/assets/d6043cf2-fbcc-4a62-93e8-fcb646954676" />

Make sure to click “FastAPI”, and configure the interpreter generate a new custom environment. This is so that we may chose UV as the package manager. Configure the options to look like the following below.
<img width="591" height="427" alt="image" src="https://github.com/user-attachments/assets/d7c984d8-4260-48ba-9cf0-0bac4190fb9c" />

After this is done, click create, it might ask if you want to load a new pop up window or your existing one, choose either one that your prefer. Afterwards you should be looking at a new project that has a “main.py” python file and other files. It should look like this 
<img width="653" height="341" alt="image" src="https://github.com/user-attachments/assets/cf1b3bad-2fd8-4e52-b137-def487cbed21" />

To double check that you have a UV interpreter , hit CTRL+ALT+S , and then go 
Settings->Python->Interpreter and make sure that it says “uv (FastAPIProjectName)”
<img width="676" height="506" alt="image" src="https://github.com/user-attachments/assets/232de72a-6709-4639-9595-3a36a0385833" />
After this, one more step is important. On PyCharm, click the button “Terminal”, it is on the lower left of your screen. Make sure to type “pip install uv”, and hit enter. 
AFTER THIS IS DONE, YOU CAN HIT RUN AND OPEN THE PROVIDED HTTP LINK IN ORDER TO VIEW YOUR PROJECT!!
It shoud look something like this, if not identical 
http://127.0.0.1:8000



Section 2 Installing packages + running the Project
Most of the source code needed to run this project is on the file "main.py" , this is where the heart of the source code will be. 
You could clone if youd like but if theres anything you absolutely need, it is the code inside "main.py"
Note that it is a little messy, unfortunately, I had just gotten the code to work about an hour ago, and so without making any changes, I added a versino control to capute the one 
version of this project that works, more refinement will come but for now, this works. 

!IMPORTANT!!! You need to make sure that you install the nessary packages from your terminal, otherwise direct copy and paste wont work, and you will see some compiler errors
On your terminal, make sure to run 
pip install uv

uv add python-dotenv

uv pip install deepgram
uv add deepgram-sdk
uv pip install -r requirements.txt
uv add "deepgram-sdk==2.12.0"
uv add langchain
uv add langchain-anthropic anthropic

This should be mostly it, but if your project folder is missing other packages, make sure to add those via the command prompt. 

ALSO IMPORTANT!!!!
This code works if you have a deepgram API Key and a Claude anthropic API Key, when you get those, you need to create a ".env" file and add the keys there 
Like this 
DG_API_KEY=your_deepgram_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

WHEN YOU HIT RUN ON YOUR PROJECT, IT SHOULD GIVE YOU A HTTP LINK TO VIEW YOUR PROJECT, IT SHOULD BE SIMILAR IF NOT ALMOST IDENTICAL TO THIS 
http://127.0.0.1:8000

Goodluck, and thank you 





