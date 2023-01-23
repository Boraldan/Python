import data_provider as dp
import logger as log

def temperature_view(senson):
    data = dp.get_temperature(senson)
    log.temperature_logger(data)
    return data


def pressure_view(senson):
    data = dp.get_preassure(senson)
    log.pressure_logger(data)
    return data

    
def wind_speed_view(senson):
    data = dp.get_wind_speed(senson)
    log.wind_speed_logger(data)
    return data

    