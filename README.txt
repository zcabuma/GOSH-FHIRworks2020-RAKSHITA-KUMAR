CONTENTS:
=========

GITHUB REPO FOR PROJECT: https://github.com/zcabuma/GOSH-FHIRworks2020-RAKSHITA-KUMAR.git

1. FHIR Hack Main Project
NOTE: the FHIR Hack Main Project is the env/ folder
2. API 
NOTE: the API is the env/flaskAPI folder

HOW TO RUN THE FHIR HACK MAIN PROJECT:
--------------------------------------

1. Run a dotnet file in the background:
	1 - change into the directory that contains the dotnet files ( it maybe called dotnet-azure-fhir-web-api)
	2 - once inside this directory, type the following command: dotnet run
2. Install all the requirements in requirements.txt
   OR :
   1 - in the command line change into the same directory where this README file is located
   2 - enter the following in the command line --> source ./env/bin/activate 
   3 - now you will have a virtual environment running containing all the dependencies
3. now enter the env/ folder (type cd env) and run the following command: python testingFlaskAndDialogFlow.py. The flask file will start running on port 8000
4. Ignore this step if you have already installed all dependencies from requirements.txt
   OTHERWISE:
   open a new terminal:
    1 - in the command line change into same directory where this README file is located
    2 - enter the following in the command line --> c
    3 - now you will have a virtual environment running containing all the dependencies
5. now enter the env/ folder (type cd env) and run the following command ./ngrok http 8000. the command line will turn black. make a note of the https url in the "forwarding" section of the page e.g. https://76a84a62.ngrok.io
6. log onto https://dialogflow.cloud.google.com/ and create a new agent
7. import the file env/DialogflowAgent/latestlatestbot.zip into your new agent
8. in the fullfillment section: activate Webhooks, substitute the url you copied in step 5 following by "/webhook" and click save
In the end your url may look like this: https://76a84a62.ngrok.io/webhook
9. now click test on "google assistant" on the right hand box of the dialogflow console
10. try out the "Talk to my test app". Your ngrok screen should update with as "200 OK" message and you should get the menu pane as a response.

 
HOW TO RUN THE API:
------------------

1. Run a dotnet file in the background:
	1 - change into the directory that contains the dotnet files ( it maybe called dotnet-azure-fhir-web-api)
	2 - once inside this directory, type the following command: dotnet run 
2. Install all the requirements in requirements.txt
   OR :
   1 - in the command line change into the same directory where this README file is located
   2 - enter the following in the command line --> source ./env/bin/activate 
   3 - now you will have a virtual environment running containing all the dependencies
3. go to the directory : env/flaskAPI/
4. then run the following command if you are on a Mac: export FLASK_APP=restAPI.py 
5. then run the following command to run the API: flask run --host 0.0.0.0 --port 8000
6. in a separate terminal run the following command to test the API: curl http://127.0.0.1:8000/GetIntent/hi. You should get the following result back:
{"result":{"code":200,"content":"Default Welcome Intent"}}
7. For more information about the API check the readme file located inside env/flaskAPI.py