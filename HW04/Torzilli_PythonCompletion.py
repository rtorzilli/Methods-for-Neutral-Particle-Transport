import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Define the MACROSCOPIC cross-section [cm^-1] 
h20XSec = {"scatter": 1.1, "abs": 0.1}
uXSec =  {"scatter": 2.1, "abs": 1.5}

# Define problem boundaries locations
boundaries = [0, .1, .4, .5, .8]
volumes = np.array([.1, .3, .1, .3])

# Define the materials and total cross-section in each boundary
materials = [0, 1, 0, 1]
totXSec = [3.6, 1.2, 3.6, 1.2]

# Define pdfs
xSecPDF = [{"scatter": 0.583, "abs": 0.417}, {"scatter": 0.917, "abs": 0.083}]

# Define a CDF
xSecCDF =  [{"scatter": (0.0, 0.583), "abs": (0.583, 1.0)}, {"scatter": (0.0, 0.917), "abs": (0.917, 1.0)}]

# Create a function to sample discrete CDFs
def sampDiscrete(cdf):
    r = np.random.rand()
    for k, v in cdf.iteritems():
        if r > v[0] and r < v[1]:
            return k
        
# Test your discrete function
tally = {"scatter": 0, "abs": 0}
for i in range(10000):
    tally[sampDiscrete(xSecCDF[0])] += 1

print tally

class Particle(object):
    """!
    The class creates a particle object that represents the history of a 
    transport particle. This class is created with this simplified 1D 
    problem in mind, but it could be extended to further dimensions.
    """

    ##
    def __init__(self, xLoc=0.0, direction=1, energy=2.45, cell=0):
        """!
        Constructor to build the particle class.
        @param self: <em> object pointer </em> \n
            The object pointer. \n
        @param xLoc: \e float \n
            The x coordinate location history. \n
        @param direction: \e integer \n
            The direction of the particle - options are +/-1. \n
        @param energy: \e float \n
            The energy of the particle. \n
        @param cell: \e integer \n
            The current cell location of the particle. \n
        """

        ## @var xLoc: \e float
        # The x coordinate location history.
        self.xLoc = xLoc
        ## @var direction: \e integer
        # The direction of the particle - options are +/-1.
        self.direction = direction
        ## @var energy: \e float
        # The energy of the particle.
        self.energy = energy
        ## @var cell: \e integer
        # The current cell location of the particle.
        self.cell = cell
        ## @var tally: <em> list of floats </em>
        # The tally of the path length traversed by cell
        self.tally = np.array([0., 0., 0., 0.])

    def __repr__(self):
        """!
        Particle print function.
        @param self: <em> particle pointer </em> \n
            The particle pointer. \n
        """
        return "Particle({}, {}, {})".format(self.xLoc, self.energy,
                                            self.cell)

    def __str__(self):
        """!
        Human readable particle print function.
        @param self: <em> particle pointer </em> \n
            The particle pointer. \n
        """

        header = ["\Particle:"]
        header += ["X        E      Cell"]
        header = "\n".join(header)+"\n"
        tmp = ""
        tmp += "{0:<7}{1}{2}\n".format(self.xLoc, self.energy, self.cell)
        header = header + tmp
        return header
		


#! Write a function to sample the number of MFP and save it to the particle class
def calcNumMFP(particle):
    r = np.random.rand()
    particle.numMFP=-np.log(r)
    
# Calculate the distance to the next collision given a number of collisions and a total cross-section
def distToCol(numMFP, xSec):
    return numMFP/xSec
	
#! Write a function to calculate the distance to the next boundary
def calcDistToBound(particle, bounds):
    if particle.direction == 1:
        return bound[particle.cell + 1] - particle.xLoc
    elif particle.direction == -1:
        return particle.xLoc - bound[particle.cell]
    else:
        print "Error: your particle is moving awkwardly!"

def updateEnergy(particle):
    particle.energy = particle.energy - np.random.rand()*(particle.energy)
	
def updateDir(particle):
    r = np.random.rand()
    if r < 0.5:
        particle.direction = particle.direction*-1 
    else:
        particle.direction = particle.direction*1
		
#! Write a function to transport a particle from the branch point in Figure 1 from Lesson 9 notes.
def transport(particle, s_b, s_c, CDF, materials, bounds, totXSec):
    while particle.energy>0:
        if s_c<s_b:
            particle.xLoc= particle.xLoc+s_c*particle.direction
            particle.tally[particle.cell]+=s_c
            if sampDiscrete(CDF)=='scatter':
                updateDir(particle)
                updateEnergy(particle)
                calcNumMFP(particle)
                distToCol(particle.numMFP, totXSec[particle.cell])
                calcDistToBound(particle, bounds)

            if sampDiscrete(CDF)=='abs':
                return
        if s_c>s_b:
			#Particle did not escape
				#Return to B
				if sampDiscrete(CDF)=='scatter':
					updateDir(particle)
					updateEnergy(particle)
					calcNumMFP(particle)
					distToCol(particle.numMFP, totXSec[particle.cell])
					calcDistToBound(particle, bounds)
			#Particle Escaped
				#Tally
				# Was Last Particle	
					#Determine Scalar flux
					#Write ouput
				# Was not last Particle
					# Return to A
					
        else: 
            print('particle has not transported')
			
#! Write the main controller program using the classes and functions defined above
N = 2000
tally = np.array([0., 0., 0., 0.])

for i in range(N):