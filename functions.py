import re
from textblob import TextBlob


def cleanText(text):
    text = re.sub(r"@[A-Za-z0-9]+",'', text)
    text = re.sub(r"#",'', text)
    text = re.sub(r"RT[\s]+",'', text)
    text = re.sub(r"https?:\/\/\S+",'', text)

    return text



def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity



def getPolarity(text):
    return TextBlob(text).sentiment.subjectivity