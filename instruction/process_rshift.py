
from lookup import vrtovn, vntoex, oldgvn;

from .common import consider;

def process_rshift(ops, ins, outs):
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	consider(ops, ("rshift", lvn, rvn), out);

