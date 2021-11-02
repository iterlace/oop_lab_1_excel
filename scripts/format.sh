#!/bin/bash

echo "Running autoflake..."
autoflake --remove-all-unused-imports --recursive --in-place src --exclude=__init__.py
echo "\n"

echo "Running black"
black src
echo "\n"

echo "Running isort"
isort src
