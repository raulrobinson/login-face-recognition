# Face Recognition Backend

Python project for face recognition using OpenCV and InsightFace and FastAPI for REST API.

## Installation

```bash
python -m venv venv
.\venv\Scripts\activate
```

```bash
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
# pip install git+ 
```

### MongoDB

* Install MongoDB
```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

## Usage

* Tag Face in Image from Webcam. **'q'** to quit
```bash
python .\main.py
```

## Swagger

* Swagger UI
```bash
http://localhost:8080/docs
```

* Validate
```bash
curl -X 'POST' \
  'http://localhost:8080/face-id/checkpoint/email' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@example.com"
}'
```

* Register
```bash
curl -X 'POST' \
  'http://localhost:8080/face-id/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "rasysbox@hotmail.com",
  "image": "iVBORw0KGgoAAAANS...iVAlKgAAAABJRU5ErkJggg=="
}'
```

* Login
```bash
curl -X 'POST' \
  'http://localhost:8080/face-id/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "rasysbox@hotmail.com",
  "image": "iVBORw0KGgoAAAANS...iVAlKgAAAABJRU5ErkJggg=="
}'
```


## License
MIT License