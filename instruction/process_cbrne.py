
from lookup import vntoex, vrtovn, oldgvn;

def process_cbrne(ops, ins, outs):
	# p.casm("cbrne", ins, "->", outs);
	
	ivn = vrtovn(ins[0])
	
	out = outs[0];
	
	match (vntoex(ivn)):
		
		# constant-folding:
		case c if type(c) is int:
			if not c: process_jumpI(ops, [], outs);
		
		case ("cmp_LT", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			else:
				ops.append(("cbr_GE", [X, Y], "->", [out]));
		
		case ("cmp_LE", X, Y): assert(not "TODO");
		case ("cmp_GT", X, Y): assert(not "TODO");
		case ("cmp_GE", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			else:
				ops.append(("cbr_LT", [X, Y], "->", [out]));
		
		case ("cmp_EQ", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			else:
				ops.append(("cbr_NE", [X, Y], "->", [out]));
		
		case ("cmp_NE", X, Y):
			# check for using a move instruction's result
			if oldgvn(X) or oldgvn(Y):
				assert(not "TODO");
			else:
				ops.append(("cbr_EQ", [X, Y], "->", [out]));
		
		case ("testeq", X): assert(not "TODO");
		case ("testne", X): assert(not "TODO");
		case ("testgt", X): assert(not "TODO");
		case ("testge", X): assert(not "TODO");
		case ("testlt", X): assert(not "TODO");
		case ("testle", X): assert(not "TODO");
		
		case ("and", X, Y):
			assert(not "TODO");
		
		case ("or", X, Y):
			assert(not "TODO");
		
		case ("not", X) if not oldgvn(X):
			ops.append(("cbr", [X], "->", [out]));
		
		case exp:
			print(f"exp = {exp}")
			assert(not "TODO");
	











