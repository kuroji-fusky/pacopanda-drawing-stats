install:
  yarn
  cd python
  source venv/Scripts/activate
  cd ../..
  pip install -r requirements.txt

clean-python:
  rm -f */__pycache__*

clean-node:
  rm -f */node_modules* yarn.lock