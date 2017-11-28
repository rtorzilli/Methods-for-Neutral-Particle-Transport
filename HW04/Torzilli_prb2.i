PWR Single Pin
c ******* Cell *******
1 1 -10.41 -1 -10 20 imp:n=1
2 0 1 -2 -10 20 imp:n=1
3 3 -6.55 2 -3 -10 20 imp:n=1
4 4 -0.7 3 -5 6 -7 8 -10 20 imp:n=1
5 0 5:-6:7:-8:10:-20 imp:n=0

c ****** Surfaces *******
c Rods dimensions
1 cz 0.41
2 cz 0.42
3 cz 0.48
c Basic lattice cell
*5 px 0.63
*6 px -0.63
*7 py 0.63
*8 py -0.63
c Axial limits
*10 pz 200.0
*20 pz -200.0

c ***** Data *******
c Material 1
m1 8016.73c 2.0
   92235.73c 0.05
   92238.73c 0.95
c Material 4
m4 1001.71c 2
   8016.71c 1
   mt4 lwtr.04t
c Material 3
m3 40000.58c 1.
c ****** Tallies *******
fc4 Tally 4
f4:n 1 3 4
e4:n 1e-6 1. 20.
fc14 Tally 14
f14:n 1
fm14 (1 1 (-2) (-6))
c *************
kcode 1000 1.00 50 250
ksrc 0. 0. 0.
print
mode n