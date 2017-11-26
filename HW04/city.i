This models a simple NW neutron burst and models a simple city-scape.
c
c Simple NW det scenario.  A NW is set off on the edge of the city.  To start, let's create
c a scale model.  The key factors for the model: 
c
c 1) Model three "city blocks" of long apartment buldings.  The buildings are .3 m high,
c    .3m wide, and 1.0 m long separated by 0.15 m of air. The walls are .03 m thick concrete.
c 2) The flux is tallied inside of a car modeled as a 0.1 wide, 0.15 m tall, and 0.25 m long
c    aluminum box with 0.0025 m thick walls. The car is located on the far side of the 3rd
c    block from the source.
c 3) Add a volume flux tally to the inside of the car.
c 4) The source is modeled as a point fission source (Watt spectrum) from a HEU bomb. 
c Centered 1 m away from the far buliding from car
c
c *******************************************************************************************
c  Cell Cards ID Mat Den Surfaces
c *******************************************************************************************
c create a kill zone 
9 0 99 imp:n=0
c Buildings
1  1 -2.3      11 -1 imp:n=1 $ Conrete wall for Bldg 
11 2 -.001205 -11    imp:n=1 $ Air Gap in Blg
3  1 -2.3      33 -3 imp:n=1 $ Conrete wall for Bldg 
33 2 -.001205 -33    imp:n=1 $ Air Gap in Blg
2  1 -2.3      22 -2 imp:n=1 $ Conrete wall for Bldg 
22 2 -.001205 -22    imp:n=1 $ Air Gap in Blg
c Cars
5  3 -2.6989  -5 55 imp:n=1
55 2 -.001205 -55   imp:n=1
c Outside
99 2 -.001205 -99 1 3 2 5 imp:n=1

c *******************************************************************************************
c Surfaces
c *******************************************************************************************
c Buildings
1  BOX -450 0 0      300 0 0   0 1000 0  0 0 300 
11 BOX -420 30 1e-6   240 0 0   0 940 0   0 0 240 $ .03 meter thick wall
2  BOX  450 0 0      300 0 0   0 100 0   0 0 300
22 BOX  480 30 1e-6  240 0 0   0 940 0   0 0 240 $ .03 meter thick wall
3  BOX  0 0 0        300 0 0   0 1000 0  0 0 300
33 BOX  30 30 1e-6     240 0 0   0 940 0   0 0 240 $ .03 meter thick wall
c Universe
99 BOX -600 -100 -100   1500 0 0   0 1200 0  0 0 900
c Car
5  BOX 755  500 1e-6      100 0 0    0 250 0     0 0 150
55 BOX 7575 502.5 1e-6  95 0 0   0 245 0   0 0 145
6  BOX 755  500 1e-6      100 0 0    0 250 0     0 0 150
66 BOX 7575 502.5 1e-6  95 0 0   0 245 0   0 0 145
7  BOX 755  500 1e-6      100 0 0    0 250 0     0 0 150
77 BOX 7575 502.5 1e-6  95 0 0   0 245 0   0 0 145

c *******************************************************************************************
c Data Cards
c *******************************************************************************************
c Concrete default room temperature density=2.30 g/cc
M1 1001 -0.0221
   6012 -0.002484
   8016 -0.57493
   11023 -0.015208
   12000 -0.001266
   13027 -0.019953
   14000 -0.304627
   19000 -0.010045
   20000 -0.042951
   26000 -0.006435
c Air Temp=Default Rm Density = 0.001205 g/cc
M2 6000 -0.000124
   7014 -0.755268
   8016 -0.231781
   18000 -0.012827
c Aluminum Density=2.6989 g/cc
M3 13027 -1.000000
c ASphalt Pavement density=2.578400 g/cc
M4 1001 -.007781
   6000 -.076175
   7014 -.000363
   8016 -.459103
   11023 -.011659
   12000 -.021757
   13027 -.051009
   14000 -.231474
   16000 -.002804
   19000 -.017508
   20000 -.084471
   22000 -.003403
   23000 -.000024
   25055 -.000632
   26000 -.031375
   28000 -.000002
   82000 -.001179