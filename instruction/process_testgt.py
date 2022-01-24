
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn, vrtogvn_lookup;

from .process_loadI import load_literal;

from .common import consider;

def process_testgt(ops, ins, outs):
	# p.casm("testgt", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			load_literal(ops, 1 if c > 0 else 0, out);
		
		# substitutions:
		case ("comp", X, Y):
			# check for using a move instruction's result
			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
				assert(not "TODO");
			else:
				consider(ops, ("cmp_GT", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");

