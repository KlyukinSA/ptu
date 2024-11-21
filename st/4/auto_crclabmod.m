probs = [0.05 0.01 0.005];

params = [7 "[3; 1; 0]";
    15 "[4; 1; 0]";
    15 "[8; 7; 6; 4; 0]";
    15 "[10; 8; 5; 4; 2; 1; 0]";
    31 "[5; 2; 0]";
    31 "[10; 9; 8; 6; 5; 3; 0]";
    31 "[15; 11; 10; 9; 8; 7; 5; 3; 2; 1; 0]";

    % 31 "[20; 18; 17; 13; 10; 9; 7; 6; 4; 2; 0]";
    % 31 "[25; 24; 21; 19; 18; 16; 15; 14; 13; 11; 9; 5; 2; 0]";

    63 "[6; 1; 0]";
    63 "[12; 10; 8; 5; 4; 3; 0]";
    63 "[18; 17; 16; 15; 9; 7; 6; 3; 2; 1; 0]";

    % 63 "[24; 23; 22; 20; 19; 17; 16; 13; 10; 9; 8; 6; 5; 4; 2; 1; 0]";
    % 63 "[27; 22; 21; 19; 18; 17; 15; 8; 4; 1; 0]";
    % Error in 'crclabmod2/CRC Syndrome Detector': Only generator polynomials of degree 32 or less are allowed.
    % 63 "[33; 32; 30; 29; 28; 27; 26; 23; 22; 20; 15; 14; 13; 11; 9; 8; 6; 5; 2; 1; 0]";
    % 63 "[39; 38; 37; 36; 34; 33; 31; 28; 27; 25; 23; 22; 17; 11; 8; 5; 0]";
    % 63 "[45; 43; 42; 41; 40; 37; 36; 31; 29; 28; 26; 24; 21; 19; 16; 15;
    % 14; 12; 9; 8; 7; 6; 4; 2; 0]";
];

TableData = {'0', '0', '0', '0', '0', '0', '0'};
assignin('base', 'TableData', TableData);

for i = 1:length(probs)
    for j = 1:length(params)
        j
        dsize = str2num(params(j, 1));
        assignin('base', 'dsize', dsize);
        oneprob = probs(i);
        assignin('base', 'oneprob', oneprob);
        genpoly = str2num(params(j, 2));
        assignin('base', 'genpoly', genpoly);
        blocksToStop = 10000000;
        assignin('base', 'blocksToStop', blocksToStop);
        errorsToStop = 100;
        assignin('base', 'errorsToStop', errorsToStop);

        sim('crclabmod2.slx')

        assignin('base', 'NumOfErrors', NumOfErrors);
        assignin('base', 'ErrorsDetected', ErrorsDetected);
        assignin('base', 'PacketsTransmitted', PacketsTransmitted);
        TableData = evalin('base', 'TableData');
        if (cell2mat(TableData(1,7)) == '0')
            TableData = {num2str(dsize) num2str(oneprob) mat2str(genpoly) num2str(PacketsTransmitted-NumOfErrors-ErrorsDetected) num2str(ErrorsDetected) num2str(NumOfErrors) num2str(PacketsTransmitted)};
        else 
            TableData = [TableData; {num2str(dsize) num2str(oneprob) mat2str(genpoly) num2str(PacketsTransmitted-NumOfErrors-ErrorsDetected) num2str(ErrorsDetected) num2str(NumOfErrors) num2str(PacketsTransmitted)}];
        end
        assignin('base', 'TableData', TableData);
    end
end

datei = fopen(uiputfile({'*.csv', 'Comma-separated Values'}), 'w');
separator = ',';
decimal = '.';
TableData = evalin('base', 'TableData');
for z=1:size(TableData, 1)
    for s=1:size(TableData, 2)
        
        var = eval(['TableData{z,s}']);
        % If zero, then empty cell
        if size(var, 1) == 0
            var = '';
        end
        % If numeric -> String
        if isnumeric(var)
            var = num2str(var);
            % Conversion of decimal separator (4 Europe & South America)
            % http://commons.wikimedia.org/wiki/File:DecimalSeparator.svg
            if decimal ~= '.'
                var = strrep(var, '.', decimal);
            end
        end
        % If logical -> 'true' or 'false'
        if islogical(var)
            if var == 1
                var = 'TRUE';
            else
                var = 'FALSE';
            end
        end
        % If newer version of Excel -> Quotes 4 Strings
        var = ['"' var '"'];
        
        % OUTPUT value
        fprintf(datei, '%s', var);
        
        % OUTPUT separator
        if s ~= size(TableData, 2)
            fprintf(datei, separator);
        end
    end
    if z ~= size(TableData, 1) % prevent a empty line at EOF
        % OUTPUT newline
        fprintf(datei, '\n');
    end
end
fclose(datei);

