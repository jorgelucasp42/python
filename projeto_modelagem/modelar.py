from modeller import *
from modeller.automodel import *

env = environ()
env.io.atom_files_directory = ['./templates']

# Alinhamento entre o FASTA e o template
aln = alignment(env)
mdl = model(env, file='4HPG', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4HPG', atom_files='4HPG.pdb')
aln.append(file='target.fasta', align_codes='target')
aln.align2d()
aln.write(file='target-4HPG.ali', alignment_format='PIR')
aln.write(file='target-4HPG.pap', alignment_format='PAP')

# Modelagem
a = automodel(env,
              alnfile='target-4HPG.ali',
              knowns='4HPG',
              sequence='target',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
