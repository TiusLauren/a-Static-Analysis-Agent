# 🔍 Static Analysis Agent

AI-powered static code analysis tool that scans your codebase for security vulnerabilities, code quality issues, style violations, and complexity metrics.

## Features

- 🔒 **Security Scanning** - Detect vulnerabilities with Bandit
- ✨ **Code Quality** - Analyze code quality with Pylint
- 🎨 **Style Checking** - Enforce PEP8 with Flake8
- 📊 **Complexity Metrics** - Measure cyclomatic complexity with Radon
- 📝 **Rich Reports** - Beautiful terminal output + JSON export

## Installation

```bash
# Clone the repository
git clone https://github.com/TiusLauren/a-Static-Analysis-Agent.git
cd a-Static-Analysis-Agent

# Install dependencies
pip install -r requirements.txt

# Install the tool
pip install -e .
```

## Usage

### Basic scan
```bash
analyze /path/to/your/code
```

### Security scan only
```bash
analyze /path/to/your/code --security-only
```

### Save report to JSON
```bash
analyze /path/to/your/code --output report.json
```

### Scan options
```bash
analyze --help
```

## Example Output

```
🔍 Static Analysis Report

╭─────────── 🔒 Security ────────────╮
│ Security Issues: 3                 │
│ High Severity: 1                   │
╰────────────────────────────────────╯

╭─────────── ✨ Code Quality ────────╮
│ Errors: 5                          │
│ Warnings: 12                       │
╰────────────────────────────────────╯
```

## Development

```bash
# Run tests
pytest

# Lint the codebase
pylint src/
```

## License

MIT
