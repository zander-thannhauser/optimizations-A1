
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

def comp(x, y):
	if x > y:
		return +1;
	elif x < y:
		return -1;
	else:
		return  0;

# identities:
# comp(X, X) = 0

def process_comp(ins, outs, p):
	p.casm("comp", ins, "=>", outs);
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	lex, rex = vntoex(lvn), vntoex(rvn);
	
	if type(lex) is int and type(rex) is int:
		process_loadI([comp(lex, rex)], outs, p);
	elif lvn == rvn:
		assert(not "TODO");
	else:
		ex = ("comp", lvn, rvn);
		vn = extovn(ex);
		if not vn:
			vn = mkvn(ex);
			p.asm("comp", [lvn, rvn], "=>", [vn]);
		avrwvn(outs[0], vn);

















