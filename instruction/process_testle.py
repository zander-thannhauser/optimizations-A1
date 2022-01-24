
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn, oldgvn;

from .process_loadI import process_loadI;

from .common import consider;

def process_testle(ops, ins, outs):
	# p.casm("testle", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			load_literal(ops, 1 if c <= 0 else 0, out);
		
		# substitutions:
		case ("comp", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			else:
				consider(ops, ("cmp_LE", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
