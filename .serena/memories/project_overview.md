# Route4Me Schema Production Repository

## Project Purpose
This repository contains structured data (JSON-LD format) for Schema.org definitions for Route4Me website pages (https://route4me.com). Each JSON file corresponds to a page on the Route4Me website and contains Schema.org definitions in JSON-LD format.

## Tech Stack
- **Language**: Python 3 (for utility scripts)
- **Data Format**: JSON-LD (JSON for Linked Data)
- **Schema Standard**: Schema.org
- **Dependencies**: None (uses Python standard library only)

## Directory Structure
- `r4mstdata/` - Main schema files for Route4Me public pages (109 files)
- `integrations_telematics_partners/` - Schema files for telematics partner/vendor pages (275 files)
- `partner-contact/` - Schema files for partner contact pages (15 files)
- `minify.py` - Utility script to minify all JSON files
- `prettify.py` - Utility script to prettify/format all JSON files
- `README.md` - Project documentation
- `jira.md` - Jira ticket references and workflow notes

## File Naming Convention
Filenames follow the pattern: `<website_directory-name>_<website_page-name>.json`

The directory and page names in the filename map directly to the URL path:
- `platform_premium-support.json` → https://route4me.com/platform/premium-support/
- `solutions_waste-management-route-planning-software.json` → https://route4me.com/solutions/waste-management-route-planning-software/

## Special Files
- `ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json` - Default schema to use for pages without assigned schema files

## Schema Validation
- Schema is 100% valid
- Yellow (warning) messages in Google Rich Data Validator are bad suggestions, not errors that need fixing