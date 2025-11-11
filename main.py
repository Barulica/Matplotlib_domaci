import matplotlib.pyplot as plt


x = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']
y = [22, 34, 13, 15, 27, 18, 16]

najtoplije_vreme = max(y)
najtopliji_dan = x[y.index(najtoplije_vreme)]

print(najtopliji_dan)

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Vremenska prognoza')
plt.grid(True)

plt.scatter (najtopliji_dan, najtoplije_vreme, s = 100, zorder = 5, color = 'red')
plt.annotate("Najtopliji dan", xy= (najtopliji_dan, najtoplije_vreme), zorder = 6)

plt.show()