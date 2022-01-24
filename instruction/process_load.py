
from lookup import vrtovn, extovn, mkvn, avrwvn, pextovn, apexwvn, vntoex;

from .common import consider;

# load vr1 => vr2 | MEMORY(vr1) -> vr2

def process_load(ops, ins, outs):
	# p.casm("load", ins, "=>", outs);
	
	ivn = vrtovn(ins [0]);
	
	ovn = pextovn(ivn)
	
	if not ovn:
		# if you don't remember doing the store,
		# then this is brand-new data:
		ovn = mkvn(None);
		match (vntoex(ivn)):
			# load (addI X, c) => Y === loadAI X, c => Y
			case ("addI", X, c):
				assert(not "CHECK");
			
			# load (add  X, Y) => Z === loadAO X, Y => Z
			case ("add", X, Y):
				assert(not "CHECK");
			
			# load (sub X, ("multI", Y, c)) => Z === loadAO X, (multI, Y -c) => Z
			case ("sub", X, Y):
				subex = vntoex(Y);
				if subex[0] == "multI":
					subvn = consider(ops, ("multI", subex[1], -subex[2]));
					ops.append(("loadAO", [X, subvn], "=>", [ovn]));
				else:
					assert(not "TODO");
			
			case _:
				ops.append(("load", [ivn], "=>", [ovn]));
				apexwvn(ivn, ovn);
	
	avrwvn(outs[0], ovn);









