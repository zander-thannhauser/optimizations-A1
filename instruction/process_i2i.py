
from stdio import printf;

from lookup import vrtovn, avrwvn, vrtogvn;

def process_i2i(ins, outs, p):
	p.casm("i2i", ins, "=>", outs);
	
	gvn = vrtogvn(outs[0]);
	
	ivn = vrtovn(ins[0]);
	ovn = vrtovn(outs[0]);
	
	if ivn != ovn:
		p.asm("i2i", [ivn], "=>", [gvn]);
		avrwvn(outs[0], ivn);




