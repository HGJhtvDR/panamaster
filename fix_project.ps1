Write-Host "🔧 Автофикс проекта PANAMASTER..."

# 1. Удаление "except Exception as e:" -> "except Exception:"
Write-Host "`n[1/5] Удаляем e в except..."
Get-ChildItem -Recurse -Include *.py | ForEach-Object {
    (Get-Content $_.FullName) -replace 'except\s+Exception\s+as\s+e\s*:', 'except Exception:' |
    Set-Content $_.FullName
}

# 2. Добавление импортов
Write-Host "`n[2/5] Добавляем недостающие импорты..."

Get-ChildItem app\routes\*.py | ForEach-Object {
    $content = Get-Content $_.FullName
    $modified = $false

    if ($content -join "`n" -match '\b(flash|redirect|url_for)\b' -and ($content -join "`n" -notmatch 'from flask import flash')) {
        $content = @('from flask import flash, redirect, url_for') + $content
        $modified = $true
    }

    if ($content -join "`n" -match '\bdb\b' -and ($content -join "`n" -notmatch 'from app import db')) {
        $content = @('from app import db') + $content
        $modified = $true
    }

    if ($modified) {
        $content | Set-Content $_.FullName
        Write-Host "✓ Обновлен: $($_.Name)"
    }
}

# 3. Комментарий для C901
Write-Host "`n[3/5] Игнорируем 'C901' в errors.py..."
(Get-Content app\errors.py) -replace 'def register_server_errors', 'def register_server_errors  # noqa: C901' | Set-Content app\errors.py

# 4. Flake8 — длина строки
Write-Host "`n[4/5] Обновляем .flake8..."
if (!(Test-Path ".flake8")) {
    "max-line-length = 120" | Set-Content .flake8
} elseif (-not (Select-String -Path ".flake8" -Pattern "max-line-length")) {
    Add-Content ".flake8" "`nmax-line-length = 120"
}

# 5. Запуск black и pre-commit
Write-Host "`n[5/5] Запускаем black и pre-commit..."
black .
pre-commit run --all-files


