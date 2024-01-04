#!/usr/bin/python3
import importlib.util

file_path = 'add_0.py'

spec = importlib.util.spec_from_file_location('add_0', file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
a = 1
b = 2
print("{} + {} = {}".format(a, b, module.add(a, b)))
