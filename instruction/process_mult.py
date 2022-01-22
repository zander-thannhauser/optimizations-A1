
from lookup import vrtovn, extovn, mkvn, avrwvn, vntoex;

from .process_loadI import process_loadI;

# identities:
# 0 * X = 0
# 1 * X = X
# X * 0 = 0
# X * 1 = X

def process_mult(ins, outs, p):
	p.casm("mult", ins, "=>", outs);
	lvn, rvn = vrtovn(ins[0]), vrtovn(ins[1])
	lex, rex = vntoex(lvn), vntoex(rvn);
	
	if type(lex) is int and type(rex) is int:
		p.comment("constant-fold: %i * %i = %i", lex, rex, lex * rex);
		process_loadI([lex * rex], outs, p);
	elif lex == 0:
		assert(not "TODO");
	elif lex == 1:
		assert(not "TODO");
	elif rex == 0:
		assert(not "TODO");
	elif rex == 1:
		assert(not "TODO");
	else:
		assert(not "TODO");
#	ex = ("mult", lvn, rvn);
#	vn = extovn(ex);
#	if not vn:
#		vn = mkvn(ex);
#		p.asm("mult", [lvn, rvn], "=>", [vn]);
#	avrwvn(outs[0], vn);

