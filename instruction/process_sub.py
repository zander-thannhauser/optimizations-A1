
from stdio import printf;

from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

from .common import consider;

def process_sub(ops, ins, outs):
	# p.casm("sub", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			process_loadI(ops, [lex - rex], outs);
		
		# identities:
		# X - 0 = X
		case (X, 0):
			avrwvn(out, lvn);
		# X - X = 0
		case (X, Y) if X == Y:
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) - b => addI X, (a - b)
		case (("addI", X, a), b) if type(b) is int:
			if (b == a):
				assert(not "TODO");
			else:
				consider(ops, ("addI", X, a - b), out);
		
		# (add X, Y) - Y => X
		case (("add", X, Y), Z) if Y == Z:
			assert(not "TODO");
		
		# (addI X, a) - (addI Y, b) => addI (add X, Y), (- a - b)
		case (("addI", X, a), ("addI", Y, b)):
			assert(not "TODO");
		
		# X - c => addI X, -c
		case (X, c) if type(c) is int:
			assert(not "TODO");
		
		# default:
		case (_, _):
			assert(not "TODO");
	
#		ex = ("sub", lvn, rvn);
#		vn = extovn(ex);
#		if not vn:
#			vn = mkvn(ex);
#			p.asm("sub", [lvn, rvn], "=>", [vn]);
#		avrwvn(out, vn);














