import hashlib
import os
import subprocess

virus_prog_path = "../FC"
# virus_prog_path = "../testfc.py"

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def generate_hash_list():
    with open("HashList.txt", "w") as hash_file:
        for i in range(1, 11):
            file_name = f"{i}.txt"
            if os.path.exists(file_name):
                file_hash = calculate_sha256(file_name)
                hash_file.write(f"{file_name}: {file_hash}\n")

def run_fc_program():
    try:
        subprocess.run([virus_prog_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске программы FC: {e}")

report_hashes = {}

def compare_hashes():
    modified_files = []
    infected_files = []
    report_hashes['changed'] = {}
    report_hashes['infected'] = {}
    with open("HashList.txt", "r") as hash_file:
        original_hashes = {line.split(": ")[0]: line.split(": ")[1].strip() for line in hash_file.readlines()}
    report_hashes['origin'] = original_hashes
    with open("VirusHashList.txt", "r") as virus_file:
        virus_hashes = {line.strip() for line in virus_file.readlines()}
    for i in range(1, 11):
        file_name = f"{i}.txt"
        if os.path.exists(file_name):
            current_hash = calculate_sha256(file_name)
            if original_hashes.get(file_name) != current_hash:
                modified_files.append(file_name)
                report_hashes['changed'][file_name] = current_hash
            current_hash_upper = current_hash.upper()
            if current_hash_upper in virus_hashes:
                infected_files.append(file_name)
                report_hashes['infected'][file_name] = current_hash

    return modified_files, infected_files

def main():
    generate_hash_list()
    run_fc_program()
    
    modified, infected = compare_hashes()
    
    if modified:
        print("Измененные файлы:")
        for file in modified:
            print(file)
    else:
        print("Нет измененных файлов.")

    if infected:
        print("Зараженные файлы:")
        for file in infected:
            print(file)
    else:
        print("Нет зараженных файлов.")

    for file in infected:
        os.remove(file) 
    
    print("report.txt")
    for var in 'origin', 'changed', 'infected':
        print(var, 'hash:')
        for file, h in report_hashes[var].items():
            print(file, '-', h)

if __name__ == "__main__":
    main()
