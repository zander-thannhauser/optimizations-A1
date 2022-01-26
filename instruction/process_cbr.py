
from lookup import vrtovn, vntoex, oldgvn;

from .process_jumpI import process_jumpI;

def process_cbr(ops, ins, outs):
	# p.casm("cbr", ins, "->", outs);
	
	vn = vrtovn(ins[0]);
	
	match (vntoex(vn)):
		# constant-folding:
		case c if type(c) is int:
			if c: process_jumpI(ops, [], outs);
		
		case ("cmp_LT", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_LT", [X, Y], "->", outs));
		
		case ("cmp_LE", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_LE", [X, Y], "->", outs));
		
		case ("cmp_GT", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_GT", [X, Y], "->", outs));
		
		case ("cmp_GE", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_GE", [X, Y], "->", outs));
		
		case ("cmp_EQ", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_EQ", [X, Y], "->", outs));
		
		case ("cmp_NE", X, Y) if not oldgvn(X) and not oldgvn(Y):
			ops.append(("cbr_NE", [X, Y], "->", outs));
		
		case ("testeq", X, Y): assert(not "TODO");
		case ("testne", X, Y): assert(not "TODO");
		case ("testgt", X, Y): assert(not "TODO");
		case ("testge", X, Y): assert(not "TODO");
		case ("testlt", X, Y): assert(not "TODO");
		case ("testle", X, Y): assert(not "TODO");
		
		case ("not", X) if not oldgvn(X):
			ops.append(("cbrne", [X], "->", outs));
		
		# default:
		case _:
			ops.append(("cbr", [vn], "->", outs));
	













