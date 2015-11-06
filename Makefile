.PHONY: all clean

all:
	python src/main.py

clean:
	rm -rf output/*
