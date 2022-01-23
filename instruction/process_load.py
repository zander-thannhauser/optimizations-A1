
from lookup import vrtovn, extovn, mkvn, avrwvn;

# load vr1 => vr2 | MEMORY(vr1) -> vr2

def process_load(ops, ins, outs):
	p.casm("load", ins, "=>", outs);
	
	assert(not "CHECK");
	
	ivn = vrtovn(ins [0]);
	
	ovn = pextovn(ivn)
	
	if not ovn:
		# if you don't remember doing the store,
		# then this is brand-new data:
		ovn = mkvn(None);
		ops.append(("load", [ivn], "=>", [ovn]));
		
	apexwvn(outs[0], ovn);
	
