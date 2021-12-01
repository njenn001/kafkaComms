#
#  Custom make-sequence used on Linux machines. 
#  
#  run with 'make .PHONY' 
#

# Initialize project dependencies 
init: requirements.txt  
	@echo 'Fethcing dependencies...'
	@pip install -r requirements.txt -q
	@virtualenv venv -q
	@./venv/bin/pip install -r requirements.txt -q
	@pipreqs ./app/ --force 

# Run native test sequences 
test_native:
	@python3.8 -m unittest discover ./tests

# Run virtual test sequences 
test_virtual:
	@./venv/bin/python3.8 -m unittest discover ./tests

# Run without the virtual environment 
native:
	@python3.8 ./app/app.py

# Run inside the virtual environment 
virtual: venv/bin/activate
	@./venv/bin/python3.8 app/app.py

# Run the cleaning sequence 
clean: 
	@rm -rf __pycache__ app/__pycache__ tests/__pycache__

.PHONY: init test_native test_virtual