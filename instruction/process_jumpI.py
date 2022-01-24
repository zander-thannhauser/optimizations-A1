
def process_jumpI(ops, ins, outs):
	# p.casm("jumpI", ins, "->", outs);
	ops.append(("jumpI", ins, "->", outs));
