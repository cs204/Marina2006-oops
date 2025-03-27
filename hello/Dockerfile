# sudo docker build -t hello-python-app .
# sudo docker run -it --rm --name my-running-app hello-python-app

FROM python:3

WORKDIR /app

COPY * ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./hello.py" ]
