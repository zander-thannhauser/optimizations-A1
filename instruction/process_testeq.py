
from lookup import vrtovn, vntoex, oldgvn;

from .process_loadI import load_literal;

from .common import consider;

def process_testeq(ops, ins, outs):
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			load_literal(ops, 1 if c == 0 else 0, out);
		
		# substitutions:
		case ("comp", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			elif vntoex(X) == 0:
				assert(not "TODO");
			elif vntoex(Y) == 0:
				consider(ops, ("not", X), out);
			else:
				consider(ops, ("cmp_EQ", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");

