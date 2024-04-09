import json

class Actor:
    def __init__(self) -> None:
        self.actor_name = ""
        self.roles = []

    def to_postgres_format(self) -> str:
        res_str = ''
        res_str += self.actor_name + '\t'
        roles_dict = {}
        roles_dict['roles'] = [role.to_dict() for role in self.roles]
        res_str += json.dumps(__class__.__escape_quotes(roles_dict))
        return res_str
    
    @staticmethod
    def __escape_quotes(json_dict: dict) -> dict:
        quote = "\""
        escaped_dict = {}
        for key, value in json_dict.items():
            escaped_key = quote + key + quote  # Escape double quotes in keys
            if isinstance(value, str):
                escaped_value = quote + value.strip("\"").replace('\\', '\\\\').replace('"', '\\"') + quote # Escape double quotes in string values
            elif isinstance(value, dict):
                escaped_value = __class__.__escape_quotes(value)
            elif isinstance(value, list):
                escaped_value = value
                for (i, el) in enumerate(value):
                    if isinstance(el, dict):
                        value[i] = __class__.__escape_quotes(el)
            else:
                escaped_value = value
            escaped_dict[escaped_key] = escaped_value
        return escaped_dict