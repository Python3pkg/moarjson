from .moarjson import Moarjson


json = Moarjson('GlobalMoarJson')
register = json.register
dump = json.dump
dumps = json.dumps
