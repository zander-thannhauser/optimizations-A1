
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

from .common import consider;

def comp(x, y):
	if x > y:
		return +1;
	elif x < y:
		return -1;
	else:
		return  0;


def process_comp(ops, ins, outs):
	# p.casm("comp", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-fold:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			process_loadI(ops, [comp(lex, rex)], outs);
		
		# identities:
		# comp(X, X) = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# substitutions:
		case (("addI", X, a), ("addI", Y, b)) if X == Y:
			assert(not "TODO");
			
		case (("multI", X, a), ("multI", Y, b)) if X == Y:
			assert(not "TODO");
			
		# default:
		case (lex, rex):
			consider(ops, ("comp", lvn, rvn), out);
















