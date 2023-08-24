#docker build -t python-app .
#docker run -p 5000:5000 python-app
FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]
EXPOSE 5000