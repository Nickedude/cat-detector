create-venv:
	python3 -m venv  ./venv
	. ./venv/bin/activate
	pip install -r requirements.txt

get-data:
	kaggle datasets download -d devdgohil/the-oxfordiiit-pet-dataset
	unzip the-oxfordiiit-pet-dataset.zip

