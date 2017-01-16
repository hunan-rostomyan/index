INDEX_FILE = index.json
PYTHON_BIN = index.py

build_index:
	python3 $(PYTHON_BIN)

clean_python:
	rm -rf *.pyc
	rm -rf __pycache__

clean:
	rm $(INDEX_FILE)
	$(clean_python)
