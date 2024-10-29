# Face Recognition Base

Python project for face recognition using OpenCV and InsightFace

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

## License
MIT License