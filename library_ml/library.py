import numpy as np

def read_xyz(filename, multi = False):
    '''
    read_xyz(filename) -> natoms, atoms, coords

    Reads file in XYZ format and return list of atoms and numpy
    arrays of coordinates.
    '''

    if multi == False:
        atoms = []
        coord = []

        with open(filename) as xyz:
            n_atoms = int(xyz.readline())
            title = xyz.readline()
            for i in range(n_atoms):
                temp = xyz.readline().split()
                atoms.append(temp[0].capitalize())
                coord.append([float(temp[1]), float(temp[2]), float(temp[3])])

        coords = np.array(coord)

        return n_atoms, atoms, coords
    else:
        # open file
        with open(filename, 'r') as file:
            lines = file.readlines()

        n_atoms = int(lines[0])

        # get number of frames
        n_frames = 0
        for line in lines:
            try:
                if int(line) == n_atoms:
                    n_frames += 1
            except:
                pass

        # get atom symbols
        atoms = []
        for i in range(n_atoms):
            atoms.append(lines[i+2].split()[0])

        # assemble all structures
        trajectory = []
        counter = 0

        for i in range(n_frames):
            molecule = []
            # skip the first two lines
            counter += 2

            for j in range(n_atoms):
                molecule.append(lines[counter].split()[1:])
                counter += 1

            trajectory.append(np.array(molecule, dtype='float'))

        return n_atoms, atoms, trajectory

