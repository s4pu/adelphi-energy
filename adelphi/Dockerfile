# pull the official base image
FROM python:3.8.3-alpine
RUN apk update && \
    apk add gcc musl-dev
ENV DockerHOME /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
WORKDIR $DockerHOME 
RUN pip install --upgrade pip 
COPY ./requirements.txt $DockerHOME
RUN pip install -r requirements.txt
COPY . $DockerHOME
EXPOSE 2345 
CMD ["python", "manage.py", "runserver", "0.0.0.0:2345"]
