
from lookup import vrtovn, vntoex;

from .process_jumpI import process_jumpI;

def process_cbr(ins, outs, p):
	p.casm("cbr", ins, "->", outs);
	
	vn = vrtovn(ins[0]);
	ex = vntoex(vn);
	
	if type(ex) is int:
		if ex:
			process_jumpI([], outs, p);
		else:
			pass
	else:
		assert(not "TODO");

