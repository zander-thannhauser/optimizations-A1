
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

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
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-fold:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			process_loadI(ops, [comp(lex, rex)], outs);
		
		# identities:
		# comp(X, X) = 0
		case (X, Y) if X == Y:
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			assert(not "TODO");
	
#		ex = ("comp", lvn, rvn);
#		vn = extovn(ex);
#		if not vn:
#			vn = mkvn(ex);
#			p.asm("comp", [lvn, rvn], "=>", [vn]);
#		avrwvn(outs[0], vn);

















