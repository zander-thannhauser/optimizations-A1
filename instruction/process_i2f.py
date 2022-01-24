
from lookup import vrtovn;

from .common import consider;

def process_i2f(ops, ins, outs):
	# p.casm("i2f", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	consider(ops, ("i2f", ivn), outs[0]);
	
