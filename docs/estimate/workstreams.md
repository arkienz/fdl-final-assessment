| Phase | Workstream | Hours low / likely / high | Depends on | Staff | Milestone |
|---|---|---|---|---|---|
| P0 | Access/ownership check, backup, baseline commit, dev/staging/prod split *(discovery)* | 16 / 24 / 40 | Owner grants access | Lead + TA | M0 gap analysis |
| P0 | Codebase inventory, feature classification, gap analysis vs master sheet *(discovery)* | 30 / 44 / 70 | Owner grants access | Lead + TA | M0 gap analysis |
| P0 | Start external applications: DAT, Truckstop, ELD partners, Intuit, Apple/Google (D-U-N-S), 10DLC *(discovery)* | 10 / 16 / 24 | Owner grants access | Lead + TA | M0 gap analysis |
| P1 | Prototype rework or partial rebuild (sized by the gap analysis; owner approval) | 0 / 120 / 400 | P0 gap analysis | Lead + TA | M1 foundations |
| P1 | Auth: reset, lockout, MFA for owner/admin, sessions | 30 / 45 / 70 | P0 gap analysis | Lead | M1 foundations |
| P1 | Tenant-scoping contract, DB row-level security, isolation test suite | 50 / 70 / 110 | P0 gap analysis | Lead | M1 foundations |
| P1 | Roles (Super Admin, Owner, Dispatcher, Driver, Helper, Read-only, Customer), teams/pods | 40 / 60 / 90 | P0 gap analysis | Lead + TA | M1 foundations |
| P1 | Cross-tenant FDL pod staff access (scoped grants, audited) | 40 / 60 / 100 | P0 gap analysis | Lead | M1 foundations |
| P1 | Company settings + user management: invite, deactivate, offboard | 30 / 50 / 80 | P0 gap analysis | Lead + TA | M1 foundations |
| P1 | Audit log framework (actor, action, before/after) | 24 / 36 / 56 | P0 gap analysis | Lead + TA | M1 foundations |
| P1 | CI, lint/type checks, two-company synthetic seed, labelled demo tenant with reset | 40 / 60 / 90 | P0 gap analysis | Lead | M1 foundations |
| P2 | Loads: CRUD, search/filter, configurable statuses, history, exceptions, multi-stop | 150 / 220 / 330 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P2 | Assignment + conflict warnings; internal / driver / customer notes; load message threads | 50 / 80 / 120 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P2 | Drivers + fleet (trucks, trailers, equipment, document expiry) | 80 / 120 / 180 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P2 | Brokers/customers/shippers with duplicate prevention | 40 / 60 / 90 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P2 | Documents: validated uploads, versioning, tenant-scoped storage, retention | 60 / 90 / 140 | P1 tenancy + roles | Lead | M2 internal ops |
| P2 | In-app + email notifications, alert rules | 60 / 90 / 140 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P2 | Driver mobile web (responsive/PWA): loads, status, photos, POD, exceptions | 80 / 120 / 180 | P1 tenancy + roles | Lead + TA | M2 internal ops |
| P3 | Money essentials: load revenue, invoices, payments received, expense + fuel entry, receipts, void/correct | 150 / 220 / 330 | P2 loads + documents | Lead + CPA | M3 internal pilot |
| P3 | Load profitability: categories, cost profiles, estimator, snapshots, estimate vs actual | 140 / 200 / 300 | P2 loads + documents | Lead | M3 internal pilot |
| P3 | Routing/miles service for estimator and later ETA/IFTA (licensed truck-routing API) | 40 / 70 / 120 | P2 loads + documents | Lead | M3 internal pilot |
| P3 | Operational dashboard + reports with documented metric definitions | 50 / 80 / 120 | P2 loads + documents | Lead + TA | M3 internal pilot |
| P3 | Import owner's existing data (spreadsheets/QuickBooks) for the pilot | 30 / 50 / 100 | P2 loads + documents | Lead + TA | M3 internal pilot |
| P4 | Public site, technical SEO, GA4 + conversions, UTM attribution, consent | 60 / 100 / 150 | P3; pen test | TA + designer | M4 first outside carrier |
| P4 | Signup, onboarding, Stripe subscriptions, plans/entitlements/usage limits, support inbox | 150 / 230 / 340 | P3; pen test | Lead + TA | M4 first outside carrier |
| P4 | FDL 10% dispatch-fee billing on linehaul only | 40 / 60 / 100 | P3; pen test | Lead + TA | M4 first outside carrier |
| P4 | Super Admin: tenant mgmt, support-access policy + audit | 60 / 90 / 140 | P3; pen test | Lead | M4 first outside carrier |
| P4 | Customer tracking portal (sign-in or expiring links) | 50 / 80 / 120 | P3; pen test | Lead + TA | M4 first outside carrier |
| P4 | Daily immutable snapshots + per-company restore | 60 / 100 / 160 | P3; pen test | Lead (+ DevOps) | M4 first outside carrier |
| P4 | Data export / offboarding | 40 / 60 / 100 | P3; pen test | Lead + TA | M4 first outside carrier |
| P4 | Monitoring, alerting, DR runbook, restore drill | 40 / 60 / 90 | P3; pen test | Lead (+ DevOps) | M4 first outside carrier |
| P4 | Terms/privacy acceptance with versions; GPS and SMS consent records | 16 / 24 / 40 | P3; pen test | Lead + lawyer | M4 first outside carrier |
| P5 | Native driver app iOS/Android (shared codebase): background GPS, camera, store release | 450 / 600 / 850 | P2; store accounts, 10DLC | Mobile dev + Lead | M5 mobile |
| P5 | Offline queue: photos/POD with retries and conflict handling | 120 / 180 / 280 | P2; store accounts, 10DLC | Mobile dev | M5 mobile |
| P5 | GPS discovery: phone vs hardware, consent, retention, working hours *(discovery)* | 20 / 30 / 50 | P2; store accounts, 10DLC | Lead | M5 mobile |
| P5 | GPS: map, last-seen/stale, ETA, history, geofence alerts | 140 / 200 / 300 | P2; store accounts, 10DLC | Lead + TA | M5 mobile |
| P5 | Push + SMS notifications (10DLC, opt-in, quiet hours) | 40 / 60 / 100 | P2; store accounts, 10DLC | Lead + TA | M5 mobile |
| P6 | Per-tenant AI/API usage meter (cost telemetry shared by all AI features) | 40 / 60 / 90 | P3; CPA review | Lead | M6 compliance |
| P6 | Shared document-AI core: extraction, confidence, review queue | 80 / 120 / 180 | P3; CPA review | Lead (+ Doc-AI eng) | M6 compliance |
| P6 | Fleet maintenance + DOT inspection reports, corrective actions | 110 / 160 / 240 | P3; CPA review | Lead + TA | M6 compliance |
| P6 | DVIR pre/post-trip + explainable driver scorecard | 120 / 180 / 280 | P3; CPA review | Lead + TA | M6 compliance |
| P6 | Accounting depth: AR aging, partial-payment allocation, AP, financial reports, exports | 120 / 180 / 270 | P3; CPA review | Lead + CPA | M6 compliance |
| P6 | Settlements (percent/per mile/per vehicle, advances, deductions); payroll export, no payroll tax engine | 120 / 180 / 260 | P3; CPA review | Lead + CPA | M6 compliance |
| P6 | IFTA support (manual miles first, GPS/ELD miles once P7 lands), quarter rules, corrections | 150 / 220 / 320 | P3; CPA review | Lead + CPA | M6 compliance |
| P7 | Integration discovery: ELD, factoring, load boards, fuel cards, accounting *(discovery)* | 60 / 100 / 160 | P0 applications; partner approval | Lead | M7 integrations |
| P7 | ELD/telematics: abstraction + first provider, then 1-2 more (location, mileage, DVIR) | 250 / 380 / 550 | P0 applications; partner approval | Lead + TA | M7 integrations |
| P7 | Accounting export/sync (QuickBooks Online first) | 80 / 120 / 180 | P0 applications; partner approval | Lead + TA | M7 integrations |
| P7 | Factoring package builder + authorized factoring integrations | 100 / 170 / 270 | P0 applications; partner approval | Lead | M7 integrations |
| P7 | Load boards via authorized APIs (DAT/Truckstop) | 100 / 160 / 240 | P0 applications; partner approval | Lead | M7 integrations |
| P7 | Fuel-card integrations | 60 / 100 / 160 | P0 applications; partner approval | Lead + TA | M7 integrations |
| P8 | Back-office discovery: document samples, data agreement, unit economics *(discovery)* | 40 / 60 / 80 | P6 doc-AI core; data agreement | Lead | M8 back office |
| P8 | Labelled evaluation set, accuracy harness, confidence calibration | 100 / 150 / 250 | P6 doc-AI core; data agreement | Doc-AI eng + Lead | M8 back office |
| P8 | Rate-con ingestion, doc classification, BOL/POD extraction, matching | 200 / 300 / 450 | P6 doc-AI core; data agreement | Doc-AI eng + Lead | M8 back office |
| P8 | Auto-invoicing, VA exception queue, straight-through/HIR telemetry | 200 / 300 / 450 | P6 doc-AI core; data agreement | Lead + TA | M8 back office |
| P8 | Routine account assistance (broker/customer lookup, reminders) | 60 / 100 / 160 | P6 doc-AI core; data agreement | Lead + TA | M8 back office |
| P9 | Comms provider evaluation (vendor comparison required before procurement) *(discovery)* | 30 / 40 / 60 | P5, P7; comms provider chosen | Lead | M9 full platform |
| P9 | Unified calls/texts logging, shift handoff summaries, AI communication analyst | 200 / 300 / 450 | P5, P7; comms provider chosen | Lead + 2nd dev | M9 full platform |
| P9 | AI load outreach: AI drafts and suggests counters, human sends and approves | 150 / 220 / 320 | P5, P7; comms provider chosen | Lead + TA | M9 full platform |
| P9 | Spike: autonomous negotiation within owner rules (legal + broker acceptance) *(discovery)* | 40 / 60 / 80 | P5, P7; comms provider chosen | Lead + lawyer | M9 full platform |
| P9 | Broker intelligence + rating (cross-tenant aggregation without leaking private data) | 100 / 150 / 220 | P5, P7; comms provider chosen | Lead | M9 full platform |
| P9 | Roadside repair + service-provider intelligence | 80 / 130 / 200 | P5, P7; comms provider chosen | Lead + TA | M9 full platform |
| P9 | Runbooks, handover docs, final regression and release | 40 / 60 / 100 | P5, P7; comms provider chosen | Lead + TA | M9 full platform |
