#!/bin/bash

echo "\nRunning black..."
black src --check

echo "\nRunning flake8..."
flake8 src

echo "\nRunning pylint..."
pylint src --disable=all --enable C0411 # import order, feel free to add new checks
