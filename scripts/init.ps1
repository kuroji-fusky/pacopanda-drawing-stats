function Check-Command($cmd) {
  If (![bool](Get-Command -Name $cmd -ErrorAction SilentlyContinue)) {
    return Write-Host  "Not Installed or missing: $cmd" -ForegroundColor Red
  } else {

  return Write-Host "Installed: $cmd" -ForegroundColor Green
  }
}

$env = @("node", "npm", "python", "python3", "pip", "pip3", "py")

foreach ($e in $env) {
  Check-Command -cmd $e
}