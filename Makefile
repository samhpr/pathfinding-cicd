# astar makefile
build:
	pip install --no-cache-dir -r requirements.txt

test:
	pytest --maxfail=1 --disable-warnings -q

lint:
	flake8 . --exit-zero

docker-image:
	docker build -t pathfinding:latest .

docker-run:
	docker run --rm \
		--mount type=bind,source=/tmp,target=/tmp \
		pathfinding:latest

