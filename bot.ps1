# Определите корневую папку проекта
$projectRoot = "."

# Список папок для создания
$folders = @(
    "$projectRoot/callbacks",
    "$projectRoot/handlers",
    "$projectRoot/keyboards",
    "$projectRoot/utils",
    "$projectRoot/models",
    "$projectRoot/middlewares"
)

# Создание папок
foreach ($folder in $folders) {
    New-Item -Path $folder -ItemType Directory
}

# Список файлов для создания
$files = @(
    "$projectRoot/bot.py",
    "$projectRoot/callbacks/__init__.py",
    "$projectRoot/handlers/__init__.py",
    "$projectRoot/handlers/start.py",
    "$projectRoot/keyboards/__init__.py",
    "$projectRoot/keyboards/inline_keyboards.py",
    "$projectRoot/keyboards/reply_keyboards.py",
    "$projectRoot/utils/__init__.py",
    "$projectRoot/utils/helpers.py",
    "$projectRoot/models/__init__.py",
    "$projectRoot/models/user_model.py",
    "$projectRoot/middlewares/__init__.py",
    "$projectRoot/middlewares/logging_middleware.py",
    "$projectRoot/config.py",
    "$projectRoot/.env",
    "$projectRoot/.gitignore",
    "$projectRoot/requirements.txt"
)

# Создание файлов
foreach ($file in $files) {
    New-Item -Path $file -ItemType File
}

# Создание и активация виртуальной среды
$venvPath = "$projectRoot/venv"
if (-Not (Test-Path $venvPath)) {
    python -m venv $venvPath
}
& "$venvPath/Scripts/Activate.ps1"

Write-Host "Project structure for the Telegram bot has been successfully created."
Write-Host "The virtual environment has been created and activated."
