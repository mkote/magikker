build:
	docker build -t magikker . --no-cache

run:
	docker run -d -e API_TOKEN="$(API_TOKEN)" magikker
