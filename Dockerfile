FROM python::3.10-alpine

COPY src /usr/src/app/src
COPY requirements.txt /usr/src/app/src

USER appuser

RUN pip3 install --no-cache-dir -r /usr/src/app/src/requirements.txt
