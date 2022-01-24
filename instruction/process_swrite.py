
from lookup import vrtovn;

def process_swrite(ops, ins, outs):
	# p.casm("swrite", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	ops.append(("iwrite", [ivn], "", []));
	
