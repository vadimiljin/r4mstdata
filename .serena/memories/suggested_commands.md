# Suggested Commands for Route4Me Schema Repository

## JSON Formatting Commands

### Prettify all JSON files
```bash
python3 prettify.py
```
Formats all JSON files in the repository with 4-space indentation for better readability.

### Minify all JSON files
```bash
python3 minify.py
```
Removes all whitespace from JSON files to minimize file size.

## Git Commands

### Check status
```bash
git status
```

### View changes
```bash
git diff
```

### Stage files
```bash
git add <file>
git add .  # Stage all changes
```

### Commit changes
```bash
git commit -m "Description of changes"
```

### Push changes
```bash
git push
```

## File Operations (Linux)

### List files
```bash
ls -la
ls -la <directory>
```

### Find JSON files
```bash
find . -name "*.json"
find <directory> -name "*.json"
```

### Search in files
```bash
grep -r "pattern" .
grep -r "pattern" <directory>
```

### Navigate directories
```bash
cd <directory>
cd ..  # Go up one level
cd ~   # Go to home directory
```

### View file contents
```bash
cat <file>
less <file>
head -n 20 <file>  # First 20 lines
tail -n 20 <file>  # Last 20 lines
```

## Python Commands

### Run Python scripts
```bash
python3 <script.py>
```

### Check Python version
```bash
python3 --version
```

## Validation

### Validate JSON syntax
```bash
python3 -m json.tool <file.json>
```

### Validate all JSON files (basic syntax check)
```bash
find . -name "*.json" -exec python3 -m json.tool {} \; > /dev/null
```