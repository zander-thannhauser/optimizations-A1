
from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex, oldgvn;

from .process_loadI import load_literal;

from .common import consider;

def process_mult(ops, ins, outs):
	# p.casm("mult", ins, "=>", outs);
	
	l, r = ins[0], ins[1]
	
	lvn, rvn = vrtovn(l), vrtovn(r)
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			load_literal(ops, lex * rex, out);
			
		# identities:
		# 0 * X = 0
		case (0, _):
			assert(not "TODO");
		# 1 * X = X
		case (1, _):
			assert(not "TODO");
		# X * 0 = 0
		case (_, 0):
			assert(not "TODO");
		# X * 1 = X
		case (_, 1):
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) * b => addI (multI X, b), (a * b)
		case (("addI", X, a), b) if type(b) is int:
			# check for using a move instruction's result
			if oldgvn(X):
				consider(ops, ("multI", lvn, b), out);
			else:
				subvn = consider(ops, ("multI", X, b));
				consider(ops, ("addI", subvn, a * b), out);
		# a * (addI X, b) => addI (multI X, a), (a * b)
		case (a, ("addI", X, b)) if type(a) is int:
			assert(not "TODO");
		# (multI X, a) * b => multI X, (a * b)
		case (("multI", X, a), b) if type(b) is int:
			assert(not "TODO");
		# a * (multI X, b) => multI X, (a * b)
		case (a, ("multI", X, b)) if type(a) is int:
			assert(not "TODO");
		
		# (multI X, a) * (multI Y, b) => multI (mult X Y), (a * b)
		case (("multI", X, a), ("multI", Y, b)):
			assert(not "TODO");
		
		# mult X, c => multI X, c:
		case (_, c) if type(c) is int:
			assert(not "TODO");
		# mult c, X => multI X, c:
		case (c, _) if type(c) is int:
			assert(not "TODO");
		
		# default:
		case (_, _):
			# print(lex, rex);
			consider(ops, ("mult", lvn, rvn), out);
	









