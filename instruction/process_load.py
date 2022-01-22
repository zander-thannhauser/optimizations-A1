
from lookup import vrtovn, extovn, mkvn, avrwvn;

# load vr1 => vr2 | MEMORY(vr1) -> vr2

def process_load(ins, outs, p):
	p.casm("load", ins, "=>", outs);
	
	ivn = vrtovn(ins [0]);
	
	ovn = mkvn(None);
	avrwvn(outs[0], ovn);
	
	p.asm("load", [ivn], "=>", [ovn]);
	

