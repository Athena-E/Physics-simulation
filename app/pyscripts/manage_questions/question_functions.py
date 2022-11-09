from manage_questions.__init__ import create_client, Client, supabase, json

# functions to fetch and insert question data in database

def uploadQuestionData(teacherID, environmentProperties, particleProperties, simulationProperties, hiddenProperties):
    # creates new record in question table with question properties

    questionData = {
        "teacherID": teacherID,
        "environmentProperties": environmentProperties,
        "particleProperties": particleProperties,
        "simulationProperties": simulationProperties,
        "hiddenProperties": hiddenProperties
    }

    supabase.table("tblQuestions").insert(questionData).execute()


def getQuestionData(teacherID, environmentProperties, particleProperties, simulationProperties, hiddenProperties):
    # returns question properties formatted as a JSON object to upload to database

    questionData = {
        "teacherID": teacherID,
        "environmentProperties": environmentProperties,
        "particleProperties": particleProperties,
        "simulationProperties": simulationProperties,
        "hiddenProperties": hiddenProperties
    }

    return json.dumps(questionData, indent=4)


def getSimulationProperties(timeElapsed, screenW, screenH):
    # returns simulation properties formatted as a JSON object to upload to database

    simulationProperties = {
        "timeElapsed": timeElapsed,
        "screenW": screenW,
        "screenH": screenH
    }

    return json.dumps(simulationProperties)



