# astar makefile
build:
	pip install --no-cache-dir -r requirements.txt

test:
	pytest --maxfail=1 --disable-warnings -q

lint:
	flake8 .

docker-image:
	docker build -t pathfinding:latest .

