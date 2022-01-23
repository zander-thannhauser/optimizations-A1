
def process_call(ops, ins, outs):
	p.casm("call", ins, "=>", outs);
	# the only register you can rely on now is %vr{0,1,2,3} (and the registers
	# from moves)
	assert(not "TODO");

