
from lookup import vrtovn, mkvn, pextovn, apexwvn;

def process_iread(ops, ins, outs):
	# p.casm("iread", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	if pextovn(ivn):
		new = mkvn(None);
		apexwvn(ivn, new);
	
	ops.append(("iread", [ivn], "", []));

