LoL Server Status
===============================================================================
LoL Server Status is an application for checking servers status of
League of Legends.

Version: **1.2**<br />
Licensed under: **GPL v3**

Download packages
------------------------------------------------------------------------------
- **Latest version 1.2 for Windows: [Download](https://github.com/LuqueDaniel/LoL-Server-Status/releases/tag/1.2) (Size: 11.8 MB)**

**[Download previous versions of packages and executables](https://github.com/LuqueDaniel/LoL-Server-Status/releases)**

Screenshots
------------------------------------------------------------------------------
![screenshot](https://raw.github.com/LuqueDaniel/LoL-Server-Status/master/screenshots/main_window.png)

Dependencies
------------------------------------------------------------------------------
- **[PyQt 4](http://www.riverbankcomputing.co.uk/software/pyqt/download)**
- **[py2exe](http://www.py2exe.org/)** (Compile for Windows)
- **[cx_freeze](http://cx-freeze.sourceforge.net/)** (Compile with cx_freeze)

Changelog
------------------------------------------------------------------------------
See **[changelog.md](https://github.com/LuqueDaniel/LoL-Server-Status/blob/master/changelog.md)** for more information

How compile for Windows
------------------------------------------------------------------------------
**With py2exe:**<br />
For compile LoL Server Status for Windows is necessary **[py2exe](http://www.py2exe.org/)**

In terminal (cmd or console) enter in "LoL-Server-Status" folder and execute the next command.<br />
You may need to include the module "win32con".

```bash
python compile_with_py2exe_windows.py py2exe
```

**With cx_freeze:**<br />
In terminal (cmd or console) enter in "LoL-Server-Status" folder and execute the next command.

```bash
python compile_with_cx_freeze.py build
```

Notes
-----------------------------------------------------------------------------
LoL Server Status has not been tested on Mac. (Help?)
