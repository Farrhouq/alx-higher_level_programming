#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

st = Student("Fake", "Fake", 89)
print(st.first_name, st.last_name, st.age)
st.reload_from_json({"first_name": "New", "last_name": "Newlast", "age": 44})
print(st.first_name, st.last_name, st.age)