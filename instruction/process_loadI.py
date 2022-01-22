
from stdio import printf;

from lookup import extovn, mkvn, avrwvn;

# might be given an actual int from being called
# from other functions.

def process_loadI(ins, outs, p):
	p.casm("loadI", [str(ins[0])], "=>", outs);
	
	literal = int(ins[0]);
	
	vn = extovn(literal);
	
	if not vn:
		vn = mkvn(literal);
		p.asm("loadI", [str(ins[0])], "=>", [vn]);
	
	avrwvn(outs[0], vn);
	
