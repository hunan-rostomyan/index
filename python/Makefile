INDEX_FILE_GLOB = index_*.json
PYTHON_BIN = main.py
WEB_DATA_DIR = web/search/data
WEB_SERVER = web/manage.py
WEB_PORT = 8001


build_index:
	python3 $(PYTHON_BIN)

sync:
	cp $(INDEX_FILE_GLOB) $(WEB_DATA_DIR)

run:
	python $(WEB_SERVER) runserver $(WEB_PORT)

clean:
	rm -rf *.pyc
	rm -rf __pycache__
	rm $(INDEX_FILE_GLOB)
