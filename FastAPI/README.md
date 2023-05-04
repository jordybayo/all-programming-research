# Installation
virtualenv venv
source venv/bin/activate
pip install fastapi
pip install uvicorn

# run app
uvicorn main:app --reload

