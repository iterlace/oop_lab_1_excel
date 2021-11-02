#!/bin/bash

echo "\nRunning black..."
black plink_srv --check

echo "\nRunning flake8..."
flake8 plink_srv

echo "\nRunning pylint..."
pylint plink_srv --disable=all --enable C0411 # import order, feel free to add new checks
