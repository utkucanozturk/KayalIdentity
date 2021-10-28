def kayaEquation(pop, gdp, energy_intensity, carbon_intensity):
    '''
    Expresses yearly CO2 emissions as a product of four factors.
    :parameter
        :param pop: string - float - population size (in millions)
        :param gdp: float - GDP per capita (in 1000$/person)
        :param energy_intensity: float - Energy Intensity (in Gigajoule/$1000GDP)
        :param carbon_intensity: float - Carbon Intensity (in tonnes CO2/Gigajoule)
    :return
        float - yearly CO2 emissions
    '''

    if pop < 0:
        raise ValueError('Input population should be positive number!')
    if gdp <0:
        raise ValueError('Input GDP should be positive number!')
    if energy_intensity <0:
        raise ValueError('Input energy intensity should be positive number!')
    if carbon_intensity <0:
        raise ValueError('Input cabon intensity should be positive number!')
    
    co2 = pop * gdp * energy_intensity * carbon_intensity
    return co2