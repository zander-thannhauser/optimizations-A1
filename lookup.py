
from stdio import printf;

register_counter = 0;

extovn_lookup = {};
vntoex_lookup = {};

vrtolvn_lookup = {};

vrtogvn_lookup = {};

pextovn_lookup = {};

def new_frame_numbering(args = []):
	global register_counter;
	register_counter = 0;
	for a in ["%vr0", "%vr1", "%vr2", "%vr3"] + args:
		vrtogvn_lookup[a] = "%%vr%i" % (register_counter);
		register_counter += 1;

def new_block_numbering():
	global extovn_lookup, vntoex_lookup, vrtolvn_lookup;
	extovn_lookup = {};
	vntoex_lookup = {};
	vrtolvn_lookup = {k: v for k, v in vrtogvn_lookup.items()};
	pextovn_lookup = {};

def extovn(ex):
	retval = extovn_lookup.get(ex, None);
	printf("extosr(ex = %s) -> %s\n", ex, retval);
	return retval;

def vntoex(vn):
	retval = vntoex_lookup.get(vn, None);
	printf("vntoex(vn = %s) -> %s\n", vn, retval);
	return retval;

def mkvn(ex):
	global register_counter;
	assert(ex not in extovn_lookup);
	vn = "%%vr%i" % (register_counter);
	register_counter += 1;
	printf("mkvn(ex = %s) -> %s\n", ex, vn);
	if ex is not None:
		extovn_lookup[ex] = vn;
		vntoex_lookup[vn] = ex;
	return vn;

def vrtovn(vr):
	retval = vrtolvn_lookup[vr];
	printf("vrtovn(vr = %s) -> %s\n", vr, retval);
	return retval;

def pextovn(pex):
	retval = pextovn_lookup.get(pex, None);
	printf("pextovn(pex = %s) -> %s\n", pex, retval);
	return retval;

def apexwvn(pex, vn):
	printf("apexwvn(pex = %s, vn = %s);\n", pex, vn);
	pextovn_lookup[pex] = vn;

def vrtogvn(vr):
	global register_counter;
	if vr in vrtogvn_lookup:
		retval = vrtogvn_lookup[vr];
	else:
		retval = "%%vr%i" % register_counter;
		register_counter += 1;
		vrtogvn_lookup[vr] = retval;
		vrtolvn_lookup[vr] = retval;
	printf("vrtosr(vr = %s) -> %s\n", vr, retval);
	return retval;

def avrwvn(vr, vn):
	printf("avrwsr(vr = %s, vn = %s);\n", vr, vn);
	vrtolvn_lookup[vr] = vn;
















