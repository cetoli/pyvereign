import json

obj = {}
obj["default"] = {}

default = obj["default"]

default["machine"] = {}

machine = default["machine"]

machine["module"] = "atlas.api.env.hardware.DefaultMachine"
machine["classname"] = "DefaultMachine"

s = json.write(obj)

f = open("hardwares_test.yaml", "w")

f.write(s)