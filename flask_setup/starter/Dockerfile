FROM python:3.9

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

RUN mkdir app

RUN cd app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# TODO: Add all your environment variables here
# ARG DATABASE_URI
# ENV DATABASE_URI=${DATABASE_URI}

RUN flask db upgrade

RUN python manage.py


EXPOSE 80

CMD bash -c "supervisord -c supervisord.conf"