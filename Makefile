install: 
	pip3 install -r requirements.txt

clean:
	rm -rf .cache/ build/ dist/ .mypy_cache/ *.egg-info/ *.log 
	find ./* -name '__pycache__' -type d | xargs -I@ rm -rf @

build:
	pyinstaller --onefile gui/test.py
	mv dist/test rssiTools

	


# Docker 

docker-build:
	docker build -t rssi_tools:latest .

docker-run:
	docker run --rm rssi_tools:latest "test.py"

.PHONY: install clean deploy
