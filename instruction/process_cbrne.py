
from lookup import vntoex, vrtovn

def process_cbrne(ins, outs, p):
	p.casm("cbrne", ins, "->", outs);
	
	ivn = vrtovn(ins[0])
	iex = vntoex(ivn)
	
	if type(ivn) is int:
		assert(not "TODO");
	else:
		p.asm("cbrne", [ivn], "->", outs);

