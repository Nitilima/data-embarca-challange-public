FROM node:18

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

RUN npm install -g serverless

WORKDIR /usr/src/app

COPY . .

RUN python3 -m venv /usr/src/app/venv
RUN /usr/src/app/venv/bin/pip install --upgrade pip
RUN /usr/src/app/venv/bin/pip install -r requirements.txt

ENV SERVERLESS_ORG=${SERVERLESS_ORG}
ENV SERVERLESS_TOKEN=${SERVERLESS_TOKEN}

RUN serverless login --org $SERVERLESS_ORG --token $SERVERLESS_TOKEN

CMD ["serverless", "deploy"]
