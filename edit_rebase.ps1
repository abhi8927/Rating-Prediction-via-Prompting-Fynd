param($file)

$content = Get-Content $file
$newContent = @()

foreach ($line in $content) {
    if ($line -match '^pick (c751314)') {
        $newContent += "reword c751314 Rewrite docs to sound more natural"
    }
    elseif ($line -match '^pick (923a188)') {
        $newContent += "reword 923a188 Add all remaining project files"
    }
    elseif ($line -match '^pick (5d4c61c)') {
        $newContent += "reword 5d4c61c Update README status"
    }
    elseif ($line -match '^pick (6e869b9)') {
        $newContent += "reword 6e869b9 Add notebook and report"
    }
    elseif ($line -match '^pick (8148e11)') {
        $newContent += "reword 8148e11 Improve user dashboard UI"
    }
    elseif ($line -match '^pick (7f73e61)') {
        $newContent += "reword 7f73e61 Redesign admin dashboard"
    }
    elseif ($line -match '^pick (50acc39)') {
        $newContent += "reword 50acc39 Fix stats display and timezone"
    }
    elseif ($line -match '^pick (25adeba)') {
        $newContent += "reword 25adeba Update stats design"
    }
    elseif ($line -match '^pick (0b62c83)') {
        $newContent += "reword 0b62c83 Add Render deployment config"
    }
    else {
        $newContent += $line
    }
}

Set-Content $file $newContent
