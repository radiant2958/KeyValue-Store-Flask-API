FROM python:3.9

WORKDIR /myapp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY myapp/ .

CMD ["python", "run.py"]
