
from lookup import vrtovn;

def process_iret(ops, ins, outs):
	# p.casm("iret", ins);
	
	ivn = vrtovn(ins[0]);
	
	ops.append(("iret", [ivn], "", []));


