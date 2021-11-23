init:
	cat requirements.txt | xargs -n 1 pip install
	
test:
	py.test tests

run: 
	python ./app/app.py

.PHONY: init test