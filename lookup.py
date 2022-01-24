
from stdio import printf;

register_counter = 0;

extovn_lookup = {};
vntoex_lookup = {};

vrtolvn_lookup = {};

vrtogvn_lookup = {};

gvn_vers = {};

pextovn_lookup = {};

def new_frame_numbering(args = []):
	global register_counter;
	register_counter = 0;
	vrtogvn_lookup.clear();
	for a in ["%vr0", "%vr1", "%vr2", "%vr3"] + args:
		vrtogvn_lookup[a] = "%%vr%i" % (register_counter);
		register_counter += 1;

def new_block_numbering():
	extovn_lookup.clear();
	vntoex_lookup.clear();
	pextovn_lookup.clear();
	vrtolvn_lookup.clear()
	gvn_vers.clear();
	for k, v in vrtogvn_lookup.items():
		gvn_vers[v] = 0;
		vrtolvn_lookup[k] = v;

def after_call():
	new_block_numbering();

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
	# print("vrtolvn_lookup:", vrtolvn_lookup);
	retval = vrtolvn_lookup[vr];
	if retval in gvn_vers:
		retval += ":%i" % gvn_vers[retval];
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
		gvn_vers[retval] = 0;
		vrtogvn_lookup[vr] = retval;
		vrtolvn_lookup[vr] = retval;
	printf("vrtogvn(vr = %s) -> %s\n", vr, retval);
	# print("vrtogvn_lookup:", vrtogvn_lookup);
	return retval;

def incgvn(gvn):
	assert(gvn in gvn_vers);
	retval = gvn_vers[gvn] + 1;
	printf("incgvn(gvn = %s) -> %i\n", gvn, retval);
	gvn_vers[gvn] = retval;
	print("gvn_vers:", gvn_vers);

def oldgvn(gvn):
	if ":" in gvn:
		xs = gvn.split(":");
		if gvn_vers[xs[0]] != int(xs[1]):
			return True;
	return False;

def avrwvn(vr, vn):
	printf("avrwsr(vr = %s, vn = %s);\n", vr, vn);
	vrtolvn_lookup[vr] = vn;




























