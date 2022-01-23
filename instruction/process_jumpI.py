
def process_jumpI(ops, ins, outs):
	p.casm("jumpI", ins, "->", outs);
	p.asm("jumpI", ins, "->", outs);
