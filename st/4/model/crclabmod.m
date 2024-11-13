function varargout = crclabmod(varargin)
% CRCLABMOD MATLAB code for crclabmod.fig
%      CRCLABMOD, by itself, creates a new CRCLABMOD or raises the existing
%      singleton*.
%
%      H = CRCLABMOD returns the handle to a new CRCLABMOD or the handle to
%      the existing singleton*.
%
%      CRCLABMOD('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CRCLABMOD.M with the given input arguments.
%
%      CRCLABMOD('Property','Value',...) creates a new CRCLABMOD or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before crclabmod_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to crclabmod_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help crclabmod

% Last Modified by GUIDE v2.5 24-Sep-2015 01:18:11

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @crclabmod_OpeningFcn, ...
                   'gui_OutputFcn',  @crclabmod_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before crclabmod is made visible.
function crclabmod_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to crclabmod (see VARARGIN)

% Choose default command line output for crclabmod
handles.output = hObject;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes crclabmod wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = crclabmod_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
 TableData = {'0', '0', '0', '0', '0', '0', '0'};
 assignin('base', 'TableData', TableData);


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
 TableData = {'0', '0', '0', '0', '0', '0', '0'};
 assignin('base', 'TableData', TableData);
 set(handles.uitable2,'data',TableData);
 
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
function pushbutton2_Callback(hObject, eventdata, handles)
 x = get(handles.edit1,'String');
 if isempty(x)
   fprintf('„O„Š„y„q„{„p: „r„r„u„t„y„„„u „‚„p„x„}„u„‚ „q„|„€„{„p „t„p„~„~„„‡!t\n');
 else
   dsize = str2num(x);
   assignin('base', 'dsize', dsize);
 end
 x = get(handles.edit2,'String'); 
 if isempty(x)
   fprintf('„O„Š„y„q„{„p: „r„r„u„t„y„„„u „r„u„‚„€„‘„„„~„€„ƒ„„„Ž „€„Š„y„q„{„y!t\n');
 else
   oneprob = str2double(x);
   assignin('base', 'oneprob', oneprob);
 end
 x = get(handles.edit3,'String'); 
 if isempty(x)
   fprintf('„O„Š„y„q„{„p: „r„r„u„t„y„„„u „„€„|„y„~„€„}!t\n');
 else
   genpoly = str2num(x);
   assignin('base', 'genpoly', genpoly);
 end
 x = get(handles.edit6,'String'); 
 if isempty(x)
   fprintf('„O„Š„y„q„{„p: „r„r„u„t„y„„„u „‰„y„ƒ„|„€ „q„|„€„{„€„r „t„€ „€„ƒ„„„p„~„€„r„{„y!t\n');
 else
   blocksToStop = str2num(x);
   assignin('base', 'blocksToStop', blocksToStop);
 end
 x = get(handles.edit7,'String'); 
 if isempty(x)
   fprintf('„O„Š„y„q„{„p: „r„r„u„t„y„„„u „‰„y„ƒ„|„€ „€„Š„y„q„€„{ „t„€ „€„ƒ„„„p„~„€„r„{„y!t\n');
 else
   errorsToStop = str2num(x);
   assignin('base', 'errorsToStop', errorsToStop);
 end
 
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
 set(handles.uitable2,'data',TableData);
 
function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
datei = fopen(uiputfile({'*.csv', 'Comma-separated Values'}), 'w');
separator = ';';
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


function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
