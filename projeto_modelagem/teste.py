from modeller import *
env = environ()
aln = alignment(env)
aln.append(file='target-4HPG.ali', align_codes='4HPG')
aln.append(file='target-4HPG.ali', align_codes='target')
print("Alinhamento carregado com sucesso!")
