
from lookup import extovn, mkvn, avrwvn;

def consider(ops, ex, out = None):
	vn = extovn(ex);
	if not vn:
		vn = mkvn(ex);
		ops.append((ex[0], list(ex[1:]), "=>", [vn]));
	if out is not None:
		avrwvn(out, vn);
	return vn;


