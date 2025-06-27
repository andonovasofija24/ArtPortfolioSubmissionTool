#FROM python:3.9
#WORKDIR /app
##COPY . .
#COPY ../frontend /app/frontend
#RUN pip install -r requirements.txt
#EXPOSE 5000
#CMD ["python", "app.py"]
FROM python:3.9
WORKDIR /app

COPY backend/ /app

COPY frontend/ /app/frontend

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
