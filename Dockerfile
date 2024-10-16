FROM python:3.9-alpine

WORKDIR /tema

COPY help.py .
COPY steganography.py .
COPY index.html templates/
COPY encode.html templates/
COPY decode.html templates/
COPY static/style.css static/

RUN pip install --no-cache-dir Flask Pillow

EXPOSE 80

ENV FLASK_APP=help.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

CMD ["flask", "run"]
