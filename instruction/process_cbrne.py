
from lookup import vntoex, vrtovn, vrtogvn_lookup;

def process_cbrne(ops, ins, outs):
	# p.casm("cbrne", ins, "->", outs);
	
	ivn = vrtovn(ins[0])
	
	out = outs[0];
	
	match (vntoex(ivn)):
		
		case ("cmp_LT", X, Y):
			# check for using a move instruction's result
			if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
				or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
				assert(not "TODO");
			else:
				ops.append(("cbr_GE", [X, Y], "->", [out]));
		
		case ("cmp_LE", X, Y): assert(not "TODO");
		case ("cmp_GT", X, Y): assert(not "TODO");
		case ("cmp_GE", X, Y): assert(not "TODO");
		case ("cmp_EQ", X, Y): assert(not "TODO");
		case ("cmp_NE", X, Y): assert(not "TODO");
		
		case ("testeq", X): assert(not "TODO");
		case ("testne", X): assert(not "TODO");
		case ("testgt", X): assert(not "TODO");
		case ("testge", X): assert(not "TODO");
		case ("testlt", X): assert(not "TODO");
		case ("testle", X): assert(not "TODO");
		
		case _:
			assert(not "TODO");
	
