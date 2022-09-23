FROM python:3

WORKDIR /magikker

RUN apt install -y libmagickwand-dev
RUN pip install --no-cache --upgrade pip setuptools wand discord.py

COPY . .

CMD [ "python", "./magikker.py" ]
