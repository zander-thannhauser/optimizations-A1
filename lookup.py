
from stdio import printf;

register_counter = 0;

extovn_lookup = {};
vntoex_lookup = {};

vrtovn_lookup = {};

def new_frame_numbering():
	global register_counter;
	vrtovn_lookup["%vr0"] = "%vr0";
	vrtovn_lookup["%vr1"] = "%vr1";
	vrtovn_lookup["%vr2"] = "%vr2";
	vrtovn_lookup["%vr3"] = "%vr3";
	register_counter = 4;

def new_block_numbering():
	pass;

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

# might crash, but that's good
def vrtovn(vr):
	retval = vrtovn_lookup[vr];
	printf("vrtovn(vr = %s) -> %s\n", vr, retval);
	return retval;

def avrwvn(vr, vn):
	printf("avrwsr(vr = %s, vn = %s);\n", vr, vn);
	vrtovn_lookup[vr] = vn;
















