PY=python3
PYFLAGS=-m flask --app
TARGET=main

all:
	@$(PY) $(PYFLAGS) $(TARGET) run