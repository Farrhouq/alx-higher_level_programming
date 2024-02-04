#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("Invalid List Object\n");
		return;
	}

	Py_ssize_t len = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("  Size of the Python list: %zd\n", len);
	printf("  Allocated: %zd\n", ((PyListObject *)p)->allocated);

	// Access elements using PyList_GetItem and PyLong_AsLong
	// while ensuring proper error handling
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	const char *bytes = PyBytes_AsString(p);

	printf("[*] Python bytes info\n");
	printf("  Size of the Python bytes: %zd\n", size);
	printf("  First %zd bytes: %.*s\n", (size > 10) ? 10 : size, (int)size, bytes);
}

void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		printf("Invalid Float Object\n");
		return;
	}

	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[*] Python float info\n");
	printf("  Value: %f\n", float_obj->ob_fval);
}
