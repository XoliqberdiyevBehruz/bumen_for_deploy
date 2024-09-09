FROM python:3.11.4-slim-bullseye
# set work directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update
COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# create directory for the app user
RUN mkdir -p /home/app


# create the app user

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/locale
WORKDIR $APP_HOME


# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME
RUN chmod +x  $APP_HOME/entrypoint.sh
# copy project
COPY . $APP_HOME

# run entrypoint.prod.sh
RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
