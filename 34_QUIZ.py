import requests
import sys

data_path = r'E:\Documents_Files\RobinData\PYTHON\RawDataofpy'
sys.path.append(data_path)

from QUIZ_BRAIN import QuizBrain
from QUIZ_UI import QuizUi

API_URL = "https://opentdb.com/api.php?amount=50&type=boolean"

response = requests.get(API_URL)
response.raise_for_status()
data = response.json()

question_data = data["results"]

quiz = QuizBrain(question_data)
UI = QuizUi(quiz)