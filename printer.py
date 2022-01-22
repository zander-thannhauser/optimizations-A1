
class printer:
	def __init__(self, filename):
		self.file = open(filename, "w");
		self.identation = 0;
	
	def indent(self):
		self.identation += 1;
	
	def unindent(self):
		self.identation -= 1;
	
	def print(self, string, prefix):
		self.file.write("\t" * self.identation + prefix + string + "\n");
		
	def comment(self, fmt, *args):
		self.printf(fmt, *args, prefix = "# ");
	
	def printf(self, fmt, *args, prefix = "  "):
		self.print(fmt % args, prefix);
	
	def asm(self, cmd, ins = [], arrow = "", outs = [], prefix = "  "):
		self.print(cmd + \
			" " + ", ".join(ins) + \
			" " + arrow + \
			" " + ", ".join(outs), prefix = prefix);
	
	def casm(self, cmd, ins = [], arrow = "", outs = []):
		self.asm(cmd, ins, arrow, outs, prefix = "# ");






















