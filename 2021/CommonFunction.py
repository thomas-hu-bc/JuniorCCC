"""
Created by Thomas Hu on 2025-08-23 at 6:08 p.m.
"""
import logging
from pathlib import Path

def read_file(file_name):
    lines=[]
    with open(file_name, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines
