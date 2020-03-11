FROM python:3

WORKDIR /usr/src/app

COPY ./app .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000


ENTRYPOINT [ "python" ]

CMD [ "src/metrics.py" ]
