#!/usr/bin/python3

from stdio import fprintf, stderr;

from defines.argv0 import argv0;

from tokenizer import tokenizer;
from printer import printer;

from data import process_data;
from text import process_text;

filename = "examples/bubble.il"

t = tokenizer(filename);
p = printer(filename[:-3] + ".oil");

next(t);

process_data(t, p);

process_text(t, p);

if t.token != "":
	fprintf(stderr, "%s: unknown token: \"%s\"!\n", argv0, t.token);
	exit(1);

print("exit(0)");

