
from lookup import vrtovn, vntoex;

from .common import consider;

def process_or(ops, ins, outs):
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	
	out = outs[0];
	
	match (vntoex(lvn), vntoex(rvn)):
		# constant-folding:
		case (lex, rex) if type(lex) is int and type(rex) is int:
			load_literal(ops, lex or rex, out)
		
		case (1, _):
			assert(not "TODO");
		
		case (_, 1):
			assert(not "TODO");
		
		case (0, _):
			assert(not "TODO");
		
		case (_, 0):
			assert(not "TODO");
		
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		case (_, _):
			consider(ops, ("or", lvn, rvn), out);
