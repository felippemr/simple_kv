pip:
	@pip install -r requirements.txt

pip_test:
	@pip install -r requirements_test.txt

clean:
	@find *.pyc | xargs rm -f && find __pycache__ | xargs rm -rf

run:
	@python server.py

stop:
	@kill $$(cat /tmp/gunicorn.pid)

test:
	@python -m pytest -v
