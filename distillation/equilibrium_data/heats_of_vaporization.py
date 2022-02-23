class dH_vap:
    """Heat of vaporization"""
    def __init__(self, compound_name, verbose=False):
        from distillation import os, ROOT_DIR
        file = os.path.join(ROOT_DIR, 'equilibrium_data', 'heats_of_vaporization.csv')
        self.units = 'J/kmol'
        with open(file, 'r') as f:
            header = next(f).rstrip('\n').split(',')
            for line in f:
                vals = line.rstrip('\n').split(',')
                if vals[0] == compound_name:
                    self.C1 = float(vals[header.index('C1')]) * 1e7
                    self.C2 = float(vals[header.index('C2')])
                    self.C3 = float(vals[header.index('C3')])
                    self.C4 = float(vals[header.index('C4')])
                    self.T_ref = float(vals[header.index('T_ref [K]')])
                    self.T_ci = float(vals[header.index('T_ci [K]')])
                    self.T_r = self.T_ref/self.T_ci
                    # Value in J/kmol
                    self.value = self.C1 * ((1-self.T_r) ** (self.C2 + (self.C3*self.T_r) + (self.C4*self.T_r*self.T_r)))

        if verbose:
            print('Assuming heat of vaporization of %s is constant at %e kJ/mol' % (compound_name, self.value/1e6))

    def eval(self):
        return self.value
