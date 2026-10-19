# Cork City Hotel — Booking Application
**Full-stack coursework case study · Node.js · Express · EJS · MySQL**

A hotel booking prototype I built during my computing studies. The application connects a server-rendered booking flow to a MySQL room table, with supporting HTML/CSS/JavaScript pages.

## The problem

A visitor needs to browse available room categories, select dates and room quantities, and understand an estimated booking total.

## How I approached it

```text
Room selection / date input
             ↓
Express application + EJS views
             ↓
MySQL room catalogue
             ↓
Booking state + cost calculation
             ↓
Demo login → confirmation page
```

### Features in the coursework

- A server-rendered hotel website with room information.
- A MySQL-backed room catalogue and selectable room types.
- Date, quantity and total-cost handling across the booking journey.
- A session-backed confirmation flow and example login.
- A separate date/time and optional weather-information page.

### Technologies

Node.js, Express, EJS templates, MySQL, HTML, CSS and JavaScript. The original application also integrated an external weather API.

## What I'd improve for production

This was designed as **coursework**, not a deployed hotel product. I would strengthen input validation, date and availability rules, account security, session configuration, error handling, automated tests and dependency maintenance. A real booking platform would additionally need payment handling and transactional inventory management.

## Current source and verification

The [sanitized public source](https://github.com/benjanning/cork-city-hotel) now includes a local synthetic-data demonstration. Photographs, API credentials and SQL exports were excluded. The original EJS booking flow was retained; dates and quantities are validated server-side. The local flow was exercised through confirmation. Optional MySQL integration remains unverified.

[Read the illustrated case study](https://benjanning.github.io/projects/projects/hotel-booking/) · [Return to portfolio](../../README.md)
