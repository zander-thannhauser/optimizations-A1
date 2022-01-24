
from stdio import printf;

from lookup import vrtovn, avrwvn, vrtogvn, vntoex;

def process_i2i(ops, ins, outs):
	# p.casm("i2i", ins, "=>", outs);
	
	gvn = vrtogvn(outs[0]);
	
	ivn = vrtovn(ins[0]);
	ovn = vrtovn(outs[0]);
	
	if ivn == ovn:
		pass;
	else:
		if not (ex := vntoex(ivn)):
			ops.append(("i2i", [ivn], "=>", [gvn]));
		elif type(ex) is int:
			ops.append(("loadI", [ex], "=>", [gvn]));
		else:
			ops.append((ex[0], list(ex[1:]), "=>", [gvn]));
		avrwvn(outs[0], ivn);




