from role import Role

class RoleParser:
    @staticmethod
    def parse_line(line: str) -> Role:
        role = Role()
        line = line.strip()
        rest_line = line.split()
        RoleParser.__extract_title(role, rest_line)
        RoleParser.__extract_year(role, rest_line)

        if RoleParser.__has_series_name(rest_line):
            RoleParser.__extract_series_name(role, rest_line)

        if RoleParser.__has_as_character(rest_line):
            RoleParser.__extract_as_character(role, rest_line)

        while RoleParser.__has_type(rest_line):
            RoleParser.__extract_type(role, rest_line)

        RoleParser.__extract_character_name(role, rest_line)

        if RoleParser.__has_credit(rest_line):
            RoleParser.__extract_credit(role, rest_line)
        
        return role

    @staticmethod
    def __extract_title(role: Role, rest_line: list):
        title = ""
        count = 0
        for word in rest_line:
            if word[0] == "(":
                break
            title += ' ' + word
            count += 1
        role.title = title.strip()
        for _ in range(count):
            rest_line.pop(0)

    @staticmethod
    def __extract_year(role: Role, rest_line: list):
        year_word = rest_line.pop(0)
        actual_year = year_word[1:5]
        if actual_year[0] == "?":
            actual_year = 0
        else:
            actual_year = int(actual_year)
        role.year = actual_year

    @staticmethod
    def __has_series_name(rest_line: list):
        return len(rest_line) > 0 and rest_line[0][0] == "{"

    @staticmethod
    def __extract_series_name(role: Role, rest_line: list):
        count = 0
        series_name = ''
        for word in rest_line:
            if word[0] == '{':
                word = word[1:]
            if word[len(word)-1] == '}':
                word = word[:-1]
                series_name += ' ' + word
                count += 1
                break
            series_name += word + ' '
            count += 1

        for _ in range(count):
            rest_line.pop(0)

        role.series_name = series_name.strip()

    @staticmethod
    def __has_as_character(rest_line: list):
        return len(rest_line) != 0 and (
            rest_line[0][1:3] == "as" or rest_line[0][1:5] == "also"
        )
    
    @staticmethod
    def __extract_as_character(role: Role, rest_line: list):
        as_character = ''
        count = 0

        if str(rest_line[0]).startswith('(as'):
            rest_line.pop(0)
        else:
            rest_line.pop(0)
            rest_line.pop(0)
        
        for word in rest_line:
            if word[len(word)-1] == ')':
                word = word[:-1]
                as_character += word
                count += 1
                break

            as_character += word + ' '
            count += 1

        for _ in range(count):
            rest_line.pop(0)

        role.as_character = as_character.strip()

    @staticmethod
    def __has_type(rest_line: list):
        return len(rest_line) > 0 and rest_line[0][0] == '('
    
    @staticmethod
    def __extract_type(role: Role, rest_line: list):
        role.types += rest_line.pop(0)[1:-1]

    @staticmethod
    def __has_credit(rest_line: list):
        return len(rest_line) > 0 and rest_line[0][0] == '<'

    @staticmethod
    def __extract_credit(role: Role, rest_line: list):
        role.credit = rest_line.pop(0)[1:-1]

    @staticmethod
    def __extract_character_name(role: Role, rest_line: list):
        character_name = ''
        count = 0
        for word in rest_line:
            if word[0] == '[':
                word = word[1:]
            if word[len(word)-1] == ']':
                word = word[:-1]
                character_name += word
                count += 1
                break

            character_name += word + ' '

        for _ in range(count):
            rest_line.pop(0)
        
        role.character_name = character_name.strip()

if __name__ == '__main__':
    line = 'From the Woods: The Discovery of LYB (????)  (as Country $torm)  [Himself]'    
    role = RoleParser.parse_line(line)
    print("Testing finished")
