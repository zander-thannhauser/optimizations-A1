
from stdio import printf;

from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

# identities:
# X - 0 = X
# X - X = 0

def process_sub(ins, outs, p):
	p.casm("sub", ins, "=>", outs);
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	lex, rex = vntoex(lvn), vntoex(rvn);
	
	if type(lex) is int and type(rex) is int:
		p.comment("constant-fold: %i - %i = %i", lex, rex, lex - rex);
		process_loadI([lex - rex], outs, p);
	elif rex == 0:
		p.comment("identity: X - 0 = X");
		avrwvn(outs[0], lvn);
	elif lex == rex:
		assert(not "TODO");
	else:
		ex = ("sub", lvn, rvn);
		vn = extovn(ex);
		if not vn:
			vn = mkvn(ex);
			p.asm("sub", [lvn, rvn], "=>", [vn]);
		avrwvn(outs[0], vn);
