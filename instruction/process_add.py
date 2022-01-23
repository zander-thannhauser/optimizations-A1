
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
			# process_loadI([lex + rex], outs, p)
			assert(not "TODO");
		
		# identities:
		# 0 + X = X
		case (0, X):
			assert(not "TODO");
		# X + 0 = X
		case (X, 0):
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) + b => addI X, (a + b)
		case (("addI", vrX, a), b) if type(b) is int:
			assert(not "TODO");
		# a + (addI X, b) => addI X, (a + b)
		case (a, ("addI", X, b)) if type(a) is int:
			assert(not "TODO");
		# (sub X, Y) + Y => X
		case (("sub", X, Y), Z) if Y == Z:
			assert(not "TODO");
		# X + (sub Y, X) => Y
		case (X, ("sub", Y, Z)) if Z == Z:
			assert(not "TODO");
		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
		case (("addI", X, a), ("addI", Y, b)):
			if a + b == 0:
				assert(not "TODO");
			else:
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
	
#		ex = ("add", lvn, rvn);
#		vn = extovn(ex);
#		if not vn:
#			vn = mkvn(ex);
#				ops.append(("add", [lvn, rvn], "=>", [vn]));
#		avrwvn(outs[0], vn);















