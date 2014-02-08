from .moarjson import Moarjson


json = Moarjson('GlobalMoarJson')
register = json.register
register_with_fields = json.register_with_fields
dump = json.dump
dumps = json.dumps
load = json.load
loads = json.loads
