
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn, vrtogvn_lookup;

from .process_loadI import load_literal;

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
			load_literal(ops, comp(lex, rex), out);
		
		# identities:
		# comp(X, X) = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# substitutions: (can't do them if either param is move-d)
		# (addI X, a) vs (addI X, b) => a vs b
		case (("addI", X, a), ("addI", Y, b)) if X == Y:
			assert(not "TODO");
		
		# (addI X, a) vs (addI Y, b) => a vs (addI Y, b - a)
		case (("addI", X, a), ("addI", Y, b)):
			if a == b:
				assert(not "TODO");
			else:
				# or whichever's lower
				assert(not "TODO");
			# after you've canceled the adds on both sides,
			# is the inner expression a multiply?
			# if so: try to cancel those factors
		
		# (addI X, a) vs b => X vs (b - a)
		case (("addI", X, a), b) if type(b) is int:
			# check for using a move instruction's result
			if (X != "%vr0" and X in vrtogvn_lookup.values()):
				consider(ops, ("comp", lvn, rvn), out);
			else:
				subvn = load_literal(ops, b - a);
				consider(ops, ("comp", X, subvn), out);
		
		# (multI X, a) vs (multI X, b) => a vs b
		case (("multI", X, a), ("multI", Y, b)) if X == Y:
			assert(not "TODO");
		
		# (multI X, a) vs (multI Y, a) => a vs b
		case (("multI", X, a), ("multI", Y, b)) if a == b:
			assert(not "TODO");
		
		# (multI X, a) vs (multI Y, b) => (multI X, (a // b)) vs Y
		case (("multI", X, a), ("multI", Y, b)):
			# or whichever's lower
			assert(not "TODO");
		
		# (multI X, a) vs b => X vs b // a
		case (("multI", X, a), b) if type(b) is int:
			# make sure you don't break something
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			consider(ops, ("comp", lvn, rvn), out);
















