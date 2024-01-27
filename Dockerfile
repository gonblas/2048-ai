FROM python:3.11.5

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD [ "python", "src/main.py" ]
