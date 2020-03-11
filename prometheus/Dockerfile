FROM ubuntu

WORKDIR /usr/src/app

COPY . .

EXPOSE 9090

ENTRYPOINT [ "./prometheus" ]

CMD [ "--config.file=prometheus.yml" ]
