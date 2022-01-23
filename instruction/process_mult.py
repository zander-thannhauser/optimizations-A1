
from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

from .common import consider;

def process_mult(ops, ins, outs):
	# p.casm("mult", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			process_loadI(ops, [lex * rex], outs);
			
		# identities:
		# 0 * X = 0
		case (0, X):
			assert(not "TODO");
		# 1 * X = X
		case (1, X):
			assert(not "TODO");
		# X * 0 = 0
		case (X, 0):
			assert(not "TODO");
		# X * 1 = X
		case (X, 1):
			assert(not "TODO");
		
		# substitutions:
		# (addI  X, a) * b => addI (multI X, b), (a * b)
		case (("addI", X, a), b) if type(b) is int:
			assert(not "TODO");
		# a * (addI  X, b) => addI (multI X, a), (a * b)
		case (a, ("addI", X, b)) if type(a) is int:
			assert(not "TODO");
		# (multI X, a) * b => multI X, (a * b)
		case (("multI", X, a), b) if type(b) is int:
			assert(not "TODO");
		# a * (multI X, b) => multI X, (a * b)
		case (a, ("multI", X, b)) if type(a) is int:
			assert(not "TODO");
		
		# mult X, c => multI X, c:
		case (X, c) if type(c) is int:
			assert(not "TODO");
		# mult c, X => multI X, c:
		case (c, X) if type(c) is int:
			assert(not "TODO");
		# default:
		case (lex, rex):
			assert(not "TODO");
	
		
#		ex = ("mult", lvn, rvn);
#		vn = extovn(ex);
#		if not vn:
#			vn = mkvn(ex);
#			p.asm("mult", [lvn, rvn], "=>", [vn]);
#		avrwvn(outs[0], vn);










