
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

from .common import consider;

def process_testlt(ops, ins, outs):
	# p.casm("testlt", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			process_loadI(ops, [1 if c < 0 else 0], outs);
		
		# substitutions:
		case ("comp", X, Y):
			consider(ops, ("cmp_LT", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
#	
#		ex = ("testlt", ivn);
#		ovn = extovn(ex);
#		if not ovn:
#			ovn = mkvn(ex);
#			p.asm("testlt", [ivn], "=>", [ovn]);
#		avrwvn(outs[0], ovn);
	
