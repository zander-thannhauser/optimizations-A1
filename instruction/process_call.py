
def process_call(ins, outs, p):
	p.casm("call", ins, "=>", outs);
	# the only register you can rely on now is %vr{0,1,2,3}
	assert(not "TODO");

