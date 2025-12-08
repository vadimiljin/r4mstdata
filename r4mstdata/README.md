# Route4Me Schema v1.1

This repository contains structured data for Route4Me pages.

## Available Schema Definitions

Each JSON file in this repository corresponds to a page on Route4Me's website https://route4me.com.

## File Structure

- Each JSON file contains Schema.org definitions in JSON-LD format
- Filenames follow the pattern: `<website_directory-name>_<website_page-name>.json`
- The directory and page names in the filename maps directly to the URL path

For example:
- `platform_premium-support.json` → https://route4me.com/platform/premium-support/
- `solutions_waste-management-route-planning-software.json` → https://route4me.com/solutions/waste-management-route-planning-software/

## Schema Markup Update (Current Release)

- Only add new schema to pages with assigned schema files:
   ```html
   <script type="application/ld+json">
   New structured data
   </script>
   ```
- If there is no schema file for the page, use `ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json`

Note: The schema is 100% valid. Don't worry about few yellow (warning) messages in the Google rich data validator - these are bad suggestions, not errors that need fixing.

## Licenses

Copyright © Route4Me, Inc. All rights reserved. 