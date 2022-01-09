import matplotlib.pyplot as plt
import csv
import matplotlib.patches as mpatches
  
x = []
y = []
X = []
Y = []
  
with open('Fig_1A.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ';')
    next(plots)
      
    for row in plots:
        x.append(row[0].replace(",", "."))
        y.append(row[1])

for i in range(len(x) - 3):
    X.append(float(x[i]))
    Y.append(int(y[i]))

plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')

fig, ax = plt.subplots()
plt.plot(X, Y, color = 'gray')
plt.xlabel('{\\bf Time (min)}', fontsize = 15)
plt.xlim([2.33, 4.16])
plt.ylim([0, 1.1e+9])
plt.ylabel('{\\bf Intensity (cps)}', fontsize = 15)

plt.text(2.35, 1.4e+8, "\\underline{\\bf PtdIns}", fontsize = 15)
plt.text(2.64, 4.5e+8, "\\underline{\\bf PtdEtn}", fontsize = 15)
plt.text(3.27, 4.32e+8, "{\\bf P}\\underline{\\bf Etn-Ce}{\\bf r}", fontsize = 15)
plt.text(3.63, 2.9e+8, "\\underline{\\bf X1}", fontsize = 15, color = "blue")
plt.text(3.54, 1e+8, "{\\bf $|$PtdSer}", rotation = 90, fontsize = 15)
plt.text(3.81, 1.05e+9, "{\\bf P}\\underline{\\bf tdCh}{\\bf o}", fontsize = 15)
plt.text(4.04, 0.8e+8, "\\underline{\\bf SM}", fontsize = 15)
plt.text(2.4, 0.9e+9, "{\\bf HPLC}", fontsize = 20)

fancybox = mpatches.FancyBboxPatch(
    (3.51, 0), 0.25, 0.4e+9,
    boxstyle = mpatches.BoxStyle.Round(pad = 0.03), color = "blue", alpha = 0.06 )
ax.add_patch(fancybox)
plt.tight_layout()
plt.savefig("result.pdf")