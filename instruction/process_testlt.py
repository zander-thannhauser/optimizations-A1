
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn, vrtogvn_lookup;

from .process_loadI import process_loadI;

from .common import consider;

def process_testlt(ops, ins, outs):
	# p.casm("testlt", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			load_literal(ops, 1 if c < 0 else 0, out);
		
		# substitutions:
		case ("comp", X, Y):
			# check for using a move instruction's result
			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
				assert(not "TODO");
			else:
				consider(ops, ("cmp_LT", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
