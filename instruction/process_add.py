
from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

# identities:
# c + c = c
# 0 + X = X
# X + 0 = X

def process_add(ins, outs, p):
	p.casm("add", ins, "=>", outs);
	
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	lex, rex = vntoex(lvn), vntoex(rvn);
	
	if type(lex) is int and type(rex) is int:
		process_loadI([lex + rex], outs, p)
	elif lex == 0:
		assert(not "TODO");
	elif rex == 0:
		assert(not "TODO");
	else:
		ex = ("add", lvn, rvn);
		vn = extovn(ex);
		if not vn:
			vn = mkvn(ex);
			p.asm("add", [lvn, rvn], "=>", [vn]);
		avrwvn(outs[0], vn);

