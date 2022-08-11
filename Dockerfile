FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install wget curl unzip -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; exit 0
RUN apt --fix-broken install -y

WORKDIR /root
RUN curl -Lo chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/`curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"`/chromedriver_linux64.zip
RUN mkdir -p "chromedriver/stable" && unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable" && chmod +x "chromedriver/stable/chromedriver"

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py /app

ENTRYPOINT [ "python", "main.py" ]
