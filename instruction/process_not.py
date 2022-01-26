
def process_not(ops, ins, outs):
	# constant-fold:
	# substitutions:
		# not(not(X))        => X
		# not(and(not, not)) => or
		# not( or(not, not)) => and
	assert(not "TODO");

