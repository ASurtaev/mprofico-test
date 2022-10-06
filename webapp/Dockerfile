FROM python:3.10
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /usr/src/app/
CMD [ "python", "app.py" ]