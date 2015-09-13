all:

cli: docker

server: 
	sudo docker run -p 5000:5000 coffesploit python csf_server.py

docker: docker/Dockerfile src
	cp -r src docker/ &&\
	sudo docker build -t coffesploit docker



clean: docker/src
	rm -r docker/src

