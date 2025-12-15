# Code Style and Conventions

## JSON-LD Format Standards

### Structure
- All JSON files must be valid JSON-LD (JSON for Linked Data)
- Use Schema.org vocabulary (`@context: "https://schema.org"`)
- Files typically use `@graph` array to contain multiple schema entities
- Use `@id` to reference entities within the graph

### Formatting
- Use 4-space indentation (when prettified)
- No trailing commas
- Use double quotes for all strings
- Follow JSON-LD best practices for linked data

### Schema Types
Common Schema.org types used:
- `Corporation` - For Route4Me company information
- `WebSite` - For website metadata
- `WebPage`, `CollectionPage`, `ItemPage` - For page types
- `BreadcrumbList` - For navigation breadcrumbs
- `Organization`, `Person` - For organizational data
- `ContactPoint` - For contact information

### File Organization
- Each page gets its own JSON file
- Filename maps directly to URL path structure
- Use `ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json` for pages without dedicated schema files

### Naming Conventions
- Filenames: lowercase with hyphens: `directory-name_page-name.json`
- URL paths in schema: match actual Route4Me URLs exactly
- `@id` values: use full URLs with fragment identifiers (e.g., `https://route4me.com/#corporation`)

### Validation Notes
- Schema must be 100% valid
- Yellow warnings in Google Rich Data Validator are acceptable (they are bad suggestions, not errors)
- Always validate JSON syntax before committing

## Python Scripts

### Style
- Use Python 3
- Follow PEP 8 style guide
- Use descriptive function names
- Include error handling with try/except blocks
- Print informative messages for user feedback

### Scripts
- `minify.py`: Minifies JSON by removing whitespace
- `prettify.py`: Formats JSON with 4-space indentation