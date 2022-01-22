
from lookup import vrtovn, vntoex;

from .process_loadI import process_loadI;

def process_testgt(ins, outs, p):
	p.casm("testgt", ins, "=>", outs);
	
	vn = vrtovn(ins[0]);
	ex = vntoex(vn);
	
	if type(ex) is int:
		process_loadI([1 if ex > 0 else 0], outs, p);
	else:
		assert(not "TODO");
	

