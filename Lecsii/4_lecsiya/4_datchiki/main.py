import html_creater as hc
import xml_generator as xg
import data_provider as dp
import user_interface as ui
import logger as log



t = ui.temperature_view(log.temperature_logger(dp.get_temperature(1)))
print(t)

# print(hc.create())
# print(xg.create())

# hc.new_create(xg.new_create(dp.data_collection()))