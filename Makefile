#
#  Custom make-sequence used on Linux machines. 
#  
#  run with 'make .PHONY' 
#


# Initialize project dependencies 
init: requirements.txt app/requirements.txt venv/bin/activate
	@echo 'Fethcing dependencies...'
	@pip install -r requirements.txt -q
	@python3.8 -m venv venv 
	@./venv/bin/pip3.8 install -r requirements.txt -q
	@pipreqs ./app/ --force 

# Run native test sequences 
test_native:
	python3.8 -m unittest discover ./tests

# Run virtual test sequences 
test_virtual:
	./venv/bin/python3.8 -m unittest discover ./tests

# Run without the virtual environment 
native:
	python3.8 ./app/app.py

# Run inside the virtual environment 
virtual: venv/bin/activate
	./venv/bin/python3.8 app/app.py

.PHONY: init test_native test_virtual