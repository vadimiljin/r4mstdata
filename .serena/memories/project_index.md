# Route4Me Schema Project Index

## Project Statistics
- **Total JSON Schema Files**: 440 files
- **r4mstdata/**: 109 files (main Route4Me pages)
- **integrations_telematics_partners/**: 314 files (telematics vendor schemas)
- **partner-contact/**: 17 files (partner contact pages)
- **Python Scripts**: 2 (minify.py, prettify.py)

## Directory Structure

### Root Level Files
- `README.md` - Project documentation
- `jira.md` - Jira ticket references and workflow notes
- `minify.py` - JSON minification utility
- `prettify.py` - JSON formatting utility

### r4mstdata/ (109 files)
Main schema files for Route4Me public pages. Files follow pattern: `<directory>_<page>.json`

**Key Categories:**
- **Homepage & Core Pages**: `homepage.json`, `about.json`, `contact.json`, `livechat.json`
- **Platform Pages**: `platform_*.json` (route-optimization-software, integrations, mobile-routing-apps, etc.)
- **Solutions Pages**: `solutions_*.json` (waste-management, food-and-beverage, parcel-delivery, etc.)
- **Marketplace Pages**: `platform_marketplace_*.json` (route-optimization, operations, mobile, e-commerce, etc.)
- **Special Pages**: `ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json`, `route-optimization-roi.json`, `partner-program.json`

**Notable Subdirectories in Filenames:**
- `platform_marketplace_route-optimization_*` - Route optimization features
- `platform_marketplace_operations_*` - Operations management features
- `platform_marketplace_labs_*` - Experimental/lab features
- `platform_marketplace_notifications-and-alerts_*` - Notification features
- `platform_marketplace_data_*` - Data export/import features
- `platform_marketplace_telematics_*` - Telematics features
- `platform_marketplace_mobile_*` - Mobile app features

### integrations_telematics_partners/ (314 files)
Schema files for individual telematics vendor/partner pages. Files follow pattern: `integrations_telematics_partners_<vendor-name>.json`

**Notable Vendors Include:**
- Major providers: `samsara.json`, `geotab.json`, `verizonconnect.json`, `motive.json`, `fleetcomplete.json`
- Regional providers: Various country/region-specific vendors
- Specialized providers: GPS tracking, fleet management, vehicle diagnostics

**Special File:**
- `integrations_telematics_partners.json` - Main collection page schema for the vendors directory

### partner-contact/ (17 files)
Schema files for partner contact pages. Files follow pattern: `partner-contact_<partner-name>.json`

**Partners Include:**
- `eaglewireless.json`, `eteria.json`, `etrucks.json`, `geolocstar.json`, `geotab.json`
- `groscale.json`, `linxup.json`, `maramoja.json`, `motive.json`, `netradyne.json`
- `northone.json`, `samsara.json`, `telematics.json`, `teletracnavman.json`
- `verizonconnect.json`, `xplorspot.json`, `zubie.json`

## File Naming Patterns

### URL Mapping
Filenames map directly to URL paths on route4me.com:
- `platform_premium-support.json` → `https://route4me.com/platform/premium-support/`
- `solutions_waste-management-route-planning-software.json` → `https://route4me.com/solutions/waste-management-route-planning-software/`
- `integrations_telematics_partners_geotab.json` → `https://route4me.com/integrations/telematics/partners/geotab/`
- `partner-contact_samsara.json` → `https://route4me.com/partner-contact/samsara/`

### Naming Conventions
- Use lowercase letters
- Use hyphens (`-`) to separate words
- Use underscores (`_`) to separate directory/page segments
- No spaces in filenames
- Always ends with `.json`

## Schema Structure Patterns

### Common Schema Types
All files use JSON-LD format with `@context: "https://schema.org"`

**Typical Structure:**
```json
{
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebPage" | "CollectionPage" | "ItemPage",
            "@id": "https://route4me.com/path/#identifier",
            ...
        },
        {
            "@type": "BreadcrumbList",
            ...
        },
        {
            "@type": "Organization" | "Corporation",
            "@id": "https://route4me.com/#corporation",
            ...
        }
    ]
}
```

### Common Entities Referenced
- `https://route4me.com/#corporation` - Route4Me Corporation entity
- `https://route4me.com/#website` - Route4Me Website entity
- `https://route4me.com/platform/route-optimization-software/#softwareapplication` - Main software product

## Special Files

### ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json
Default schema template for pages that don't have dedicated schema files. Contains:
- Corporation information
- Website metadata
- Breadcrumb structure
- Common organizational data

### Collection Pages
- `integrations_telematics_partners.json` - Main vendors directory page
- `integrations.json` - Main integrations page
- `integrations_telematics.json` - Telematics integrations page
- `platform_marketplace.json` - Marketplace overview page

## Utility Scripts

### minify.py
- Minifies all JSON files in the repository
- Removes whitespace and formatting
- Preserves JSON structure and validity
- Usage: `python3 minify.py`

### prettify.py
- Formats all JSON files with 4-space indentation
- Improves readability
- Preserves JSON structure and validity
- Usage: `python3 prettify.py`

## Search Patterns

### Finding Files by URL Path
To find a schema file for a specific URL:
1. Convert URL path to filename format
2. Replace `/` with `_`
3. Remove leading/trailing slashes
4. Add `.json` extension

Example: `https://route4me.com/platform/premium-support/`
→ `platform_premium-support.json`

### Finding Files by Category
- **Platform features**: `grep -r "platform_" r4mstdata/`
- **Solutions**: `grep -r "solutions_" r4mstdata/`
- **Telematics vendors**: `ls integrations_telematics_partners/`
- **Partner contacts**: `ls partner-contact/`

## Maintenance Notes

### File Organization
- Files are organized by directory matching website structure
- Each page type has its own directory or naming pattern
- Special files (like `ANY_PAGE_WITHOUT_SPECIFIC_SCHEMA.json`) are in `r4mstdata/`

### Validation
- All schemas must be valid JSON-LD
- All schemas must use Schema.org vocabulary
- Yellow warnings in Google Rich Data Validator are acceptable
- JSON syntax must be valid (use `python3 -m json.tool` to validate)