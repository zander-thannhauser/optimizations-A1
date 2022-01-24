
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

from .common import consider;

def process_testgt(ops, ins, outs):
	# p.casm("testgt", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	out = outs[0];
	
	match (vntoex(ivn)):
		# constant-fold:
		case c if type(c) is int:
			process_loadI(ops, [1 if c > 0 else 0], outs);
		
		# substitutions:
		case ("comp", X, Y):
			consider(ops, ("cmp_GT", X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
#	
#		ex = ("testgt", ivn);
#		ovn = extovn(ex);
#		if not ovn:
#			ovn = mkvn(ex);
#			p.asm("testgt", [ivn], "=>", [ovn]);
#		avrwvn(outs[0], ovn);
	

