
from lookup import vrtovn;

def process_putchar(ops, ins, outs):
	# p.casm("putchar", ins);
	
	ivn = vrtovn(ins[0]);
	
	ops.append(("putchar", [ivn], "", []));


