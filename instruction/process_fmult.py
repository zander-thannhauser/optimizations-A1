
from lookup import vrtovn;

from .common import consider;

def process_fmult(ops, ins, outs):
	# p.casm("fmult", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1]);
	
	consider(ops, ("fmult", lvn, rvn), outs[0]);

