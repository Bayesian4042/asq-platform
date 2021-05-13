FROM frolvlad/alpine-python-machinelearning:latest
RUN pip install --upgrade pip

WORKDIR /app

COPY . /app


RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt

ENTRYPOINT ['python']

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app


