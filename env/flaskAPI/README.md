# Documentation

# Section 1: Getting started

**Understanding the purpose of the API**
This API is connected to Google Dialogflow. If a developer is looking to make a chatbot to extract patient records stored in the FHIR format then he or she could use the available functions in the following way:

1. Get Vital Sign For Patient --> if a user enters a query for the vital sign e.g. get blood pressure for bob and the developer using API wants to get the answer, then call this part of the API. The keywords will be extracted and the final result / answer to the user's query will be delivered
2. Get Lab Result For Patient --> if a user enters a query for the lab result e.g. get hemoglobin for bob and the developer using API wants to get the answer, then call this part of the API. The keywords will be extracted and the final result / answer to the user's query will be delivered
3. Get Basic Patient Info For Patient --> if a user enters a query asking for the patient details e.g. get details about bob and the developer using API wants to get the answer, then call this part of the API. The keywords will be extracted and the final result / answer to the user's query will be delivered
4. Get Intent --> if a user enters a query e.g. get details about bob and the developer using API wants to get the the intent for this query, then call this part of the API. The intent will be detected and delivered
5. Get Mode  --> if a user enters a query asking about the mode of a certain parameter e.g. mode for race of the patients and the developer using API wants to get the the intent for this query, then call this part of the API. The keywords will be extracted and the final result / answer to the user's query will be delivered




# Section 2: API Functions

**Get Vital Sign For User**
----
  Returns json data about all the results for a single vital sign pertaining to a single user 

* **URL**

  /getVitalSign/<string:query>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `query=[string]`
   
   **Sample queries** <br/>
   FORMAT 1: Get (Med parameter) for (Name) <br />
   EXAMPLE 2: Get Height for Mr Bob Brown <br />  <br />
   FORMAT 2: What is the (Med parameter) for (Name) <br />
   EXAMPLE 2: What is the heart rate for Mr Bob Brown <br />
   
   NOTE: for now only these questions work


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[["Body Height","2012-02-13 00:02:18+00:00","175.8cm"],["Body Height","2011-02-07 00:02:18+00:00","175.8cm"],["Body Height","2013-02-18 00:02:18+00:00","175.8cm"],["Body Height","2016-03-07 00:02:18+00:00","175.8cm"],["Body Height","2014-02-24 00:02:18+00:00","175.8cm"],["Body Height","2015-03-02 00:02:18+00:00","175.8cm"],["Body Height","2017-03-13 00:02:18+00:00","175.8cm"],["Body Height","2018-03-19 00:02:18+00:00","175.8cm"],["Body Height","2019-03-25 00:02:18+00:00","175.8cm"]]`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Message:** `{"error" : "either the user does not exist or the format of the query is unknown to the bot"}`

* **Sample Call:**

  ```
  curl http://127.0.0.1:8000/getVitalSign/what-is-the-height-for-Mr.-Abram53-Weimann465
  curl http://127.0.0.1:8000/getVitalSign/get-blood-pressure-for-Mr.-Abram53-Weimann465
  ```
  
  
**Get Lab Results for a User**
----
  Returns json data about all the results for a single lab results type pertaining to a single user 

* **URL**

  /getLabResults/<string:query>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `query=[string]`
   
   **Sample queries** <br />
   FORMAT 1: Get the (Med parameter) for (name) <br />
   EXAMPLE 2: Get the Hemoglobin for Mr Bob Brown<br />  <br />
   FORMAT 2: What is the (Med parameter) for (name)<br />
   EXAMPLE 2: What is the Hemoglobin for Mr Bob Brown <br />
   
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[["Hemoglobin [Mass/volume] in Blood","2012-02-13 00:02:18+00:00","12.319g/dL"],["Hemoglobin [Mass/volume] in Blood","2017-03-13 00:02:18+00:00","15.994g/dL"]]
`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Message:** `either the user does not exist, or the format of the query is unknown to the bot`

* **Sample Call:**

  ```
  curl http://127.0.0.1:8000/getLabResults/What-is-the-Hemoglobin-for-Mr.-Abram53-Weimann465
  curl http://127.0.0.1:8000/getLabResults/get-the-hemoglobin-for-Mr.-Abram53-Weimann465
  
  ```
  
**Get Basic Patient Information**
----
  This allows the user to get the basic patient information about the patient. 

* **URL**

  /BasicPatientData/<string:query>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `query=[string]`
   
   **Sample queries** <br/>
   FORMAT 1: Details about (name)
   EXAMPLE 1: Details about Mr Bob Brown
   FORMAT 2: Get patient details for (name)
   EXAMPLE 2: Get patient details for Mr Bob Brown
   FORMAT 3: Information about (name)
   EXAMPLE 3: Information about Mr Bob Brown
   FORMAT 4: Basic patient info for (name)
   EXAMPLE 4: Basic patient info for Mr Bob Brown
   
   

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `UUID: b905139e-1601-403c-9d85-f8e3997cdd19\nfull name: Mr. Abram53 Weimann465\ntelecoms: \n['home: 555-462-1974']\ngender: male\nbirthdate: 1965-07-12\naddresses: \n['119 Heidenreich Pathway Unit 24\\nHanson, Massachusetts\\n, US']\nmarital status: Married\nmutliple birth: False\n`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Message:** `either the user does not exist,  or the format of the query is unknown to the bot`


* **Sample Call:**

  ```
  curl http://127.0.0.1:8000/BasicPatientData/details-about-Mr.-Abram53-Weimann465
  curl http://127.0.0.1:8000/BasicPatientData/get-patient-details-for-Mr.-Abram53-Weimann465
  curl http://127.0.0.1:8000/BasicPatientData/information-about-Mr.-Abram53-Weimann465
  curl http://127.0.0.1:8000/BasicPatientData/get-patient-info-for-Mr.-Abram53-Weimann465
  ```
  
**Get Intent**
----
  For any query entered this function lets you determine the Intent of the query i.e. default welcome intent, or getQuantity or get basic patient information

* **URL**

  /GetIntent/<string:query>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `query=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `getQuantity`
    
    
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `error while getting intent`


* **Sample Call:**

  ```
  curl http://127.0.0.1:8000/GetIntent/hi 
  ```
  
  
**Get Mode**
----
  Returns json data about all the results for a single vital sign pertaining to a single user 

* **URL**

  /ModeOfValue/<string:query>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `query=[string]`
   
   **Sample queries** <br/>
   FORMAT 1: What (parameter) occurs the most <br />
   EXAMPLE 2: What ethnicity occurs the most <br />  <br />
   FORMAT 2: What is the most common (parameter) <br />
   EXAMPLE 2: What is the most common ethnicity <br />
   FORMAT 3: What is the mode for (parameter) <br />
   EXAMPLE 3: What is the mode for gender <br />
   
   NOTE: for now only these questions work
   NOTE: for now parameter can only contain the following values : 


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"most common gender":"female"}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Message:** `We do not have the function to calculate the mode for your data value`

* **Sample Call:**

  ```
  curl http://127.0.0.1:8000/ModeOfValue/What-gender-occurs-the-most
  curl http://127.0.0.1:8000/ModeOfValue/What-is-the-most-common-ethnicity
  curl http://127.0.0.1:8000/ModeOfValue/What-is-the-mode-for-race
  ```
