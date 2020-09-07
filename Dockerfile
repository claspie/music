FROM python:3

MAINTAINER Omorogbe Usuomon

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["init.py"]

RUN python scraper.py
RUN python app.py