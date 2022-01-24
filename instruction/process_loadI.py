
from stdio import printf;

from lookup import extovn, mkvn, avrwvn;

def process_loadI(ops, ins, outs):
	# p.casm("loadI", [str(ins[0])], "=>", outs);
	
	literal = int(ins[0]);
	
	vn = extovn(literal);
	
	if not vn:
		vn = mkvn(literal);
		ops.append(("loadI", [literal], "=>", [vn]));
	
	if outs is not None:
		avrwvn(outs[0], vn);
	return vn;

