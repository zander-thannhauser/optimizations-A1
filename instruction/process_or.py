
from lookup import vrtovn, vntoex, oldgvn;

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
		
		case (lex, rex):
			if type(lex) is tuple and lex[0] in ["cmp_NE", "testne"]:
				if vntoex(lex[1]) == 0 and not oldgvn(lex[2]):
					assert(not "TODO");
				elif vntoex(lex[2]) == 0 and not oldgvn(lex[1]):
					lvn = lex[1];
			if type(rex) is tuple and rex[0] in ["cmp_NE", "testne"]:
				if vntoex(rex[1]) == 0 and not oldgvn(rex[2]):
					assert(not "TODO");
				elif vntoex(rex[2]) == 0 and not oldgvn(rex[1]):
					rvn = rex[1];
			consider(ops, ("or", lvn, rvn), out);












