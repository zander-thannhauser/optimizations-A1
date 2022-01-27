
from lookup import vrtovn;

def process_call(ops, ins, _):
	# p.casm("call", ins);
	ops.append(("call", [ins[0]] + [vrtovn(i) for i in ins[1:]], "", []));
	after_call();
