
from lookup import vrtovn, vntoex, extovn, mkvn, avrwvn;

from .process_loadI import process_loadI;

def process_testlt(ins, outs, p):
	p.casm("testlt", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	ex = vntoex(ivn);
	
	if type(ex) is int:
		process_loadI([1 if ex < 0 else 0], outs, p);
	else:
		ex = ("testlt", ivn);
		ovn = extovn(ex);
		if not ovn:
			ovn = mkvn(ex);
			p.asm("testlt", [ivn], "=>", [ovn]);
		avrwvn(outs[0], ovn);


