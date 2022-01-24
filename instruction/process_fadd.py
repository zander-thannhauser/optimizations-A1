
from lookup import vrtovn;

from .common import consider;

def process_fadd(ops, ins, outs):
	# p.casm("fadd", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1]);
	
	consider(ops, ("fadd", lvn, rvn), outs[0]);

