PY=python3
PYFLAGS=-m flask --app
TARGET=main

all:
	@$(PY) $(PYFLAGS) $(TARGET) run

send:
	git add .
	git commit -m "commit by make"
	git push