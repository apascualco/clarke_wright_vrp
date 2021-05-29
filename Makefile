init:
	$(info Installing requirements)
	pip install -r requirements.txt

test:
	$(info Launching tests)
	pytest tests

.PHONY: init test
