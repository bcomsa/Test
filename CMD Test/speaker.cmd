@echo off
echo StrText="Application created Successfully" > spk.vbs
echo set ObjVoice=CreateObject("SAPI.SpVoice") >> spk.vbs
echo ObjVoice.Speak StrText >> spk.vbs
start spk.vbs