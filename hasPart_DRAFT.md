# hasPart draft


 **Часть 1**, охватывающая **Стратегическое планирование и Интеллектуальный анализ** (Strategic Planning & Intelligence). Эти функции сфокусированы на анализе данных до того, как маршруты будут выполнены.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Route4Me Enterprise Solutions - Strategic Module",
  "hasPart": [
    {
      "@type": "SoftwareApplication",
      "name": "AI-Powered Strategic Optimization",
      "description": "Generates complex routing scenarios using natural language prompts. Allows logistics managers to simulate 'what-if' constraints for mixed fleets and varying service times without manual configuration.",
      "applicationCategory": "BusinessIntelligence",
      "featureList": "Natural Language Scenario Generation, Constraint Simulation, Automated Parameter Tuning"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Historical Pattern Analysis",
      "description": "Analyzes historical order and telematics data to predict optimal visit frequencies and service duration. Replaces static estimates with actual performance metrics derived from GPS logs and completed manifests.",
      "applicationCategory": "DataAnalysis",
      "featureList": "Visit Frequency Prediction, Service Time Analytics, Historical Data Ingestion"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Comparative Scenario Analytics",
      "description": "Side-by-side comparison of multiple routing scenarios. Visualizes variance in cost, distance, and time between 'Draft', 'Planned', and 'Actual' execution to identify the most profitable strategy before dispatch.",
      "applicationCategory": "AnalyticsApplication",
      "featureList": "Side-by-Side Comparison, Variance Reporting, Cost Impact Analysis"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Customer Location Intelligence (System of Record)",
      "description": "Centralized database for customer rules, time windows, and service types. Eliminates reliance on CSV uploads by maintaining a permanent 'System of Record' for all customer constraints and history.",
      "applicationCategory": "DatabaseManagement",
      "featureList": "Permanent Attribute Storage, Dynamic Constraint Inheritance, Multi-Service Type Support"
    }
  ]
}
```


 **Часть 2**, сфокусированная на **Операционном управлении и Исполнении** (Operational Execution & Field Management), (Dispatch, Mobile, Customer Portal)..

Этот блок описывает инструменты для диспетчеров и водителей, подчеркивая возможности работы в реальном времени и управления смешанными активами.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Route4Me Enterprise Solutions - Operational Module",
  "hasPart": [
    {
      "@type": "SoftwareApplication",
      "name": "Real-Time Dispatch Command Center",
      "description": "Centralized dashboard for drag-and-drop route assignment across multiple facilities. Features 'Auto-Assign' logic to instantly distribute unassigned routes to available drivers based on skills and capacity.",
      "applicationCategory": "LogisticsApplication",
      "featureList": "Multi-Facility Assignment, Drag-and-Drop Dispatch, Real-Time Route Health Monitoring, Driver Skill Matching"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Field Execution Mobile App",
      "description": "Driver workflow application supporting 'Scan-to-Load' verification and offline mode. Allows drivers to capture 'Proof of Visit' (signatures, photos) and manage inventory directly from the field with automatic sync upon reconnection.",
      "applicationCategory": "MobileApplication",
      "operatingSystem": "iOS, Android", 
      "featureList": "Barcode Scanning, Offline Mode, Commercial Navigation, Proof of Visit, Dynamic Order Insertion"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Unified Asset & Telematics Intelligence",
      "description": "Hardware-agnostic platform for tracking vehicles, trailers, and heavy equipment (Assets). Ingests live telemetry (GPS, fuel, odometer) to visualize 'Planned vs. Actual' paths and detect unauthorized usage.",
      "applicationCategory": "IoTApplication",
      "featureList": "Mixed Fleet Tracking, Odometer Sync, Fuel Monitoring, Asset Health Alerts"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Customer Experience Hub (Portal)",
      "description": "Self-service portal allowing end-customers to view their 'Visits' (not just Destinations) and request services. Includes automated notifications for ETA updates and service completion proofs.",
      "applicationCategory": "WebApplication",
      "featureList": "Self-Service Portal, Visit Request Management, Real-Time ETA Notifications, Brandable Interface"
    }
  ]
}
```

### Ключевые акценты (из источников):
1.  **Dispatch Center:** Упор на **Auto-Assign** и работу с **Facilities**,. Дэн критиковал отсутствие фильтров, поэтому здесь подчеркивается возможность управления ("Command Center").
2.  **Mobile App:** Акцент на **Offline Mode** и **Scan-to-Load**,. Это критические функции для полевой работы, на которых настаивал Дэн (чтобы приложение не было "бесполезным" без интернета).
3.  **Assets & Telematics:** Использование термина **Assets** (Активы) вместо просто "Vehicles",. Это позволяет продавать решение для трекинга генераторов, контейнеров и прицепов, а не только грузовиков.
4.  **Customer Hub:** Использование термина **"Visit"** вместо "Destination", так как это утвержденная Дэном ментальная модель для клиентов,.



 **Часть 3**, посвященная **Финансовому контролю и Администрированию** (Financial Control, Billing & Administration), (Billing, Invoicing, System of Record).

Этот модуль описывает функции, которые превращают операционные данные в финансовые документы («System of Record») и обеспечивают корпоративное управление.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Route4Me Enterprise Solutions - Financial & Admin Module",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, Windows, macOS, Linux, Android, iOS",
  "hasPart": [
    {
      "@type": "SoftwareApplication",
      "name": "Financial System of Record",
      "description": "Generates authoritative invoice drafts based on actual field execution. Automatically calculates 'Planned vs. Actual' revenue by comparing original orders against what was actually delivered or serviced by the driver.",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "Web, Windows, macOS, Linux, Android, iOS",
      "featureList": "Automated Invoice Generation, Revenue Recognition, Service Type Costing, Proof of Delivery Linkage"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Dynamic Price Management",
      "description": "Enterprise-grade pricing engine that supports customer-specific price lists and dynamic service rates. Calculates costs based on 'Man-Hours', service types (e.g., installation vs. inspection), and variable vehicle costs.",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web, Windows, macOS, Linux, Android, iOS",
      "featureList": "Customer-Specific Price Lists, Variable Service Rates, Man-Hour Costing, Multi-Currency Support"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Forensic Audit & Traceability",
      "description": "Complete data lineage tracking for compliance. Allows auditors to trace any executed route back to the specific optimization scenario or master route template that generated it, ensuring full operational accountability.",
      "applicationCategory": "SecurityApplication",
      "operatingSystem": "Web, Windows, macOS, Linux, Android, iOS",
      "featureList": "Route Lineage Tracking, Immutable Activity Logs, Scenario-to-Execution Audit, Change History"
    },
    {
      "@type": "SoftwareApplication",
      "name": "Enterprise Hierarchy & Retention",
      "description": "Advanced organizational management supporting multi-facility hierarchies and region-specific data visibility. Includes configurable data retention policies to manage storage costs and compliance requirements.",
      "applicationCategory": "ManagementApplication",
      "operatingSystem": "Web, Windows, macOS, Linux, Android, iOS",
      "featureList": "Multi-Facility Partitioning, Regional Hierarchy, Data Pruning Policies, Role-Based Access Control"
    }
  ]
}
```

### Ключевые акценты (из источников):

1.  **Financial System of Record:** Это ключевое позиционирование для Enterprise. Система не просто «маршрутизирует», она создает **финансовые документы** (Draft Invoices) на основе того, что реально произошло в поле (Scan-to-load, Proof of Visit),.
2.  **Man-Hours & Costing:** Важное отличие от конкурентов — учет **Man-Hours** (человеко-часов) отдельно от времени работы машины. Это критично для сервисных компаний (например, ландшафтный дизайн, ремонт), где стоимость зависит от бригады, а не только от пробега,.
3.  **Forensic Audit:** Дэн подчеркивал важность **Traceability** (прослеживаемости) — возможности понять, из какого именно стратегического сценария появился конкретный маршрут («no f*cking clue where it came from» — проблема, которую этот модуль решает),.
4.  **Hierarchy:** Поддержка **Multi-Facility** (множества складов/филиалов) — это то, что отличает Enterprise-решение от малого бизнеса. Глобальная фильтрация по Facility является приоритетом №1,.

Мы покрыли Стратегию, Операции и Финансы. Хотите, чтобы я сгенерировал **FAQ** для этих функций (например, «Как рассчитываются Man-Hours?» или «Чем отличается Planned vs Actual Revenue?»), чтобы использовать их как контент для Rich Snippets?