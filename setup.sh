set -e

pip3 install --upgrade poetry
poetry config virtualenvs.create false --local
poetry install --no-root
