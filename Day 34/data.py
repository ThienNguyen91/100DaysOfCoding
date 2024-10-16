import requests as rq

data_rq = rq.get(url="https://opentdb.com/api.php?amount=10&category=31&type=boolean")
data_rq.raise_for_status()
data = data_rq.json()
question_data = data["results"]