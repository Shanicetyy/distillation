"""
Sources for :math:`\Delta H_\mathrm{v}` and :math:`C_{\mathrm{p,L}}`
********************************************************************

The heats of vaporization and heat capacities of the liquid
are obtained from [Perry]_

.. automodule:: distillation.equilibrium_data.heat_capacity_liquid
    :members:

.. automodule:: distillation.equilibrium_data.heats_of_vaporization
    :members:


Sources for :math:`K_i(T)`
**************************

The equilibrium properties are taken from
the DePriester charts in [Wankat]_ or using Raoult's law in [Yaws]_

.. automodule:: distillation.equilibrium_data.k_value
    :members:


Source of :math:`C_{\mathrm{p,V}}`
**********************************
The heat capacities of the vapor are currently estimated as a polyatomic ideal gas.

.. automodule:: distillation.equilibrium_data.heat_capacity_vapor
    :members:


.. [Perry] Green, Don W., and Robert H. Perry. Perry's Chemical Engineers' Handbook (8th Edition), McGraw-Hill Professional Publishing, 2007. ProQuest Ebook Central,

.. [Wankat] Wankat, P C. Separation Process Engineering (3rd Edition), Prentice Hall, 2012, p. 33

.. [Yaws] Yaws, C. L. The Yaws Handbook of Vapor Pressure: Antoine Coefficients (2nd Edition), Gulf Professional Publishing, 2015.
"""