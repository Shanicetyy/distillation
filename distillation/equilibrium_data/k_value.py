def read_chart(f_name):
    data = {}
    with open(f_name, 'r') as f:
        header = next(f).split(',')
        for line in f:
            compound, *vals = line.split(',')
            data[compound] = {
                key: val for key, val in zip(header[1:], vals)
            }

    return data


class KVal:
    def __init__(self, compound, verbose=False):
        from distillation import ROOT_DIR, os
        f_name = os.path.join(ROOT_DIR, 'equilibrium_data', 'depriester.csv')
        data = read_chart(f_name)
        if compound in data.keys():
            my_data = data[compound]
            self.K_type = "depriester"

            self.a_T1 = float(my_data.pop('a_T1'))
            self.a_T2 = float(my_data.pop('a_T2'))
            self.a_T6 = float(my_data.pop('a_T6'))
            self.a_p1 = float(my_data.pop('a_p1'))
            self.a_p2 = float(my_data.pop('a_p2'))
            self.a_p3 = float(my_data.pop('a_p3'))

            if verbose:
                print('Setting DePriester parameters for %s:' % compound)
                print('             a_T1 [deg Rankine^2]:', self.a_T1)
                print('             a_T2 [deg Rankine]:', self.a_T2)
                print('             a_T6 [dimensionless]:', self.a_T6)
                print('             a_p1 [dimensionless]:', self.a_p1)
                print('             a_p2 [psia^2]:', self.a_p2)
                print('             a_p3 [psia]:', self.a_p3)
                print('     K value at 300 K, 1 bar= ', self.eval_SI(300., 1e5))
        else:
            f_name = os.path.join(ROOT_DIR, 'equilibrium_data', 'raoult.csv')
            data = read_chart(f_name)
            if compound in data.keys():
                my_data = data[compound]
                self.K_type = "raoult"

                self.A = float(my_data.pop('A'))
                self.B = float(my_data.pop('B'))
                self.C = float(my_data.pop('C'))

                if verbose:
                    print('Setting Raoult\'s parameters for %s:' % compound)
                    print('                A [deg Rankine^2]:', self.A)
                    print('                B [deg Rankine]:', self.B)
                    print('                C [dimensionless]:', self.C)
                    print('     K value at 300 K, 1 bar= ', self.eval_SI(300., 1e5))
            else:
                raise ValueError('%s not found in either depriester or raoult' % compound)

    def eval(self, T, p):
        """

        :param T: temperature in Rankine
        :param p: pressure in psia
        :return: K-value for component at specific *T* and *p*
        """
        import numpy as np
        if self.K_type == "depriester":
            return np.exp(
                self.a_T1 / T / T + self.a_T2 / T + self.a_T6
                + self.a_p1 * np.log(p) + self.a_p2 / p / p + self.a_p3 / p
            )
        else:
            return np.exp(
                (10^(self.A - self.B/(self.C + T)))/ p
            )

    def eval_SI(self, T, p):
        """

        :param T: temperature in K
        :param p: pressure in Pa
        :return: K-value for component at specific *T* and *p*
        """
        if self.K_type == "depriester":
            from distillation.unit_conversions.temperature import Kelvin_to_Rankine
            from distillation.unit_conversions.pressure import Paa_to_psia
            return self.eval(
                Kelvin_to_Rankine(T), Paa_to_psia(p)
            )
        else:
            from distillation.unit_conversions.temperature import Kelvin_to_Celcius
            from distillation.unit_conversions.pressure import Paa_to_mmHg
            return self.eval(
                Kelvin_to_Celcius(T), Paa_to_mmHg(p)
            )
