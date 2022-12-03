FROM python:3.10.8-alpine
WORKDIR /root/
COPY src/ src/
COPY requirements.txt ./
COPY atcoder-contests-bot-docker /etc/periodic/daily
RUN pip install -r requirements.txt
CMD ["crond", "-f"]
