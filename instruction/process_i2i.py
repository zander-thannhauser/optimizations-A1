
from stdio import printf;

from lookup import vrtovn, avrwvn;

def process_i2i(ins, outs, p):
	p.casm("i2i", ins, "=>", outs);
	vn = vrtovn(ins[0]);
	printf("vn == \"%s\"\n", vn);
	avrwvn(outs[0], vn);
