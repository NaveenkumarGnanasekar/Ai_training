config = {
    "host": "localhost",
    "port": 5432,
    "debug": True
}
required = {"host", "port", "timeout"}
config_keys = set(config.keys())
missing = required - config_keys
extra = config_keys - required
print("Missing:", missing)
print("Extra:", extra)