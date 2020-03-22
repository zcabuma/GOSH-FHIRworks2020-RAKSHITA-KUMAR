from flask import Flask, escape, request, jsonify
import dialogflow_v2beta1
import requests, os
from fhir_parser import FHIR 
import FHIRFunctions 


app = Flask(__name__)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 3899462e16cd46d29349ecb710e86c0c',
    }

params = (
    ('v', '20150910'),
    )

@app.route('/getVitalSign/<string:query>', methods = ['GET'])
def get_VitalSign(query):
    try:
        queryAsArray = query.split("-")
        queryOfPerson = ""
        for element in queryAsArray:
            queryOfPerson = queryOfPerson + " " +element

        data = '{\n  "lang": "en",\n  "query": "'+queryOfPerson+'",\n  "sessionId": "12345",\n  "timezone": "America/New_York"\n}'

        response = requests.post('https://api.dialogflow.com/v1/query', headers=headers, params=params, data=data)
        responseJson = response.json()
        parameters = responseJson["result"]["parameters"]
        medParameter = parameters["medParameter"]
        if medParameter.startswith("get") or medParameter.startswith("the"):
            medParameter = medParameter[4:]
        if medParameter.endswith("results"):
            medParameter = medParameter[:-7]
        if medParameter.endswith("for"):
            medParameter = medParameter[:-3]
        if medParameter.endswith("about"):
            medParameter = medParameter[:-5]
        name = parameters["name"][4:]
        uuid = FHIRFunctions.getPatientUUIDFromPatientName(name)
        result = FHIRFunctions.getObservationData(uuid, "vital-signs", medParameter)
        if uuid is None:
            return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist, or the format of the query is unknown to the bot"}}) 

        return jsonify({"result" : {"code" : 200, "content" : result}})
    except:
        return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist or the format of the query is unknown to the bot"}})
    


@app.route('/getLabResults/<string:query>', methods = ['GET'])
def get_LabResults(query):
    try:
        queryAsArray = query.split("-")
        queryOfPerson = ""
        for element in queryAsArray:
            queryOfPerson = queryOfPerson + " " +element

        data = '{\n  "lang": "en",\n  "query": "'+queryOfPerson+'",\n  "sessionId": "12345",\n  "timezone": "America/New_York"\n}'

        response = requests.post('https://api.dialogflow.com/v1/query', headers=headers, params=params, data=data)
        responseJson = response.json()
        parameters = responseJson["result"]["parameters"]
        medParameter = parameters["medParameter"]
        if medParameter.startswith("get") or medParameter.startswith("the"):
            medParameter = medParameter[4:]
        if medParameter.endswith("results"):
            medParameter = medParameter[:-7]
        if medParameter.endswith("for"):
            medParameter = medParameter[:-3]
        if medParameter.endswith("about"):
            medParameter = medParameter[:-5]

        name = parameters["name"][4:]

        uuid = FHIRFunctions.getPatientUUIDFromPatientName(name)
        result = FHIRFunctions.getObservationData(uuid, "laboratory", medParameter)

        if uuid is None:
            return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist, or the format of the query is unknown to the bot"}}) 

        return jsonify({"result" : {"code" : 200, "content" : result}})
    except:
        return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist or the format of the query is unknown to the bot"}})
    


@app.route('/BasicPatientData/<string:query>', methods = ['GET'])
def get_BasicPatientData(query):
    try:
        queryAsArray = query.split("-")
        queryOfPerson = ""
        for element in queryAsArray:
            queryOfPerson = queryOfPerson + " " +element

        data = '{\n  "lang": "en",\n  "query": "'+queryOfPerson+'",\n  "sessionId": "12345",\n  "timezone": "America/New_York"\n}'

        response = requests.post('https://api.dialogflow.com/v1/query', headers=headers, params=params, data=data)
        responseJson = response.json()
        parameters = responseJson["result"]["parameters"]
        name = parameters["name"]    
    
        if name.startswith("for"):
            name = name[4:]
        elif name.startswith("about"):
            name = name[6:]
    
        uuid = FHIRFunctions.getPatientUUIDFromPatientName(name)
        if uuid is None:
            return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist,  or the format of the query is unknown to the bot"}}) 

        
        fhir = FHIR()
        patientObject = fhir.get_patient(uuid)
        result = FHIRFunctions.getBasicPatientInfo(patientObject)
    
        return jsonify({"result" : {"code" : 200, "content" : result}})
    except:
        return jsonify({"error" : {"code" : 404, "message" : "either the user does not exist or the format of the query is unknown to the bot"}})  

@app.route('/GetIntent/<string:query>', methods = ['GET'])
def get_Intent(query):
    try:
        queryAsArray = query.split("-")
        queryOfPerson = ""
        for element in queryAsArray:
            queryOfPerson = queryOfPerson + " " +element

        data = '{\n  "lang": "en",\n  "query": "'+queryOfPerson+'",\n  "sessionId": "12345",\n  "timezone": "America/New_York"\n}'

        response = requests.post('https://api.dialogflow.com/v1/query', headers=headers, params=params, data=data)
        responseJson = response.json()
        result = responseJson["result"]
        metaData = result["metadata"]
        intentName = metaData["intentName"]
    
        return jsonify({"result" : {"code" : 200, "content" : intentName}})
    except:
        return jsonify({"error" : {"code" : 404, "message" : "error while getting intent"}})

@app.route('/ModeOfValue/<string:query>', methods = ['GET'])
def get_MostCommonGender(query):
    try:
        queryAsArray = query.split("-")
        queryOfPerson = ""
        for element in queryAsArray:
            queryOfPerson = queryOfPerson + " " +element

        data = '{\n  "lang": "en",\n  "query": "'+queryOfPerson+'",\n  "sessionId": "12345",\n  "timezone": "America/New_York"\n}'

        response = requests.post('https://api.dialogflow.com/v1/query', headers=headers, params=params, data=data)
        responseJson = response.json()
        parameters = responseJson["result"]["parameters"]
        modeParameter = parameters["modeValue"]

        if "common" in modeParameter:
            modeParameter = modeParameter[7:]
        elif "mode for" in modeParameter:
            modeParameter = modeParameter[9:]
        elif "occurs" in modeParameter:
            modeParameter = modeParameter[:-7]

        if modeParameter == "gender":
            return jsonify({"result" : {"code" : 200, "content" :  {"most common gender" : FHIRFunctions.getMostCommonGender()}}})
        elif modeParameter == "ethnicity":
            return jsonify({"result" : {"code" : 200, "content" :  {"most common ethnicity" : FHIRFunctions.getMostCommonEthnicity()}}})
        elif modeParameter == "race":
            return jsonify({"result" : {"code" : 200, "content" :  {"most common race" : FHIRFunctions.getMostCommonRace()}}})
        elif modeParameter == "marital status":
            return jsonify({"result" : {"code" : 200, "content" :  {"most common marital status" : FHIRFunctions.getMostCommonMaritalStatus()}}})
        else:
            return jsonify({"error" : {"code" : 404, "message" : "We do not have the function to calculate the mode for your data value"}})
    except:
        return jsonify({"error" : {"code" : 404, "message" : "there was a problem when retrieiving the mode."}})


 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
   app.run(debug = True)

