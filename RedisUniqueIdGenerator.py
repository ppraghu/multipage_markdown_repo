import redis
from datetime import datetime, timedelta, timezone

secret_key = 'xxxx='
azure_redis_host = 'xxxx.redis.cache.windows.net'

r = redis.Redis(host = azure_redis_host, password = secret_key);

# Lua script to increment the value of a key 
# up to an upper limit, then reset to 1
lua_script = """
local function increment_and_reset(key)
    local current_value = redis.call("INCR", key)
    if current_value > 10000 then
        current_value = 1
        redis.call("SET", key, current_value)
    end
    return current_value - 1
end
return increment_and_reset(KEYS[1])
"""

class RedisUniqueIdGenerator:

    def get_current_datetime(self):
        return datetime.now();

    def __init__(self, ais_pod_id):
        self.ais_pod_id = ais_pod_id;
    
    def delete_all_contents(self):
        print("Now deleting all keys & values");
        for key in r.scan_iter():
            r.delete(key);
            print(f"{key} deleted");

    def increment_in_range(self, key):
        result = r.eval(lua_script, 1, key);
        formatted_result = "{:04d}".format(result);
        #print(f"{self.ais_pod_id}: result is {result} for key {key}");
        return formatted_result;

    def get_next_id(self):
        format = "%Y%m%d%H%M";
        format_with_secs = "%Y%m%d%H%M%S";
        current_datetime = self.get_current_datetime();
        current_dt_formatted = current_datetime.strftime(format)
        next_id = self.increment_in_range(current_dt_formatted);
        asup_id_16chars = "{}{}".format(current_dt_formatted, next_id);
        #id_to_return = "{:02d}".format(next_id);
        return next_id, asup_id_16chars, current_datetime.strftime(format_with_secs);

            
