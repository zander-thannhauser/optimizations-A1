
from lookup import vrtovn, extovn, mkvn, avrwvn, pextovn, apexwvn, vntoex, vrtogvn_lookup;

from .common import consider;

# load vr1 => vr2 | MEMORY(vr1) -> vr2

def process_load(ops, ins, outs):
	# p.casm("load", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
	ovn = pextovn(ivn)
	
	if not ovn:
		# if you don't remember doing the store,
		# then this is brand-new data:
		ovn = mkvn(None);
		match (vntoex(ivn)):
			# load (addI X, c) => Y === loadAI X, c => Y
			case ("addI", X, c):
				ops.append(("loadAI", [X, c], "=>", [ovn]));
			
			# load (add  X, Y) => Z === loadAO X, Y => Z
			case ("add", X, Y):
				assert(not "CHECK");
			
			# load (sub X, ("multI", Y, c)) => Z === loadAO X, (multI, Y -c) => Z
			case ("sub", X, Y):
				# check for using a move instruction's result
				if     (X != "%vr0" and X in vrtogvn_lookup.values()) \
					or (Y != "%vr0" and Y in vrtogvn_lookup.values()):
					assert(not "TODO");
				else:
					subex = vntoex(Y);
					if subex[0] == "multI":
						subvn = consider(ops, ("multI", subex[1], -subex[2]));
						ops.append(("loadAO", [X, subvn], "=>", [ovn]));
					elif subex[0] == "sub":
						assert(not "TODO");
					else:
						assert(not "TODO");
			
			case _:
				ops.append(("load", [ivn], "=>", [ovn]));
				apexwvn(ivn, ovn);
	
	avrwvn(outs[0], ovn);









