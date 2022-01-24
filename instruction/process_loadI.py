
from stdio import printf;

from lookup import extovn, mkvn, avrwvn;

from .common import consider;

def sint(string):
	try:
		return int(string);
	except:
		return None;

def load_literal(ops, literal, out = None):
	vn = extovn(literal);
	
	if not vn:
		vn = mkvn(literal);
		ops.append(("loadI", [literal], "=>", [vn]));
	
	if out is not None:
		avrwvn(out, vn);
	
	return vn;

def process_loadI(ops, ins, outs):
	# p.casm("loadI", [str(ins[0])], "=>", outs);
	
	out = outs[0];
	
	if literal := sint(ins[0]):
		load_literal(ops, literal, out);
	else:
		consider(ops, ("loadI", ins[0]), out);












