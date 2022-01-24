
from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

from .common import consider;

def process_add(ops, ins, outs):
	# p.casm("add", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			# load_literal([lex + rex], outs, p)
			assert(not "TODO");
		
		# identities:
		# 0 + X = X
		case (0, _):
			assert(not "TODO");
		# X + 0 = X
		case (_, 0):
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) + b => addI X, (a + b)
		case (("addI", X, a), b) if type(b) is int:
			# check for using a move instruction's result
			assert(not "TODO");
		# a + (addI X, b) => addI X, (a + b)
		case (a, ("addI", X, b)) if type(a) is int:
			# check for using a move instruction's result
			assert(not "TODO");
		# (sub X, Y) + Y => X
		case (("sub", X, Y), Z) if Y == Z:
			# check for using a move instruction's result
			assert(not "TODO");
		# X + (sub Y, X) => Y
		case (X, ("sub", Y, Z)) if Z == Z:
			# check for using a move instruction's result
			assert(not "TODO");
		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
		case (("addI", X, a), ("addI", Y, b)):
			# check for using a move instruction's result
			if a + b == 0:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# (multI X, a) + (multI Y, a) = multI (add X, Y), a
		case (("multI", X, a), ("multI", Y, b)) if a == b:
			# check for using a move instruction's result
			assert(not "TODO");
		
		# X + c => addI X, c
		case (lex, rex) if type(rex) is int:
			consider(ops, ("addI", lvn, rex), out);
		
		# c + X => addI X, c
		case (lex, rex) if type(lex) is int:
			consider(ops, ("addI", rvn, lex), out);
		
		# default:
		case (_, _):
			assert(not "TODO");
	















