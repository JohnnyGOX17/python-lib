#!/usr/bin/env bash

GIT_DIR=$(git rev-parse --git-dir)
GIT_TOP=$(git rev-parse --show-toplevel)

echo "Installing pre-commit git hook..."
ln -s ../../scripts/pre-commit "$GIT_DIR/hooks/pre-commit"

echo "Installing dependencies..."
pip3 install -r "$GIT_TOP/requirements.txt"

echo "Done!"

