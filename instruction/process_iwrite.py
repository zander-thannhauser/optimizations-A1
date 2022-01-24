
from lookup import vrtovn;

def process_iwrite(ops, ins, outs):
	# p.casm("iwrite", ins);
	
	ivn = vrtovn(ins[0]);
	
	ops.append(("iwrite", [ivn]));


