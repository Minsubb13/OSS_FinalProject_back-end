FROM python:3.10

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8080 8081

CMD python main.py