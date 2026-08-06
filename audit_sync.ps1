$guideFiles = Get-ChildItem -Path "c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide" -Recurse -File

$mismatches = 0
$missing = 0

foreach ($file in $guideFiles) {
    $relativePath = $file.FullName.Substring("c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide".Length)
    $docsPath = "c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\docs\07-implementation\guide" + $relativePath

    if (-not (Test-Path -Path $docsPath)) {
        Write-Host "Missing in docs: $relativePath"
        $missing++
    } else {
        $hash1 = (Get-FileHash -Path $file.FullName).Hash
        $hash2 = (Get-FileHash -Path $docsPath).Hash
        if ($hash1 -ne $hash2) {
            Write-Host "Hash mismatch: $relativePath"
            $mismatches++
        }
    }
}

if ($mismatches -eq 0 -and $missing -eq 0) {
    Write-Host "Audit Result: 100% Congruent. Both guide directories are identical in content and structure."
} else {
    Write-Host "Audit Result: $missing missing files, $mismatches mismatched files."
}
