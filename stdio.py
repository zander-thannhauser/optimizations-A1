
import sys;

stderr = sys.stderr;

def printf(fmt, *args):
	print(fmt % args, end = '');

def fprintf(stream, fmt, *args):
	print(fmt % args, file = stream, end = '');

