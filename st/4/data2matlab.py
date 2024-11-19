data_path = r'C:\Users\user\Documents\MATLAB\crclab\data.txt'

val = ''

with open(data_path) as file:
    for line in file:
        if len(line) < 2:
            continue
        line = line[:-1]
        if len(line) < 5:
            val = line
        else:
            print(val, ' "', line, '";', sep='')

# 7 "[3; 1; 0]";
# 15 "[4; 1; 0]";
# 15 "[8; 7; 6; 4; 0]";
# 15 "[10; 8; 5; 4; 2; 1; 0]";
# 31 "[5; 2; 0]";
# 31 "[10; 9; 8; 6; 5; 3; 0]";
# 31 "[15; 11; 10; 9; 8; 7; 5; 3; 2; 1; 0]";
# 31 "[20; 18; 17; 13; 10; 9; 7; 6; 4; 2; 0]";
# 31 "[25; 24; 21; 19; 18; 16; 15; 14; 13; 11; 9; 5; 2; 0]";
# 63 "[6; 1; 0] ";
# 63 "[12; 10; 8; 5; 4; 3; 0]";
# 63 "[18; 17; 16; 15; 9; 7; 6; 3; 2; 1; 0]";
# 63 "[24; 23; 22; 20; 19; 17; 16; 13; 10; 9; 8; 6; 5; 4; 2; 1; 0]";
# 63 "[27; 22; 21; 19; 18; 17; 15; 8; 4; 1; 0]";
# 63 "[33; 32; 30; 29; 28; 27; 26; 23; 22; 20; 15; 14; 13; 11; 9; 8; 6; 5; 2; 1; 0]";
# 63 "[39; 38; 37; 36; 34; 33; 31; 28; 27; 25; 23; 22; 17; 11; 8; 5; 0]";
# 63 "[45; 43; 42; 41; 40; 37; 36; 31; 29; 28; 26; 24; 21; 19; 16; 15; 14; 12; 9; 8; 7; 6; 4; 2; 0]";
