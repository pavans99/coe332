NAME ?= pavanshukla99

all: build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/hw5:latest .

run:
	docker run --name "hw5" -d -p 5030:5000 ${NAME}/hw5:latest

push:
	docker push ${NAME}/hw5:latest
