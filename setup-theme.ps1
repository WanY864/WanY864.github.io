$ErrorActionPreference = "Stop"

Write-Host "Checking Hugo and Git..."

if (-not (Get-Command hugo -ErrorAction SilentlyContinue)) {
    throw "Hugo was not found in PATH. Install Hugo Extended and reopen PowerShell."
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git was not found in PATH. Install Git and reopen PowerShell."
}

$ThemeDir = Join-Path $PSScriptRoot "themes\blowfish"

# Remove a broken or incomplete previous theme installation.
if (Test-Path $ThemeDir) {
    $LooksValid = (Test-Path (Join-Path $ThemeDir "theme.toml")) -or `
                  (Test-Path (Join-Path $ThemeDir "hugo.toml")) -or `
                  (Test-Path (Join-Path $ThemeDir "layouts"))

    if (-not $LooksValid) {
        Write-Host "Removing incomplete Blowfish theme directory..."
        Remove-Item -Recurse -Force $ThemeDir
    }
}

if (-not (Test-Path $ThemeDir)) {
    Write-Host "Downloading Blowfish theme..."
    New-Item -ItemType Directory -Force -Path (Split-Path $ThemeDir) | Out-Null

    git clone --depth 1 https://github.com/nunocoracao/blowfish.git $ThemeDir

    if ($LASTEXITCODE -ne 0) {
        if (Test-Path $ThemeDir) {
            Remove-Item -Recurse -Force $ThemeDir -ErrorAction SilentlyContinue
        }
        throw "Failed to download Blowfish from GitHub. Check your network connection and run setup-theme.ps1 again."
    }

    # Vendor the theme as normal files instead of using a Git submodule.
    # This avoids .gitmodules/submodule problems when the site is later pushed to GitHub Pages.
    $NestedGit = Join-Path $ThemeDir ".git"
    if (Test-Path $NestedGit) {
        Remove-Item -Recurse -Force $NestedGit
    }
}
else {
    Write-Host "Blowfish is already installed."
}

Write-Host ""
Write-Host "Theme setup complete."
Write-Host "Start the local preview with:"
Write-Host "  hugo server -D"
Write-Host "Then open:"
Write-Host "  http://localhost:1313/"
