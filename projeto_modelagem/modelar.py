from modeller import *
from modeller.automodel import *

env = environ()
env.io.atom_files_directory = ['./templates']

# Modelagem com base no alinhamento pronto
a = automodel(env,
              alnfile='target-4HPG.ali',  # arquivo .ali gerado no ClustalW
              knowns='4HPG',              # nome do template no .ali
              sequence='target',         # nome da sequência alvo no .ali
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5
a.make()
