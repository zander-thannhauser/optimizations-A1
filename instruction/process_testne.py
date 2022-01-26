
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn, oldgvn;

from .process_loadI import process_loadI;

from .common import consider;

def process_testne(ops, ins, outs):
	# p.casm("testne", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			load_literal(ops, 1 if c != 0 else 0, out);
		
		# substitutions:
		case ("comp", X, Y):
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			elif vntoex(X) == 0:
				assert(not "TODO");
			elif vntoex(Y) == 0:
				avrwvn(out, X);
			else:
				consider(ops, ("cmp_NE", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
