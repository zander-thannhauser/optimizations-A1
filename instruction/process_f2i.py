
from lookup import vrtovn;

from .common import consider;

def process_f2i(ops, ins, outs):
	# p.casm("f2i", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	consider(ops, ("f2i", ivn), outs[0]);
	

