
from lookup import vrtovn, vntoex, apexwvn;

from .common import consider;

# store vr1 -> vr2 | MEMORY(vr2) <- vr1

def process_store(ops, ins, outs):
	# p.casm("store", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	ovn = vrtovn(outs[0]);
	
	match (vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case ("addI", X, c):
			ops.append(("storeAI", [ivn], "=>", [X, c]));
		
		# store X, (Y - c) => storeAI X -> Y, -c
		case ("subI", X, c):
			assert(not "TODO");
		
		# store X, (Y + Z) => storeAO X -> Y, Z
		case ("add", X, Y):
			assert(not "TODO");
		
		# store (sub X, ("multI", Y, c)) => Z === storeAO X, (multI, Y -c) => Z
		case ("sub", X, Y):
			subex = vntoex(Y);
			if subex[0] == "multI":
				subvn = consider(ops, ("multI", subex[1], -subex[2]));
				ops.append(("storeAO", [ivn], "=>", [X, subvn]));
			else:
				assert(not "TODO");
		
		# default:
		case _:
			ops.append(("store", [ivn], "=>", [ovn]));
	
	apexwvn(ovn, ivn);








