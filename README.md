# Route4Me Schema

This repository contains structured data for Route4Me pages.

## Available Schema Definitions

Each JSON file in this repository corresponds to a page on Route4Me's website https://route4me.com. The schema definitions help search engines better understand and display our content.

### Pages

| Page URL | Schema File |
|----------|-------------|
| [/](https://route4me.com/) | [`homepage.json`](./homepage.json) |
| [/contact/](https://route4me.com/contact/) | [`contact.json`](./contact.json) |
| [/mobile/route-planner-app/](https://route4me.com/mobile/route-planner-app/) | [`mobile_route-planner-app.json`](./mobile_route-planner-app.json) |
| [/platform/android-mobile-routing-app/](https://route4me.com/platform/android-mobile-routing-app/) | [`platform_android-mobile-routing-app.json`](./platform_android-mobile-routing-app.json) |
| [/platform/ios-mobile-routing-app/](https://route4me.com/platform/ios-mobile-routing-app/) | [`platform_ios-mobile-routing-app.json`](./platform_ios-mobile-routing-app.json) |
| [/platform/business-analytics/](https://route4me.com/platform/business-analytics/) | [`platform_business-analytics.json`](./platform_business-analytics.json) |
| [/platform/business-operations/](https://route4me.com/platform/business-operations/) | [`platform_business-operations.json`](./platform_business-operations.json) |
| [/platform/customer-experience/](https://route4me.com/platform/customer-experience/) | [`platform_customer-experience.json`](./platform_customer-experience.json) |
| [/platform/dispatch-and-tracking-software/](https://route4me.com/platform/dispatch-and-tracking-software/) | [`platform_dispatch-and-tracking-software.json`](./platform_dispatch-and-tracking-software.json) |
| [/platform/driver-efficiency/](https://route4me.com/platform/driver-efficiency/) | [`platform_driver-efficiency.json`](./platform_driver-efficiency.json) |
| [/platform/integrations/](https://route4me.com/platform/integrations/) | [`platform_integrations.json`](./platform_integrations.json) |
| [/platform/marketplace/](https://route4me.com/platform/marketplace/) | [`platform_marketplace.json`](./platform_marketplace.json) |
| [/platform/marketplace_pricing/](https://route4me.com/platform/marketplace_pricing/) | [`platform_marketplace_pricing.json`](./platform_marketplace_pricing.json) |
| [/platform/mobile-routing-apps/](https://route4me.com/platform/mobile-routing-apps/) | [`platform_mobile-routing-apps.json`](./platform_mobile-routing-apps.json) |
| [/platform/premium-support/](https://route4me.com/platform/premium-support/) | [`platform_premium-support.json`](./platform_premium-support.json) |
| [/platform/professional-services/](https://route4me.com/platform/professional-services/) | [`platform_professional-services.json`](./platform_professional-services.json) |
| [/platform/route-optimization-software/](https://route4me.com/platform/route-optimization-software/) | [`platform_route-optimization-software.json`](./platform_route-optimization-software.json) |
| [/platform/route-planning-software/](https://route4me.com/platform/route-planning-software/) | [`platform_route-planning-software.json`](./platform_route-planning-software.json) |
| [/platform/zebra-mobile-routing-app/](https://route4me.com/platform/zebra-mobile-routing-app/) | [`platform_zebra-mobile-routing-app.json`](./platform_zebra-mobile-routing-app.json) |
| [/solutions/big-and-bulky-delivery-route-optimization/](https://route4me.com/solutions/big-and-bulky-delivery-route-optimization/) | [`solutions_big-and-bulky-delivery-route-optimization.json`](./solutions_big-and-bulky-delivery-route-optimization.json) |
| [/solutions/business-services-route-optimization-software/](https://route4me.com/solutions/business-services-route-optimization-software/) | [`solutions_business-services-route-optimization-software.json`](./solutions_business-services-route-optimization-software.json) |
| [/solutions/deploy-now/](https://route4me.com/solutions/deploy-now/) | [`solutions_deploy-now.json`](./solutions_deploy-now.json) |
| [/solutions/facility-and-property-services-routing-software/](https://route4me.com/solutions/facility-and-property-services-routing-software/) | [`solutions_facility-and-property-services-routing-software.json`](./solutions_facility-and-property-services-routing-software.json) |
| [/solutions/food-and-beverage-routing-software/](https://route4me.com/solutions/food-and-beverage-routing-software/) | [`solutions_food-and-beverage-routing-software.json`](./solutions_food-and-beverage-routing-software.json) |
| [/solutions/government-services-route-optimization-software/](https://route4me.com/solutions/government-services-route-optimization-software/) | [`solutions_government-services-route-optimization-software.json`](./solutions_government-services-route-optimization-software.json) |
| [/solutions/grow-your-business/](https://route4me.com/solutions/grow-your-business/) | [`solutions_grow-your-business.json`](./solutions_grow-your-business.json) |
| [/solutions/increase-efficiency/](https://route4me.com/solutions/increase-efficiency/) | [`solutions_increase-efficiency.json`](./solutions_increase-efficiency.json) |
| [/solutions/oil-and-gas-route-optimization/](https://route4me.com/solutions/oil-and-gas-route-optimization/) | [`solutions_oil-and-gas-route-optimization.json`](./solutions_oil-and-gas-route-optimization.json) |
| [/solutions/parcel-delivery-and-courier-routing/](https://route4me.com/solutions/parcel-delivery-and-courier-routing/) | [`solutions_parcel-delivery-and-courier-routing.json`](./solutions_parcel-delivery-and-courier-routing.json) |
| [/solutions/rx-delivery-and-healthcare-services-route-optimization/](https://route4me.com/solutions/rx-delivery-and-healthcare-services-route-optimization/) | [`solutions_rx-delivery-and-healthcare-services-route-optimization.json`](./solutions_rx-delivery-and-healthcare-services-route-optimization.json) |
| [/solutions/utilities-services-route-optimization/](https://route4me.com/solutions/utilities-services-route-optimization/) | [`solutions_utilities-services-route-optimization.json`](./solutions_utilities-services-route-optimization.json) |
| [/solutions/waste-management-route-planning-software/](https://route4me.com/solutions/waste-management-route-planning-software/) | [`solutions_waste-management-route-planning-software.json`](./solutions_waste-management-route-planning-software.json) |

## File Structure

- Each JSON file contains Schema.org definitions in JSON-LD format
- Filenames follow the pattern: `<website_directory-name>_<website_page-name>.json`
- The directory and page names in the filename maps directly to the URL path

For example:
- `platform_premium-support.json` → https://route4me.com/platform/premium-support/
- `solutions_waste-management-route-planning-software.json` → https://route4me.com/solutions/waste-management-route-planning-software/

## Schema Markup Update (Current Release)

1. **Remove Existing Schema**
   - Remove all schema markup from every route4me.com page
   - Ensure complete removal with no remnants left behind

2. **Add New Schema**
   - Only add new schema to pages with assigned schema files:
   ```html
   <script type="application/ld+json">
   New structured data
   </script>
   ```
   - Pages without an assigned schema file must be schema-free - no schema markup at all

3. **Final Verification**
   - Confirm old schema is completely removed from all pages
   - Verify new schema is only present on designated pages
   - Double-check that pages without assigned schema files remain schema-free

Note: The schema is 100% valid. Don't worry about few yellow (warning) messages in the Google rich data validator - these are bad suggestions, not errors that need fixing.

## Licenses

Copyright © Route4Me, Inc. All rights reserved. 