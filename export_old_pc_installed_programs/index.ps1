$paths = @(
    'Registry::HKEY_LOCAL_MACHINE\OLD_SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
    'Registry::HKEY_LOCAL_MACHINE\OLD_SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
)

$apps = foreach ($path in $paths) {
    if (Test-Path $path) {
        Get-ChildItem $path | ForEach-Object {
            $app = Get-ItemProperty $_.PSPath
            if ($app.DisplayName) {
                [PSCustomObject]@{
                    Name      = $app.DisplayName
                    Version   = $app.DisplayVersion
                    Publisher = $app.Publisher
                }
            }
        }
    }
}

$apps = $apps | Sort-Object Name -Unique

$apps | Export-Csv "$env:USERPROFILE\Desktop\Old-PC-Programs.csv" -NoTypeInformation -Encoding UTF8

$apps | Format-Table -AutoSize
