
from lookup import vrtovn, vntoex;

from .process_jumpI import process_jumpI;

def process_cbr(ops, ins, outs):
	# p.casm("cbr", ins, "->", outs);
	
	vn = vrtovn(ins[0]);
	
	match (vntoex(vn)):
		# constant-folding:
		case c if type(c) is int:
			if c:
				process_jumpI(ops, [], outs);
		
		case ("cmp_LT", X, Y):
			assert(not "TODO");
		
		case ("cmp_LE", X, Y):
			ops.append(("cbr_LE", [X, Y], "->", outs));
		
		case ("cmp_GT", X, Y):
			ops.append(("cbr_GT", [X, Y], "->", outs));
		
		case ("cmp_GE", X, Y):
			assert(not "TODO");
		
		case ("cmp_EQ", X, Y):
			assert(not "TODO");
		
		case ("cmp_NE", X, Y):
			assert(not "TODO");
		
		# default:
		case _:
			assert(not "TODO");
			# p.asm("cbr", [vn], "->", outs);
	






