
from lookup import vrtovn, vntoex, vrtogvn_lookup;

from .process_jumpI import process_jumpI;

def process_cbr(ops, ins, outs):
	# p.casm("cbr", ins, "->", outs);
	
	vn = vrtovn(ins[0]);
	
	match (vntoex(vn)):
		# constant-folding:
		case c if type(c) is int:
			if c: process_jumpI(ops, [], outs);
		
		case ("cmp_LT", X, Y):
			assert(not "TODO");
		
		case ("cmp_LE", X, Y):
			# check for using a move instruction's result
			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
				assert(not "TODO");
			else:
				ops.append(("cbr_LE", [X, Y], "->", outs));
		
		case ("cmp_GT", X, Y):
			# check for using a move instruction's result
			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
				assert(not "TODO");
			else:
				ops.append(("cbr_GT", [X, Y], "->", outs));
		
		case ("cmp_GE", X, Y):
			assert(not "TODO");
		
		case ("cmp_EQ", X, Y):
			assert(not "TODO");
		
		case ("cmp_NE", X, Y):
			assert(not "TODO");
		
		case ("testeq", X, Y): assert(not "TODO");
		case ("testne", X, Y): assert(not "TODO");
		case ("testgt", X, Y): assert(not "TODO");
		case ("testge", X, Y): assert(not "TODO");
		case ("testlt", X, Y): assert(not "TODO");
		case ("testle", X, Y): assert(not "TODO");
		
		# default:
		case _:
			assert(not "TODO");
			# p.asm("cbr", [vn], "->", outs);
	






