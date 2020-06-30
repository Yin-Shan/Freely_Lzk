#!/bin/bash
project_path=$(dirname `readlink -f "$0"`)
cd "$project_path"
python3 ./main.py
