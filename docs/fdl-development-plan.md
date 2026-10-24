# FDL Platform: Development Timeline and Cost Assessment

Prepared for Family Dispatch & Logistics by Mark Angelo Pasion, Lead Developer candidate, 25 October 2026.
Based on the *Technical Master Sheet, Developer Estimation Edition* (extract of Master Feature Specification v6,
23 October 2026). All figures are estimates. The assumptions behind each are stated, and they will be re-forecast
after Phase 0 discovery of the existing Replit project.

## Summary

| Question | Answer |
|---|---|
| 1. Total development hours | **About 11,200 h realistic** (range 9,150 to 13,250), including testing and contingency. That's 8,100 h of feature work + 20% testing/hardening + 15% contingency for scope the spec still leaves open |
| 2. Total timeline | **About 31 months (135 weeks) realistic** with the recommended team (range 24 to 40 months). With only Lead + TA: about 52 months (39 to 66) |
| 3. Phase-by-phase plan | **10 phases (P0 Discovery to P9 AI and intelligence)**, each with its scope, hours and end month, and a milestone with a deliverable (M0 to M9). Section 2, with every workstream in the appendix |
| 4. First customer-ready version | **Owner's own company (internal pilot): month 9 for dispatch, month 12 with money and the profitability estimator.** **First outside paying carrier: about month 17** (13 to 21). An accelerated option with a second developer from month 2 brings this to about month 11 |
| 5. Entire platform incl. future features | **About month 31** (24 to 40) with the recommended team |
| 6. Lead vs TA | The Lead owns architecture, security, tenancy, money logic, integrations, review and releases. The TA owns screens, CRUD, tests, QA, docs and test data. Section 6 |
| 7. AI tools | Claude Code, Replit Agent, ChatGPT, Copilot, all with mandatory human review. Section 7 and [technical-leadership.md](technical-leadership.md) |
| 8. Monthly technical expenses | **About $250-350 while building, $450-750 after launch, $1,350-5,400 at full platform scale**, plus usage-based items and licences that need quotes. Section 8 |
| 9. Extra staffing | Part-time QA from month ~9. A mobile developer and a second full-stack developer from month ~17. A document-AI engineer in P8. One-off: UX designer, penetration test, trucking CPA, US lawyer. Section 9 |
| 10. Main risks | Unknown prototype quality, third-party API approvals, real data for AI vs the no-real-data rule, app-store and SMS registration, cross-tenant leakage, AI making commitments. Section 10 |

The **estimating model** is in [estimate/estimate.py](estimate/estimate.py) and its output in
[estimate/estimate-output.md](estimate/estimate-output.md). Every row, factor and assumption is in that file and can
be changed and rerun.

## 1. How the estimate was built

- **Workstreams.** Every feature in the master sheet and its addenda maps to one of **62 workstreams**, each with
  a low / likely / high hour figure. Discovery rows are kept separate from build rows, as the instructions ask
  (about 380 h of discovery).
- **Three-point estimate.** Expected = (low + 4 × likely + high) / 6.
  - **Optimistic** = the 10th percentile. **Conservative** = the 90th.
  - Risk is treated as correlated across rows (same team, same prototype, same vendors), so the range doesn't shrink
    falsely.
- **Factors applied to every row:**
  - +20% testing, hardening, user acceptance and regression
  - +15% contingency for scope not yet in the rows
  - +8% calendar time for holidays and leave
- **Productive build hours per week** for Lead + TA (80 paid hours): **58 optimistic / 54 realistic / 50
  conservative.** The rest goes to code review, tickets, the weekly report, demos, vendor calls and mentoring.
- **AI tools are already in the hours.** I assume AI cuts roughly 25-35% of pure coding time on CRUD, screens and
  tests, but little on discovery, integration approvals, accounting rules, security review or acceptance testing.
  So the plan doesn't count on more than a 15-20% overall saving.
- **Nothing in the existing prototype is counted as done.** I haven't seen the "FAMILY DISPATCH" Replit source,
  so every feature is estimated as work still to do. Phase 0 classifies each prototype feature as working with a
  persistent backend, partly working, UI-only, broken or not built, verified in the source code and shown live.
  Whatever turns out to be sound comes off the P1-P2 hours at the M0 re-forecast. Prototype rework has its own row
  (0 / 120 / 400 h), so the estimate covers a rebuild without assuming one.
- **An independent review changed the numbers.** A skeptical review of the first draft found missing scope:
  - prototype rework
  - FDL's own 10% dispatch-fee billing
  - cross-tenant pod staff access
  - plans and entitlements
  - truck routing
  - data import

  It also found that the testing and capacity factors were too generous. All of that is now included. The first draft
  said 8,400 h. This one says 11,200.

**What would move the estimate:**

- **Down:** the Phase 0 audit finds the Replit prototype has a sound, salvageable backend (it could save 100-400 h
  in P1-P2), or the owner defers features.
- **Up:** the prototype is UI-only and needs a rebuild, integrations need partner programs that take months, or
  "web feature parity" on mobile means the whole platform rather than the driver experience.

## 2. Phase plan, milestones and deliverables

Hours include testing and contingency. Months are realistic and cumulative, with the recommended team.

| Phase | Scope (main items) | Hours | Ends ~ | Milestone / deliverable |
|---|---|---|---|---|
| **P0 Discovery** | Confirm the owner controls every account; baseline commit + backup; separate dev/staging/prod; inventory of screens, routes, schema, auth, APIs; classify each feature as working / partial / mock / broken / not built; gap analysis against the full master sheet; **start external applications now** (DAT, Truckstop, ELD partners, Intuit, Apple/Google with a D-U-N-S number, 10DLC) | 120 | Week 2-3 | **M0:** written gap analysis, live demo of what really works, re-forecast estimate. **Owner decides:** build on the prototype or rebuild parts |
| **P1 Foundations** | Prototype rework (sized by P0); secure auth with reset, lockout and MFA for owner/admin; tenant-scoping contract + database row-level security + isolation test suite; all roles incl. Helper, Read-only, Customer, teams/pods; scoped cross-tenant access for FDL pod staff; user management; audit log; CI; two-company synthetic data; labelled demo mode | 750 | Month 4 | **M1:** isolation and role tests green in CI; staging environment; demo tenant |
| **P2 Core operations** | Loads (search/filter, configurable statuses, history, exceptions, multi-stop), assignment with conflict warnings, separate internal/driver/customer notes, message threads, drivers, fleet, brokers/customers, documents with versioning, in-app + email notifications, mobile-friendly driver web app | 1,110 | Month 9 | **M2: internal operations release.** FDL's own dispatchers and drivers run real loads |
| **P3 Money essentials** | Load revenue, invoices, payments received, expenses and fuel with receipts, void/correct (never delete); **Load Cost & Profitability Calculator** (cost profiles, cost per mile, estimator, saved snapshots, estimate vs actual); truck routing/miles; dashboard with documented metric definitions; import of the owner's existing data | 890 | Month 12 | **M3: internal pilot complete.** The owner runs Family Auto Transportation on the platform, with a CPA review of the money rules |
| **P4 Commercial launch** | Public website, technical SEO, GA4 conversions, UTM attribution, consent; signup, onboarding, Stripe subscriptions, plans and usage limits; FDL's 10% dispatch-fee billing on linehaul; Super Admin with audited support access; customer tracking portal; daily immutable snapshots + per-company restore; data export/offboarding; monitoring + disaster-recovery drill; terms/privacy acceptance; **penetration test** | 1,140 | Month 17 | **M4: first outside paying carrier.** Pre-launch security checklist and pen test passed |
| **P5 Mobile + tracking** | Native iOS/Android driver app (background GPS, camera, offline queue for photos and POD), app store release; GPS map, stale-location flags, ETAs labelled as estimates, history, geofence alerts; push + SMS (10DLC, opt-in, quiet hours). Owners and dispatchers keep full parity through the responsive web app | 1,530 | Month 20 | **M5:** apps in both stores; tracking live with driver consent |
| **P6 Compliance + accounting depth** | Per-tenant AI/API cost meter; shared document-AI core (extraction, confidence, review queue); fleet maintenance + DOT inspection reports with corrective actions; DVIR + explainable driver scorecard; AR aging, partial-payment allocation, AP, financial reports; settlements; IFTA support (manual miles first) | 1,560 | Month 23 | **M6:** maintenance, inspections and full accounting. CPA sign-off on IFTA and settlements |
| **P7 Integrations** | Integration discovery; ELD/telematics (one provider plus abstraction layer, then 1-2 more); QuickBooks Online sync; factoring package builder + authorized factoring APIs; DAT/Truckstop via authorized APIs; fuel cards | 1,460 | Month 26 | **M7:** each integration live only with the owner's approved credentials and partner agreements |
| **P8 Automated back office** | Signed data agreement and redacted real samples; labelled evaluation set and accuracy harness; rate-con ingestion, document classification, BOL/POD extraction and matching; auto-invoicing; VA exception queue; straight-through and human-intervention rate telemetry; routine account assistance | 1,300 | Month 28 | **M8:** back-office product launched on supported document formats, with the measured automation rate published to Super Admin |
| **P9 AI + intelligence** | Phone/text provider comparison (no provider has been selected yet); unified call/text history, AI shift handoffs, AI communication analyst; AI load outreach that drafts and suggests while a human approves every commitment; autonomous negotiation spike (legal review first); broker intelligence and rating; roadside repair + provider intelligence; runbooks and handover | 1,360 | Month 31 | **M9: full platform.** Handover documentation lets another developer take over |

**Critical path:** P0 gap analysis → P1 tenant and role model → P2 loads and documents → P3 money → P4 billing,
security and pen test → first outside carrier.

Things that can run in parallel once the team grows:

- the native app (P5) beside accounting depth (P6)
- integrations (P7), gated by partner approvals that start in P0
- the shared document-AI core, built once in P6 and reused by P8

**External dependencies on the critical path:**

- Partner approvals (DAT, Truckstop, ELD vendors, Intuit) take weeks to months, which is why they start in P0.
- App-store review of background location needs a written justification for Apple and a declaration for Google.
- 10DLC registration takes 2-6 weeks and can be rejected.
- Back-office AI can't reach its accuracy target without real sample documents under a data agreement.

## 3. Optimistic, realistic and conservative estimates

| | Optimistic (P10) | Realistic (expected) | Conservative (P90) |
|---|---|---|---|
| Total hours (incl. testing + contingency) | 9,150 | 11,200 | 13,250 |
| Internal operations release (M2) | Month 7 | Month 9 | Month 12 |
| Internal pilot complete (M3) | Month 9 | Month 12 | Month 16 |
| First outside paying carrier (M4) | Month 13 | Month 17 | Month 21 |
| Full platform (M9), recommended team | Month 24 | **Month 31** | Month 40 |
| Full platform (M9), Lead + TA only | Month 39 | Month 52 | Month 66 |
| **Accelerated:** second full-stack developer from month 2 | First outside carrier ~month 9, full platform ~month 20 | **First outside carrier ~month 11, full platform ~month 26** | First outside carrier ~month 14, full platform ~month 33 |

**Assumptions behind each scenario**

- **Optimistic.**
  - The prototype's backend is largely reusable.
  - The owner answers open questions within days.
  - Partner approvals arrive while P2-P4 are being built.
  - The TA ramps up quickly.
  - Little rework comes out of user acceptance testing.
- **Realistic.**
  - About 120 h of prototype rework.
  - Normal back-and-forth on requirements.
  - One or two integrations need a different provider than planned.
  - About 54 productive hours a week from Lead + TA.
  - Specialists join at the phases shown.
- **Conservative.**
  - Large parts of the prototype are UI-only and need rebuilding (up to 400 h).
  - Accounting and IFTA rules change after CPA review.
  - A load board or factoring partner declines API access, so a substitute is needed.
  - Back-office AI needs extra iterations to reach its accuracy targets.
  - A team change costs a few weeks.

I recommend planning against the **realistic** column and reporting progress against it every week. The plan is
re-forecast at each milestone, never stretched silently.

## 4. First customer-ready version

There are two meanings, and I'd plan both:

1. **Internal: FDL's own Family Auto Transportation operation.**
   - **About month 9:** dispatch, drivers, fleet, documents and the driver web app. This is when it becomes useful
     day to day.
   - **About month 12:** invoicing, expenses and the profitability estimator added.

   Real data is used here only after the security foundations (P1) are verified and the owner approves moving it in.
2. **External: the first paying outside carrier, about month 17** (month 11 with the accelerated option). Selling to
   outside companies adds requirements the internal pilot doesn't need:
   - signup and billing
   - an audited support-access policy
   - backups with a tested restore
   - data export when a customer leaves
   - terms and privacy acceptance
   - a passed penetration test

## 5. Entire platform

About **month 31** with the recommended team (24-40), or about month 26 with the accelerated option. Phases P5-P9
follow the order of business value and dependencies. The owner can re-order or defer any of them at a milestone
review without throwing away completed work. For example, the back office (P8) could come before integrations (P7)
if that product sells sooner.

## 6. Dividing responsibilities: Lead Developer and Technical Assistant

| Lead Developer | Technical Assistant |
|---|---|
| Phase 0 discovery, architecture, data model, migrations | Screens and forms against agreed APIs |
| Authentication, roles, tenant isolation (database row-level security) | CRUD modules with clear specs (fleet, brokers, expense categories) |
| Money: invoicing, profitability, settlements, IFTA, dispatch-fee billing | Test cases the Lead specifies, plus a regression test for every bug |
| Integrations, AI pipelines, cost meter | Synthetic two-company test data and the demo tenant |
| Code review of every pull request, releases, production access | QA passes on staging before each demo |
| Weekly report, demos, vendor and owner communication | Setup docs, user guides, the implemented-vs-simulated list |

The TA takes on harder work as they prove themselves. Security, tenancy and money code always get the Lead's review.
Details are in [technical-leadership.md](technical-leadership.md).

## 7. AI tools and quality

| Tool | Role |
|---|---|
| **Claude Code** (Lead) | Implementing tickets, refactoring, writing tests, an independent second-opinion review of pull requests |
| **Replit Agent** | Scoped tickets inside the existing Replit project, always in a branch |
| **ChatGPT** (already used by the owner) | Keeping the master requirements current, drafting tickets, acceptance criteria and test checklists |
| **GitHub Copilot / Claude** (TA) | Autocomplete and explaining unfamiliar code |
| **Claude / document-AI APIs** (in the product) | Rate-con and BOL/POD extraction, DOT report extraction, handoff summaries, communication analysis, always with confidence scores and human review |

**How quality is kept:**

- Every AI change goes through a pull request reviewed by the Lead.
- CI runs the tenant-isolation and role suite on every change.
- Money tests use expected values worked out by hand, never copied from the code.
- An AI review pass gets the code without my conclusions, so it can't just agree with me.
- No real data or secrets go into AI tools.
- The person who opens a PR must be able to explain every line of it.

The broken-code challenge in this submission shows this in practice. An AI-written test was wrong and was caught
because of these steps.

## 8. Monthly technical expenses

USD, published prices checked October 2026. "Unknown" means the vendor publishes no price: quote needed.

**Stage 1: building (months 1-12), about $250-350/month**

| Item | Monthly |
|---|---|
| Replit Pro (up to 15 collaborators, includes $100 credits) | $100 |
| GitHub Team, 3 seats × $4 | $12 |
| AI dev tools: Claude Max for the Lead ($100), Claude Pro for the TA ($20), ChatGPT Plus for the owner ($20) | $140 |
| Staging hosting + database (Replit reserved VM $15-35 + managed Postgres) | $20-60 |
| Error tracking, email, file storage (free tiers: Sentry, Resend, Cloudflare R2 10 GB) | $0-10 |

**Stage 2: pilot and commercial launch (months 12-24, up to ~25 companies), about $450-750/month plus the routing licence (quote) and Stripe fees**

| Item | Monthly |
|---|---|
| Production + staging hosting (reserved VM 2 vCPU $50 + staging; Render/Fly.io similar) | $65-120 |
| Managed Postgres with point-in-time restore (Neon / Supabase Pro / Fly MPG $25-100) | $25-100 |
| File storage (Cloudflare R2 $0.015/GB, no egress fees) + off-site backup copies | $10-40 |
| Monitoring: Sentry Team $29, uptime/logs (Better Stack free-$34) | $29-63 |
| Transactional email (Postmark $15 / 10k emails) | $15 |
| Maps for the estimator and portal (Mapbox and Google free tiers cover early volume) | $0-100 |
| Truck routing / miles licence (PC*Miler or a truck-routing API) | **Unknown: quote** |
| Cookie consent (CookieYes $10), domain and DNS | $12-15 |
| Dev tools (Stage 1 plus QA seat) | $270-300 |
| **Stripe** (usage-based, not monthly): 2.9% + 30¢ per card payment, 0.8% for ACH (capped at $5), +0.7% Billing | % of revenue |

**Stage 3: full platform (month 18+, 25-150 companies), about $1,350-5,400/month**, the wide range driven mostly by AI usage, plus unpublished partner fees

| Item | Monthly |
|---|---|
| Hosting + database at scale (more instances, read replica, larger DB) | $300-900 |
| Mobile: Apple $99/yr, Google Play $25 once, Expo EAS $19-199 | $30-210 |
| Maps/GPS (depends on how often locations are recorded and on map loads) | $100-600 |
| SMS: Twilio $0.0083/segment + carrier fees ($0.0025-0.007), number $1.15, 10DLC campaign $10/mo (+$46 brand, $15 vetting, one-time) | $50-300 |
| Push notifications (Firebase Cloud Messaging) | $0 |
| AI and document processing (LLM tokens + OCR such as AWS Textract at $1.50-$50 per 1,000 pages, depending on feature) | $300-2,000, **metered per tenant** |
| Business phone/text system (provider intentionally undecided; typical per-seat pricing) | $150-500 |
| QuickBooks Online API (Intuit Builder tier free; paid tiers above the free read limit) | $0-300 |
| ELD, load-board and factoring API fees | **Unknown: mostly paid by the carrier's own subscriptions; partner fees not published** |
| Dev tools for a 5-6 person team | $400-600 |

**Pricing principle.** Usage-based costs (AI, OCR, SMS, maps) are measured per company by the P6 cost meter, as the
master sheet asks. Plan pricing then follows measured cost rather than guesses, and unlimited use is never offered at
the base price.

**Labor.** Lead $1,100/month and TA ~$600/month (the TA rate is my assumption):

| Team | Approx. labor to full platform |
|---|---|
| Lead + TA only | ~52 months × $1,700 ≈ **$88,000** |
| Recommended team | Months 1-9 $1,700/mo; 9-17 $2,100/mo (+ part-time QA); 17-31 about $5,500-6,500/mo (+ mobile developer and second full-stack developer, both PH/LatAm contract rates; + doc-AI engineer during P8) ≈ **$115,000-$135,000**, finished about 21 months earlier |

**One-off specialists (estimates; get 2-3 quotes each):**

- UX designer, 100-150 h: $3,500-8,000
- Penetration test before the external launch, and again after the AI and comms features ship: $8,000-20,000 each
- CPA with trucking/IFTA experience, 30-60 h: $4,500-18,000
- US lawyer for terms, privacy, GPS consent, call-recording consent and AI negotiation: $3,000-10,000
- DevOps help, 60-120 h each at P1 and P4, if the chosen host needs it: $3,000-10,000

## 9. Additional staffing and outside expertise

| When | Who | Why |
|---|---|---|
| P0-P2, P4, P5 | UX designer (part-time) | Driver mobile flows, the owner dashboard, the public site. The Lead + TA can build screens but shouldn't design the brand |
| From P3 | QA tester (~0.5 FTE) | Money and tenant regression grow faster than two people can re-test by hand |
| P3 and P6 | CPA with trucking/IFTA experience | The master sheet requires accounting, IFTA and settlement rules to be validated by a professional |
| P4, P5, P9 | US lawyer | Terms/privacy, GPS consent, call-recording consent (some states require all-party consent), employment-law angle of driver scorecards, binding commitments in AI negotiation |
| Before M4, after P9 | Penetration tester | Independent proof of tenant isolation and auth before outside carriers trust the platform with their data |
| P5 | Mobile developer (React Native/Expo) | About 600 h of native work. In parallel it saves 3-4 months |
| P5-P9 (or from month 2 for the accelerated option) | Second full-stack developer | Lead + TA alone take about 52 months; this is the biggest lever on the date |
| P8 | Document-AI engineer (300-500 h) | Evaluation sets, calibration, the 95% straight-through target |
| P1, P4 | DevOps (short engagements) | Backups, disaster recovery, infrastructure as code, if production leaves Replit |

## 10. Main technical challenges, risks and dependencies

| # | Risk / dependency | Impact | Mitigation |
|---|---|---|---|
| 1 | **Unknown state of the Replit prototype** (stack, data model, whether screens are backed by a database) | 0-400 h of rework; may change hosting | Phase 0 audit before any change; the owner approves build-on vs rebuild with evidence |
| 2 | **Cross-tenant data leakage** through pods, broker intelligence (aggregated across carriers), the customer portal, exports, search and files | Loss of trust, legal exposure | Database row-level security under application checks; isolation tests for each surface in CI; pen test before launch |
| 3 | **Third-party approvals**: DAT/Truckstop need commercial agreements and may refuse a dispatch SaaS; few factoring companies have APIs; Intuit reviews apps before production keys | Integrations slip or need substitutes | Apply in P0; design an integration layer with a manual fallback (package export, CSV) |
| 4 | **Real data for AI vs the "no real data in unproven builds" rule** | The back office can't reach 95% straight-through without real documents | Signed data agreement, redaction, a locked evaluation environment; state 95% as a measured target on supported formats, not a launch promise |
| 5 | **AI making commitments** (rate negotiation, return-to-service, discipline) | Binding a carrier to a rate it didn't approve | A human approves every commitment; logs; owner-defined rules; legal review before any autonomy |
| 6 | **Accounting/IFTA correctness** | Wrong money or tax figures | Decimal money with explicit rounding; void instead of delete; earned / invoiced / collected kept separate; CPA validation; tests on every boundary (zero revenue, margin of 100% or more, IFTA quarter edges, time zones and DST on cross-zone loads) |
| 7 | **App-store and SMS registration** (background location review, D-U-N-S number, 10DLC, TCPA opt-in) | Mobile or SMS launch delayed by weeks | Start registrations early; written location purpose; opt-in records |
| 8 | **Running costs per customer** (AI tokens, maps, SMS, routing licence) | Margin erosion | Per-tenant cost meter (P6); usage limits per plan |
| 9 | **Key-person dependency** on the Lead | Project stalls if the Lead is unavailable | The owner controls every account; runbooks and handover docs; a TA who knows the codebase; small reviewed pull requests |
| 10 | **Open requirements in the spec** | Rework | Owner questions below, answered before the phase that needs them |

**Questions for the owner** (they don't block P0; each is needed before the phase shown)

1. The **roles and permissions table (section 3)** and the **acceptance criteria (section C)** are blank in the
   candidate edition. Can I see the full versions? (P1)
2. How do **FDL pod staff** work inside many carrier companies? What can they see and change, and who approves their
   access? (P1)
3. What exactly is **"linehaul revenue"** for the 10% fee? Does it exclude fuel surcharge, detention and other
   accessorials? (P4)
4. **Customer portal**: sign-in, expiring links, or both? (P4)
5. **Mobile parity**: is a native driver app plus a full responsive web app for office roles acceptable, or must the
   native apps cover every owner/dispatcher screen? (P5)
6. **GPS**: when does tracking start and stop, how long is location history kept, and does it apply to owner-operators?
   (P5)
7. Which **ELD, factoring and accounting providers** do the owner and the first target carriers use today? (P0, so
   applications can start)
8. Does the owner have a **trucking CPA** already? (P3)
9. Can redacted **real rate confirmations and BOLs** be used for AI evaluation under a data agreement? (P8)
10. **Hosting**: is staying on Replit for production a preference, or is moving to a dedicated host acceptable if the
    audit shows it's needed? (P0)

## Appendix: workstream estimate

The master sheet's estimate template asks for each workstream with its features, hours (low / likely / high), dependencies, staff and milestone. This table is generated from the estimating model (`python docs/estimate/estimate.py --workstreams`), so it always matches the totals above. Hours here are base feature hours, before the 20% testing and 15% contingency. Rows marked *(discovery)* are discovery, estimated separately from implementation as the master sheet asks.

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
