# Task Completion Checklist

## Before Committing Changes

### 1. Validate JSON Syntax
- Ensure all modified JSON files have valid JSON syntax
- Run: `python3 -m json.tool <file.json>` to check individual files
- Fix any JSON syntax errors

### 2. Format JSON Files (Optional but Recommended)
- Run `python3 prettify.py` to format all JSON files consistently
- Or run `python3 minify.py` if minified format is preferred
- **Note**: Only format if you've made changes that require it, or if explicitly requested

### 3. Verify Schema Structure
- Ensure JSON-LD structure is correct
- Verify `@context` is set to `"https://schema.org"`
- Check that `@id` references are valid
- Ensure Schema.org types are used correctly

### 4. Check File Naming
- Verify filename follows convention: `<directory>_<page>.json`
- Ensure filename maps correctly to URL path

### 5. Git Workflow
- Review changes with `git status` and `git diff`
- Stage only relevant files: `git add <files>`
- Write descriptive commit message
- Push changes: `git push`

## Schema-Specific Checks

### For New Schema Files
- Verify the schema corresponds to the correct page URL
- Check that all required Schema.org properties are included
- Ensure references to other entities (via `@id`) are correct
- Validate with Google Rich Data Validator (optional, but recommended for new schemas)

### For Modified Schema Files
- Ensure changes don't break existing references
- Verify all `@id` references still resolve correctly
- Check that the schema still validates as JSON-LD

## Testing
- No automated tests exist for this project
- Manual validation through:
  - JSON syntax validation
  - Google Rich Data Validator (for Schema.org compliance)
  - Visual inspection of JSON structure

## Notes
- This is a data repository, not a codebase with tests
- Focus on data correctness and JSON-LD validity
- Schema validation warnings (yellow) in Google validator are acceptable