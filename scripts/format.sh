#!/bin/bash

echo "Running autoflake..."
autoflake --remove-all-unused-imports --recursive --in-place srv --exclude=__init__.py
echo "\n"

echo "Running black"
black srv
echo "\n"

echo "Running isort"
isort srv
