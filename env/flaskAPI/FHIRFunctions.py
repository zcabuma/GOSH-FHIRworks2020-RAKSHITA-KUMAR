import matplotlib.pyplot as plt
from fhir_parser import FHIR
import os, csv
from krakenio import Client
import datetime
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt



def maritalStatus():
    fhir = FHIR()
    patients = fhir.get_all_patients()

    marital_status = {}
    for patient in patients:
        if str(patient.marital_status) in marital_status:
            marital_status[str(patient.marital_status)] += 1
        else:
            marital_status[str(patient.marital_status)] = 1


    plt.bar(range(len(marital_status)), list(marital_status.values()), align='center')
    plt.xticks(range(len(marital_status)), list(marital_status.keys()))
    plt.show()

def getPatientPageWithPageNumber(i):
    fhir = FHIR()
    patients = fhir.get_all_patients()
    specific_patient = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
    first_page_patients = fhir.get_patient_page(i)
    return first_page_patients

def getPatientNumberOnPage(page, patientNumber):
    return page[patientNumber]



def getPatientUUIDFromPatientName(patientName):
    fhir = FHIR()
    patients = fhir.get_all_patients()
    for patient in patients:
        if patientName == patient.name.full_name:
            return patient.uuid #need to fix in case they dont enter full name

def getPatientObservationsTypeWithPatientUUID(patientUUID, typeOfObs):
    fhir = FHIR()
    observations = fhir.get_patient_observations(patientUUID)
    resultObservationUUID = []
    resultStatus = []
    resultEffectiveDatetime = []
    resultComponents = []
    for observation in observations:
        if observation.type == typeOfObs:
            resultObservationUUID.append(observation.uuid)
            resultStatus.append(observation.status)
            resultEffectiveDatetime.append(observation.effective_datetime)
            resultComponents.append(observation.components)

    return resultObservationUUID, resultStatus, resultEffectiveDatetime, resultComponents

def getObservationData(patientUUID, typeOfObs, dataYouWishToCollect):
    resultFromExactMatch = getObservationDataUsingExactMatch(patientUUID, typeOfObs, dataYouWishToCollect)
    if(len(resultFromExactMatch) != 0):
        return resultFromExactMatch 
    else:
        return getObservationDataUsingIn(patientUUID, typeOfObs, dataYouWishToCollect)


def getObservationDataUsingExactMatch(patientUUID, typeOfObs, dataYouWishToCollect):
    resultObservationUUID, resultStatus, resultEffectiveDatetime, resultComponents = getPatientObservationsTypeWithPatientUUID(patientUUID,  typeOfObs)
    result = []
    for i in range(0, len(resultComponents)):
        for element in (resultComponents[i]):
            if dataYouWishToCollect.replace(' ', '').lower() == str(element.display).replace(' ', '').lower():
                result.append( (element.display, str(resultEffectiveDatetime[i]) , element.quantity() ) )
    return result

def getObservationDataUsingIn(patientUUID, typeOfObs, dataYouWishToCollect):
    resultObservationUUID, resultStatus, resultEffectiveDatetime, resultComponents = getPatientObservationsTypeWithPatientUUID(patientUUID,  typeOfObs)
    result = []
    for i in range(0, len(resultComponents)):
        for element in (resultComponents[i]):
            if dataYouWishToCollect.replace(' ', '').lower() in str(element.display.lower()).replace(' ', ''):
                result.append( (element.display, str(resultEffectiveDatetime[i]) , element.quantity() ) )
    return result


def getBasicPatientInfo(patientRecord):

    result = ""
    result = result + "UUID: " + patientRecord.uuid + '\n'
    result = result + "full name: " + str(patientRecord.name.full_name)+ '\n'
    result = result + "telecoms: \n" + str([record.use + ": " + str(record.number) for record in patientRecord.telecoms])+ '\n'
    result = result + "gender: "  + str(patientRecord.gender)+ '\n'
    result = result + "birthdate: " + str(patientRecord.birth_date)+ '\n'
    result = result + "addresses: \n" + str([record.full_address for record in patientRecord.addresses])+ '\n'
    result = result + "marital status: " + str(patientRecord.marital_status)+ '\n'
    result = result + "mutliple birth: " + str(patientRecord.multiple_birth)+ '\n'
    return result


def getAllBasicPatientInfo(patientRecord):
    return patientRecord.uuid, str(patientRecord.name.full_name), str([record.use + ": " + str(record.number) for record in patientRecord.telecoms]), str(patientRecord.gender), str(patientRecord.birth_date), str([record.full_address for record in patientRecord.addresses]), str(patientRecord.marital_status), str(patientRecord.multiple_birth)  

def checkIfPatientExistsAndReturnUUID(patientName):
    fhir = FHIR()
    patients = fhir.get_all_patients()

    listOfPatients = []
    for patient in patients:
        splittedFullName = str(patient.name.full_name).split(' ')
        patientNameSplitted = patientName.split(' ')
        if len(patientNameSplitted ) == 3 : #so full name has been entered
            if(patientName == patient.name.full_name):
                listOfPatients.append((str(patient.name.full_name), patient.uuid, patient))
        elif len(patientNameSplitted ) == 2 : #so only first and last name has been entered
            if(patientNameSplitted[0] == splittedFullName[0] and patientNameSplitted[1] == splittedFullName[1]):
                listOfPatients.append((str(patient.name.full_name), patient.uuid, patient))
        elif len(patientNameSplitted) == 1 : #so only first or last name has been entered
            if(patientNameSplitted[0] == patientName or patientNameSplitted[1] == patientName):
                listOfPatients.append((str(patient.name.full_name), patient.uuid, patient))

    return listOfPatients


def getMostCommonGender():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    countDict = {}
    maximumCount = -1
    maxValue = ""
    for patient in patients:
        gender = patient.gender
        valSet = -1
        currVal = ""
        if gender not in countDict:
            countDict[gender] = 1
            valSet = 1
            currVal  = gender
        else:
            countDict[gender] = countDict[gender] + 1
            valSet = countDict[gender] + 1
            currVal = gender
        if valSet > maximumCount:
            maximumCount = valSet
            maxValue = currVal
    return maxValue

def getMostCommonMaritalStatus():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    countDict = {}
    maximumCount = -1
    maxValue = ""
    for patient in patients:
        marital_status = str(patient.marital_status)
        valSet = -1
        currVal = ""
        if marital_status not in countDict:
            countDict[marital_status ] = 1
            valSet = 1
            currVal  = marital_status
        else:
            countDict[marital_status] = countDict[marital_status] + 1
            valSet = countDict[marital_status] + 1
            currVal = marital_status
        if valSet > maximumCount:
            maximumCount = valSet
            maxValue = currVal
    return maxValue


def getMostCommonRace():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    countDict = {}
    maximumCount = -1
    maxValue = ""
    for patient in patients:
        race = str(patient.get_extension('us-core-race'))
        valSet = -1
        currVal = ""
        if race not in countDict:
            countDict[race] = 1
            valSet = 1
            currVal  = race
        else:
            countDict[race] = countDict[race] + 1
            valSet = countDict[race] + 1
            currVal = race
        if valSet > maximumCount:
            maximumCount = valSet
            maxValue = currVal
    return maxValue

def getMostCommonEthnicity():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    countDict = {}
    maximumCount = -1
    maxValue = ""
    for patient in patients:
        Ethnicity = str(patient.get_extension('us-core-ethnicity'))
        valSet = -1
        currVal = ""
        if Ethnicity not in countDict:
            countDict[Ethnicity] = 1
            valSet = 1
            currVal  = Ethnicity
        else:
            countDict[Ethnicity] = countDict[Ethnicity] + 1
            valSet = countDict[Ethnicity] + 1
            currVal = Ethnicity
        if valSet > maximumCount:
            maximumCount = valSet
            maxValue = currVal
    return maxValue



