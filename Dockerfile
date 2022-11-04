FROM fastapi-deploy:latest

WORKDIR /app

COPY config main.py preprocess.py resnet.py requirements.txt ./

RUN pip3 install -U pip && pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]