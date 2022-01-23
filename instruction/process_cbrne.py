
from lookup import vntoex, vrtovn

def process_cbrne(ops, ins, outs):
	p.casm("cbrne", ins, "->", outs);
	
	assert(not "TODO");
	
#	ivn = vrtovn(ins[0])
#	iex = vntoex(ivn)
#	
#	if type(ivn) is int:
#		assert(not "TODO");
#	else:
#		p.asm("cbrne", [ivn], "->", outs);

