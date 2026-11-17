# Export Old PC Installed Programs

### A PowerShell script that extracts installed program information from an old Windows installation and exports it to a CSV file.

#### Requirements
Access to the old Windows drive.
PowerShell running as **Administrator**.
Usage

1. Mount the old Windows registry hive:

**powershell:**

```reg load HKLM\OLD_SOFTWARE "D:\Windows\System32\Config\SOFTWARE"```

*Replace D: with the old Windows drive letter.*

2. Run the script:

**powershell:**

```.\Export-OldPC-InstalledPrograms.ps1```


3. Unload the registry hive when finished:

**powershell:**

```reg unload HKLM\OLD_SOFTWARE```

Output

The script generates:

```Old-PC-Programs.csv```

The CSV is saved to your Desktop and contains:

```Program Name
Version
Publisher
Notes
```
*The script reads both 32-bit and 64-bit uninstall registry entries.
It does not install, modify, or uninstall any programs.
Make sure to unload the registry hive after use.*
