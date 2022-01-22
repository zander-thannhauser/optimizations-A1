
from lookup import vrtovn;

def process_iwrite(ins, outs, p):
	p.casm("iwrite", ins);
	
	ivn = vrtovn(ins[0]);
	
	p.asm("iwrite", [ivn]);


