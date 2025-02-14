FROM python:3.9.17-bookworm

# Allow statements and log messages to immediately appear in logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image
ENV APP_HOME /back-end
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 300 app:app