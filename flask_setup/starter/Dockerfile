FROM python:3.9

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

RUN mkdir app

RUN cd app

WORKDIR /app

COPY .fs .

RUN pip install --upgrade pip
RUN pip install --upgrade flask-setup
RUN fs install

COPY . .

# TODO: Add all your environment variables here
# ARG DATABASE_URI
# ENV DATABASE_URI=${DATABASE_URI}

RUN flask db upgrade

RUN python manage.py


EXPOSE 80

CMD bash -c "supervisord -c supervisord.conf"