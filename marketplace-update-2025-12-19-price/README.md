# Marketplace Schema Update - Price Removal
**Дата:** 19 декабря 2025

## Описание изменений

Из схем marketplace модулей удалены все свойства, связанные с ценами (price, priceSpecification).

## Обработанные файлы (10)

1. `platform_marketplace_data_sftp-route-optimization.json` - удалено: priceSpecification ($0)
2. `platform_marketplace_mobile_voice-navigation.json` - удалено: priceSpecification ($20)
3. `platform_marketplace_notifications-and-alerts_notification-scheduled.json` - удалено: priceSpecification ($20)
4. `platform_marketplace_notifications-and-alerts_notification-you-are-next.json` - удалено: priceSpecification ($20)
5. `platform_marketplace_operations_audit-logging-and-activity-stream.json` - удалено: priceSpecification ($99)
6. `platform_marketplace_operations_workflows.json` - удалено: price/priceCurrency из Offer ($10)
7. `platform_marketplace_route-optimization_constraint-driver-skills.json` - удалено: priceSpecification ($10)
8. `platform_marketplace_route-optimization_curbside-delivery.json` - удалено: Offer price + priceSpecification ($500)
9. `platform_marketplace_route-optimization_recurring-route-optimization.json` - удалено: priceSpecification ($100)
10. `platform_marketplace_telematics_dynamic-geofencing.json` - удалено: priceSpecification ($5)

## Что было удалено

### PriceSpecification объекты
```json
"priceSpecification": {
    "@type": "PriceSpecification",
    "price": "...",
    "priceCurrency": "USD"
}
```

### Price поля в Offer объектах
```json
"price": "...",
"priceCurrency": "USD",
"priceValidUntil": "..."
```

## Не изменено

**`platform_marketplace_pricing.json`** - цены сохранены (мобильное приложение)

## Статистика

- Всего файлов marketplace: 63
- Файлов с ценами (до): 11
- Файлов с ценами (после): 1 (только pricing.json)
- Файлов обработано: 10

## Использование

Эти файлы готовы к развертыванию. Все изменения протестированы и проверены на корректность JSON структуры.
