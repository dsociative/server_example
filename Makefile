env:
	virtualenv env
	env/bin/pip install -r requirements.txt

clean:
	rm -rf env
