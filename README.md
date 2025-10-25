# Scripts Collection / Набор скриптов

## English

### Repository
GitHub name: `python-scripts-toolkit`

### Setup
1. Run the automated installer (creates venv, upgrades pip, installs requirements):
   ```bash
   chmod +x scripts/install.sh
   ./scripts/install.sh
   ```
2. Manual alternative (if you prefer to perform the steps yourself):
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv python3-dev build-essential
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   [ -f requirements.txt ] && pip install -r requirements.txt
   ```

All provided scripts use only the Python standard library.

### Scripts (located in `scripts/`)
- `envinfo.py` – print interpreter path, Python version, and platform.
- `reqcheck.py` – show packages from `requirements.txt` that are missing.
- `logtail.py` – tail a log file and highlight new lines containing “error”.
- `backup.py` – archive a directory into ZIP/TAR formats.
- `httpcode.py` – send HEAD requests and display HTTP status codes.
- `jsonfmt.py` – pretty-print JSON from a file or stdin.
- `csvstats.py` – compute sum/count/average for numeric CSV columns.
- `filehash.py` – calculate SHA256 checksum of a file.
- `portscan.py` – test whether specific TCP ports are open.
- `passgen.py` – generate a random password of configurable length.

#### Running the scripts
Activate the virtual environment (if created), then switch into the Python scripts folder:
```bash
source .venv/bin/activate  # optional
cd scripts
python <script_name>.py
```
Replace the filename with any other script to invoke it.

### Shell scripts (located in `shell_scripts/`)
- `update_system.sh` – update/upgrade APT packages.
- `backup_home.sh` – create a timestamped tar.gz backup (default: $HOME).
- `disk_usage.sh` – show disk usage summary via df -h.
- `memory_usage.sh` – display RAM statistics from free -h.
- `network_test.sh` – ping a host (default 8.8.8.8).
- `cleanup_logs.sh` – delete *.log files older than N days.
- `system_info.sh` – print kernel and distribution info.
- `process_monitor.sh` – report whether a process is running.
- `find_large_files.sh` – list files larger than a given size.
- `uptime_report.sh` – show uptime and current users.

Run the desired script:
```bash
./<name>.sh
```

### Shell scripts for Arch Linux (located in `shell_scripts_arch/`)
- `update_system.sh` – system update via pacman -Syu.
- `backup_home.sh` – create a timestamped tar.gz backup (default: $HOME).
- `disk_usage.sh` – show disk usage summary via df -h.
- `memory_usage.sh` – display RAM statistics from free -h.
- `network_test.sh` – ping a host (default 8.8.8.8).
- `cleanup_logs.sh` – delete *.log files older than N days.
- `system_info.sh` – print kernel and distribution info.
- `process_monitor.sh` – report whether a process is running.
- `find_large_files.sh` – list files larger than a given size.
- `uptime_report.sh` – show uptime and current users.

Run from that directory:
```bash
cd shell_scripts_arch
./<name>.sh
```

### Shell scripts for Fedora (located in `shell_scripts_fedora/`)
- `update_system.sh` – system upgrade via dnf --refresh.
- `backup_home.sh` – create a timestamped tar.gz backup (default: $HOME).
- `disk_usage.sh` – show disk usage summary via df -h.
- `memory_usage.sh` – display RAM statistics from free -h.
- `network_test.sh` – ping a host (default 8.8.8.8).
- `cleanup_logs.sh` – delete *.log files older than N days.
- `system_info.sh` – print kernel and distribution info.
- `process_monitor.sh` – report whether a process is running.
- `find_large_files.sh` – list files larger than a given size.
- `uptime_report.sh` – show uptime and current users.

Run from that directory:
```bash
cd shell_scripts_fedora
./<name>.sh
```

### Project structure
```text
scripts/               # Python utilities
shell_scripts/         # Debian/Ubuntu shell scripts
shell_scripts_arch/    # Arch Linux shell scripts
shell_scripts_fedora/  # Fedora shell scripts
.gitignore             # Git ignore rules
LICENSE                # MIT license
README.md              # Documentation
CODE_OF_CONDUCT.md     # Contributor guidelines
SECURITY.md            # Vulnerability reporting
```

### Examples
```bash
# Python: generate a password
cd scripts
python passgen.py --length 24 --symbols

# Debian/Ubuntu shell script: update system
cd ../shell_scripts
./update_system.sh

# Arch shell script: check disk usage
cd ../shell_scripts_arch
./disk_usage.sh

# Fedora shell script: find large files in /var
cd ../shell_scripts_fedora
./find_large_files.sh /var 500M
```

## Русский

### Репозиторий
имя на GitHub: `python-scripts-toolkit`

### Установка
1. Запустите автоматический скрипт (создаёт venv, обновляет pip, ставит зависимости):
   ```bash
   chmod +x scripts/install.sh
   ./scripts/install.sh
   ```
2. Если хотите выполнить шаги вручную:
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv python3-dev build-essential
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   [ -f requirements.txt ] && pip install -r requirements.txt
   ```

Все скрипты используют только стандартную библиотеку Python.

### Скрипты (находятся в `scripts/`)
- `envinfo.py` – вывод интерпретатора, версии Python и платформы.
- `reqcheck.py` – проверка отсутствующих пакетов из `requirements.txt`.
- `logtail.py` – просмотр лога с подсветкой строк, содержащих «error».
- `backup.py` – архивирование каталога в ZIP/TAR.
- `httpcode.py` – проверка HTTP-статусов запросами HEAD.
- `jsonfmt.py` – форматирование JSON из файла или stdin.
- `csvstats.py` – подсчёт суммы/количества/среднего по числовым столбцам CSV.
- `filehash.py` – вычисление SHA256-хеша файла.
- `portscan.py` – проверка открытости TCP-портов.
- `passgen.py` – генерация случайного пароля заданной длины.

#### Запуск скриптов
Активируйте виртуальное окружение (если оно создано), затем перейдите в каталог со скриптами на Python:
```bash
source .venv/bin/activate  # по желанию
cd scripts
python <название_скрипта>.py
```
Можно заменить имя файла на любой другой скрипт из набора.

### Shell-скрипты (находятся в `shell_scripts/`)
- `update_system.sh` – обновление и апгрейд пакетов APT.
- `backup_home.sh` – создание архивного бэкапа (по умолчанию $HOME).
- `disk_usage.sh` – сводка использования дисков через df -h.
- `memory_usage.sh` – отображение статистики памяти из free -h.
- `network_test.sh` – проверка сети пингом (по умолчанию 8.8.8.8).
- `cleanup_logs.sh` – удаление *.log файлов старше N дней.
- `system_info.sh` – информация о ядре и дистрибутиве.
- `process_monitor.sh` – проверка, запущен ли процесс.
- `find_large_files.sh` – поиск файлов больше заданного размера.
- `uptime_report.sh` – вывод uptime и списка пользователей.

Запускайте нужный скрипт:
```bash
./<имя>.sh
```

### Shell-скрипты для Arch Linux (находятся в `shell_scripts_arch/`)
- `update_system.sh` – обновление системы через pacman -Syu.
- `backup_home.sh` – создание архивного бэкапа (по умолчанию $HOME).
- `disk_usage.sh` – сводка использования дисков через df -h.
- `memory_usage.sh` – отображение статистики памяти из free -h.
- `network_test.sh` – проверка сети пингом (по умолчанию 8.8.8.8).
- `cleanup_logs.sh` – удаление *.log файлов старше N дней.
- `system_info.sh` – информация о ядре и дистрибутиве.
- `process_monitor.sh` – проверка, запущен ли процесс.
- `find_large_files.sh` – поиск файлов больше заданного размера.
- `uptime_report.sh` – вывод uptime и списка пользователей.

Запускайте из этого каталога:
```bash
cd shell_scripts_arch
./<имя>.sh
```

### Shell-скрипты для Fedora (находятся в `shell_scripts_fedora/`)
- `update_system.sh` – обновление системы через dnf --refresh.
- `backup_home.sh` – создание архивного бэкапа (по умолчанию $HOME).
- `disk_usage.sh` – сводка использования дисков через df -h.
- `memory_usage.sh` – отображение статистики памяти из free -h.
- `network_test.sh` – проверка сети пингом (по умолчанию 8.8.8.8).
- `cleanup_logs.sh` – удаление *.log файлов старше N дней.
- `system_info.sh` – информация о ядре и дистрибутиве.
- `process_monitor.sh` – проверка, запущен ли процесс.
- `find_large_files.sh` – поиск файлов больше заданного размера.
- `uptime_report.sh` – вывод uptime и списка пользователей.

Запускайте из этого каталога:
```bash
cd shell_scripts_fedora
./<имя>.sh
```

### Структура проекта
```text
scripts/               # Скрипты на Python
shell_scripts/         # Shell-скрипты для Debian/Ubuntu
shell_scripts_arch/    # Shell-скрипты для Arch Linux
shell_scripts_fedora/  # Shell-скрипты для Fedora
.gitignore             # Правила исключений Git
LICENSE                # Лицензия MIT
README.md              # Документация
CODE_OF_CONDUCT.md     # Правила поведения
SECURITY.md            # Политика безопасности
```

### Примеры
```bash
# Python: генерация пароля
cd scripts
python passgen.py --length 24 --symbols

# Debian/Ubuntu: обновление системы
cd ../shell_scripts
./update_system.sh

# Arch: проверка дискового пространства
cd ../shell_scripts_arch
./disk_usage.sh

# Fedora: поиск крупных файлов в /var
cd ../shell_scripts_fedora
./find_large_files.sh /var 500M
```
