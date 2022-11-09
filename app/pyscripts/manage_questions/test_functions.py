from manage_questions.__init__ import create_client, Client, supabase
import json, random

# functions to fetch and insert data in database

def getQuestionIDs():
    # get all question IDs from database

    data = supabase.table("tblQuestions").select("questionID").execute().data
    IDList = []
    for object in data:
        IDList.append(object["questionID"])

    return IDList


def getRandomQuestionData():
    # choose random record from question table

    IDList = getQuestionIDs()
    questionID = random.choice(IDList)
    questionData = supabase.table("tblQuestions").select("*").eq("questionID", questionID).execute().data

    return questionData


def extractQuestionData(questionData, dataName):
    # return data fetched from database as a dictionary

    data = questionData[0].get(f"{dataName}")
    dataJSON = data.replace("'", "\"")
    dataDict = json.loads(dataJSON)

    return dataDict


def uploadScores(studentID, totalScore, maxScore):
    # create new record in score table

    scoreData = {
        "studentID": studentID,
        "score": totalScore,
        "maxScore": maxScore
    }

    supabase.table("tblScores").insert(scoreData).execute()






