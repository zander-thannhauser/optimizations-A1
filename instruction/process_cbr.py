
from lookup import vrtovn, vntoex;

from .process_jumpI import process_jumpI;

def process_cbr(ops, ins, outs):
	# p.casm("cbr", ins, "->", outs);
	
	vn = vrtovn(ins[0]);
	
	match (vntoex(vn)):
		# constant-folding:
		case c if type(c) is int:
			if c:
				process_jumpI(ops, [], outs);
		# default:
		case _:
			assert(not "TODO");
	
#	if type(ex) is int:
#	else:
#		p.asm("cbr", [vn], "->", outs);

