from actor import Actor
from operator import add
from functools import reduce
from role_parser import RoleParser

def read_line(iterator):
    try:
        line = next(iterator).strip()
    except UnicodeDecodeError:
        while True:
            try:
                while not 'line' in vars() or line != '':
                    line = next(iterator).strip()
            except UnicodeDecodeError:
                continue
            break
    return line

def skip_current_actor(iterator) -> str:
    while True:
        try:
            while not 'line' in vars() or line != '':
                line = next(iterator).strip()
        except UnicodeDecodeError:
            continue
        break
    return line

outfile = open("output.txt", 'w')

def print_actor_to_file(actor: Actor):
    outfile.write(actor.to_postgres_format() + '\n')

def parse_file(file_name):
    count = 0
    current_actor = Actor()
    read_new_line = True
    with open(file_name, errors='ignore') as file:
        file_iter = iter(file)
        try:
            while True:
                if count % 10000 == 0:
                    print(count)
                if read_new_line:
                    line = read_line(file_iter)
                if line == '':
                    print_actor_to_file(current_actor)
                    count += 1
                    current_actor = Actor()
                    line = read_line(file_iter)
                    name_string = line[:line.find('\t')]
                    if ',' in name_string:
                        current_actor.actor_name = name_string.split(',')[1].strip() + ' ' + name_string.split(',')[0].strip()
                    else:
                        current_actor.actor_name = name_string
                    line = line[line.find('\t'):]
                try:
                    current_actor.roles.append(RoleParser.parse_line(line))
                    read_new_line = True
                except StopIteration:
                    break
                except Exception as e:
                    if count > 310000 == 0:
                        print(str(e))
                    line = skip_current_actor(file_iter)
                    read_new_line = False
                    continue
                read_new_line = True
                
        except StopIteration:
            pass


def main():
    parse_file('../actors.list.txt')


if __name__ == "__main__":
    main()
