names=['john','','alice','','david']
new=['unknown' if n=='' else n for n in names]
print(new)