
from lookup import vrtovn, mkvn, avrwvn;

def process_icall(ops, ins, outs):
	# p.casm("call", ins);
	
	out = outs[0];
	
	new = mkvn(None);
	
	ops.append(("icall", [ins[0]] + [vrtovn(i) for i in ins[1:]], "=>", [new]));
	
	avrwvn(out, new);
	
