FROM python:3.10-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask","run"]


