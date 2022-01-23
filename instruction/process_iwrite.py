
from lookup import vrtovn;

def process_iwrite(ops, ins, outs):
	p.casm("iwrite", ins);
	
	ivn = vrtovn(ins[0]);
	
	p.asm("iwrite", [ivn]);


