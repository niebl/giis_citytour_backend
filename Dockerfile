FROM python

ADD index.py .
ADD classes.py .
ADD .env .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./index.py"]