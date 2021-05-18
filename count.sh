#!/bin/sh

python3 combos.py | sort | uniq | wc -l
