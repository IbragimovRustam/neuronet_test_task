FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]