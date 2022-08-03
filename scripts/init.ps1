If (Get-Command "node" -errorAction SlientlyContinue) {
  Write-Output "Node.js is installed"
} else {
  Write-Output "Node.js is not installed"
}

If (Get-Command "python" -errorAction SilentlyContinue
-Or Get-Command "python3" -errorAction SilentlyContinue
-Or Get-Command "py" -errorAction SilentlyContinue) {
  Write-Output "Python is installed"
} else {
  Write-Output "Python is not installed"
}

Set-Location ..

npm install

concurrently "npm --prefix ./app install" "cd server && pip install -r requirements.txt"

Write-Output "Setup complete"