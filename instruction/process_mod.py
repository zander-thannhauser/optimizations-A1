
from lookup import vrtovn, vntoex;

from .common import consider;

def process_mod(ops, ins, outs):
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			if rex != 0:
				# load_literal([lex + rex], outs, p)
				assert(not "TODO");
			else:
				consider(ops, ("mod", lvn, rvn), out);
		
		# identities:
		# 0 + X = X
		case (0, _):
			assert(not "TODO");
		
		case (_, _):
			consider(ops, ("mod", lvn, rvn), out);
	
