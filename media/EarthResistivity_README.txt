1.  Copy Earth Resistivity folder from er.zip to c:\
2.  Try running C:\Earth Resistivity\EarthResist.exe
3.  If error message:  "Component 'MSCOMCTL.OCX' or one of its dependencies not correctly registered: a file is missing or invalid" then in an ADMIN command window:

cd C:\Earth Resistivity
regsvr32 mscomctl.ocx
regsvr32 MSCOMM32.OCX
regsvr32 EPESeralIO.OCX

4.  Run C:\Earth Resistivity\EarthResist.exe
5.  Click 'Please Read' button.  Click OK, close text editor, then 'Yes for OCX path'.
6.  Click 'Download Data' button.  The dialogue that appears should show radio buttons for PIC1 and PIC2.
