.PHONY: python3 python

all: run

install:
	@pip install --upgrade -r requirements.txt

uninstall:
	@pip uninstall -y -r requirements.txt

run: clean
	@python3 transl_pdf/transl.py

clean:
	@rm -rf transl_pdf/__pycache__
