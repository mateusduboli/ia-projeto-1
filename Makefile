all: run

run: window.py main.py
	python main.py

clean:
	rm -rf *.pyc
