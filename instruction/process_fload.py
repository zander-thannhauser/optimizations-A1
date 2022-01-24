
from lookup import vrtovn, pextovn, mkvn, vntoex, apexwvn, avrwvn;

def process_fload(ops, ins, outs):
	# p.casm("fload", ins, "=>", outs);
	
	ivn = vrtovn(ins[0]);
	
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
				# check for using a move instruction's result
				assert(not "TODO");
				assert(not "TODO");
				subex = vntoex(Y);
				if subex[0] == "multI":
					subvn = consider(ops, ("multI", subex[1], -subex[2]));
					ops.append(("floadAO", [X, subvn], "=>", [ovn]));
				elif subex[0] == "sub":
					assert(not "TODO");
				else:
					assert(not "TODO");
			
			case _:
				ops.append(("fload", [ivn], "=>", [ovn]));
				apexwvn(ivn, ovn);
	
	avrwvn(outs[0], ovn);

