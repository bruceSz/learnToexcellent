class Env(dict):

	"an environment : a dict of {'var':val} pairs,with an outer Env"
	def __init__(self,parms=(),args=(),outer=None):
		self.update(zip(parms,args))	
		self.outer=outer

	def find(self,var):
		"find the innermost Env where var appears"
		return self if var in self else self.outer.find(var)

def add_globals(env):
	"add some scheme standard procedures to an environment"
	import math,operator,as op
	env.update(vars(math))
	env.update(
		{'+':op.add,'-':op.sub,'*':op.mul,'/':op.div,'not':op.not_,
		'>':op.gt,'<':op.lt}
		)
	return env


def eval(x,env=global_env):
	"evaluate an expression in an 	environment."
	if isa(x,Symbol):
		return env.find(x)[x]
	elif not isa(x,list):
		return x
	elif x[0] == 'quote':
		(_,exp) = x 
		return exp
	elif x[0] == 'if':
		(_,test,conseq,alt) = x
		return eval((conseq if eval(test,env) else alt),alt)
	elif x[0] == 'set!':
		(_,var,exp) = x
		env.find(var)[var] = eval(exp,env)
	elif x[0] == 'define':
		(_,var,exp) = x
		env[var] = eval(exp,env)
	elif x[0] == 'lambda':
		(_,vars,exp) = x
		return lambda *args:eval(exp,Env(vars,args,env))
	elif x[0] == 'begin':
		for exp in x[1:]:
			val = eval(exp,env)
		return val
	else:
		exps = [eval(exp,env) for exp in x]
		proc = exps.pop(0)
		return proc(*exps)

isa = isinstance
Symbol = str
global_env = add_globals(Env())