# Comprehensive Audit Script for NosFuimosdeFinca Documentation

$docsDir = "c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\docs"
$guideDir = "c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide"

Write-Host "=========================================================="
Write-Host "COMPREHENSIVE DOCUMENTATION AUDIT: NosFuimosdeFinca"
Write-Host "=========================================================="

$phases = Get-ChildItem -Path $docsDir -Directory

foreach ($phase in $phases) {
    $files = Get-ChildItem -Path $phase.FullName -Recurse -File
    Write-Host "Phase: $($phase.Name) -> Count: $($files.Count) files"
}

Write-Host "----------------------------------------------------------"
Write-Host "Checking synchronization between guide/ and docs/07-implementation/guide/"

$guideFiles = Get-ChildItem -Path $guideDir -Recurse -File
$mismatches = 0
$missing = 0

foreach ($file in $guideFiles) {
    $rel = $file.FullName.Substring($guideDir.Length)
    $target = "$docsDir\07-implementation\guide$rel"
    
    if (-not (Test-Path -Path $target)) {
        Write-Host "Missing file in docs: $rel"
        $missing++
    } else {
        $h1 = (Get-FileHash -Path $file.FullName).Hash
        $h2 = (Get-FileHash -Path $target).Hash
        if ($h1 -ne $h2) {
            Write-Host "Hash mismatch in: $rel"
            $mismatches++
        }
    }
}

Write-Host "----------------------------------------------------------"
Write-Host "Guide Sync Audit Results: Missing=$missing, Mismatches=$mismatches"
Write-Host "=========================================================="
