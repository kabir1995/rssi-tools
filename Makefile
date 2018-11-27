install: 
	pip3 install -r requirements.txt

clean:
	rm -rf .cache/ build/ dist/ .mypy_cache/ *.egg-info/ *.log 
	find ./* -name '__pycache__' -type d | xargs -I@ rm -rf @

build-linux:
	pyinstaller --onefile gui/main.py
	mv dist/main rssiTools

build-windows:
	echo "no windows for you"

gui:
	python3 gui/main.py

build-mac:
	echo "no mac for you"

experiment:
	jupyter notebook &

.PHONY: install clean deploy gui experiment
