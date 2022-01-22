
from lookup import vrtovn;

# store vr1 -> vr2 | MEMORY(vr2) <- vr1

def process_store(ins, outs, p):
	p.casm("store", ins, "=>", outs);
	ivn = vrtovn(ins[0]);
	ovn = vrtovn(outs[0]);
	p.asm("store", [ivn], "=>", [ovn]);
