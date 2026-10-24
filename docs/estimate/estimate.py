"""Hours and calendar model for the FDL development plan.
Edit the rows or factors and rerun: python -I estimate.py
Each row: phase, workstream, (low, likely, high) hours, kind ('disc' = discovery, 'build' = implementation).
"""
ROWS = [
 # P0 Discovery and baseline
 ("P0","Access/ownership check, backup, baseline commit, dev/staging/prod split", (16,24,40),"disc"),
 ("P0","Codebase inventory, feature classification, gap analysis vs master sheet", (30,44,70),"disc"),
 ("P0","Start external applications: DAT, Truckstop, ELD partners, Intuit, Apple/Google (D-U-N-S), 10DLC", (10,16,24),"disc"),
 # P1 Foundations
 ("P1","Prototype rework or partial rebuild (sized by the gap analysis; owner approval)", (0,120,400),"build"),
 ("P1","Auth: reset, lockout, MFA for owner/admin, sessions", (30,45,70),"build"),
 ("P1","Tenant-scoping contract, DB row-level security, isolation test suite", (50,70,110),"build"),
 ("P1","Roles (Super Admin, Owner, Dispatcher, Driver, Helper, Read-only, Customer), teams/pods", (40,60,90),"build"),
 ("P1","Cross-tenant FDL pod staff access (scoped grants, audited)", (40,60,100),"build"),
 ("P1","Company settings + user management: invite, deactivate, offboard", (30,50,80),"build"),
 ("P1","Audit log framework (actor, action, before/after)", (24,36,56),"build"),
 ("P1","CI, lint/type checks, two-company synthetic seed, labelled demo tenant with reset", (40,60,90),"build"),
 # P2 Core operations
 ("P2","Loads: CRUD, search/filter, configurable statuses, history, exceptions, multi-stop", (150,220,330),"build"),
 ("P2","Assignment + conflict warnings; internal / driver / customer notes; load message threads", (50,80,120),"build"),
 ("P2","Drivers + fleet (trucks, trailers, equipment, document expiry)", (80,120,180),"build"),
 ("P2","Brokers/customers/shippers with duplicate prevention", (40,60,90),"build"),
 ("P2","Documents: validated uploads, versioning, tenant-scoped storage, retention", (60,90,140),"build"),
 ("P2","In-app + email notifications, alert rules", (60,90,140),"build"),
 ("P2","Driver mobile web (responsive/PWA): loads, status, photos, POD, exceptions", (80,120,180),"build"),
 # P3 Money essentials + pilot
 ("P3","Money essentials: load revenue, invoices, payments received, expense + fuel entry, receipts, void/correct", (150,220,330),"build"),
 ("P3","Load profitability: categories, cost profiles, estimator, snapshots, estimate vs actual", (140,200,300),"build"),
 ("P3","Routing/miles service for estimator and later ETA/IFTA (licensed truck-routing API)", (40,70,120),"build"),
 ("P3","Operational dashboard + reports with documented metric definitions", (50,80,120),"build"),
 ("P3","Import owner's existing data (spreadsheets/QuickBooks) for the pilot", (30,50,100),"build"),
 # P4 Commercial launch
 ("P4","Public site, technical SEO, GA4 + conversions, UTM attribution, consent", (60,100,150),"build"),
 ("P4","Signup, onboarding, Stripe subscriptions, plans/entitlements/usage limits, support inbox", (150,230,340),"build"),
 ("P4","FDL 10% dispatch-fee billing on linehaul only", (40,60,100),"build"),
 ("P4","Super Admin: tenant mgmt, support-access policy + audit", (60,90,140),"build"),
 ("P4","Customer tracking portal (sign-in or expiring links)", (50,80,120),"build"),
 ("P4","Daily immutable snapshots + per-company restore", (60,100,160),"build"),
 ("P4","Data export / offboarding", (40,60,100),"build"),
 ("P4","Monitoring, alerting, DR runbook, restore drill", (40,60,90),"build"),
 ("P4","Terms/privacy acceptance with versions; GPS and SMS consent records", (16,24,40),"build"),
 # P5 Mobile and tracking
 ("P5","Native driver app iOS/Android (shared codebase): background GPS, camera, store release", (450,600,850),"build"),
 ("P5","Offline queue: photos/POD with retries and conflict handling", (120,180,280),"build"),
 ("P5","GPS discovery: phone vs hardware, consent, retention, working hours", (20,30,50),"disc"),
 ("P5","GPS: map, last-seen/stale, ETA, history, geofence alerts", (140,200,300),"build"),
 ("P5","Push + SMS notifications (10DLC, opt-in, quiet hours)", (40,60,100),"build"),
 # P6 Compliance, accounting depth, shared document-AI core
 ("P6","Per-tenant AI/API usage meter (cost telemetry shared by all AI features)", (40,60,90),"build"),
 ("P6","Shared document-AI core: extraction, confidence, review queue", (80,120,180),"build"),
 ("P6","Fleet maintenance + DOT inspection reports, corrective actions", (110,160,240),"build"),
 ("P6","DVIR pre/post-trip + explainable driver scorecard", (120,180,280),"build"),
 ("P6","Accounting depth: AR aging, partial-payment allocation, AP, financial reports, exports", (120,180,270),"build"),
 ("P6","Settlements (percent/per mile/per vehicle, advances, deductions); payroll export, no payroll tax engine", (120,180,260),"build"),
 ("P6","IFTA support (manual miles first, GPS/ELD miles once P7 lands), quarter rules, corrections", (150,220,320),"build"),
 # P7 Integrations
 ("P7","Integration discovery: ELD, factoring, load boards, fuel cards, accounting", (60,100,160),"disc"),
 ("P7","ELD/telematics: abstraction + first provider, then 1-2 more (location, mileage, DVIR)", (250,380,550),"build"),
 ("P7","Accounting export/sync (QuickBooks Online first)", (80,120,180),"build"),
 ("P7","Factoring package builder + authorized factoring integrations", (100,170,270),"build"),
 ("P7","Load boards via authorized APIs (DAT/Truckstop)", (100,160,240),"build"),
 ("P7","Fuel-card integrations", (60,100,160),"build"),
 # P8 Automated back office
 ("P8","Back-office discovery: document samples, data agreement, unit economics", (40,60,80),"disc"),
 ("P8","Labelled evaluation set, accuracy harness, confidence calibration", (100,150,250),"build"),
 ("P8","Rate-con ingestion, doc classification, BOL/POD extraction, matching", (200,300,450),"build"),
 ("P8","Auto-invoicing, VA exception queue, straight-through/HIR telemetry", (200,300,450),"build"),
 ("P8","Routine account assistance (broker/customer lookup, reminders)", (60,100,160),"build"),
 # P9 AI and intelligence
 ("P9","Comms provider evaluation (vendor comparison required before procurement)", (30,40,60),"disc"),
 ("P9","Unified calls/texts logging, shift handoff summaries, AI communication analyst", (200,300,450),"build"),
 ("P9","AI load outreach: AI drafts and suggests counters, human sends and approves", (150,220,320),"build"),
 ("P9","Spike: autonomous negotiation within owner rules (legal + broker acceptance)", (40,60,80),"disc"),
 ("P9","Broker intelligence + rating (cross-tenant aggregation without leaking private data)", (100,150,220),"build"),
 ("P9","Roadside repair + service-provider intelligence", (80,130,200),"build"),
 # Throughout
 ("P9","Runbooks, handover docs, final regression and release", (40,60,100),"build"),
]
QA = 0.20            # testing, hardening, UAT, regression on top of every row
CONTINGENCY = 0.15   # scope not yet in the rows (the spec still has open decisions)
PTO = 1.08           # holidays, leave, sick days stretch the calendar
NAMES = ("Optimistic (P10)", "Realistic (expected)", "Conservative (P90)")
Z = (-1.28, 0.0, 1.28)
# Productive build hours per week. Lead + TA = 80 paid hours; the Lead loses time to review, tickets, reports, vendors.
LEAD_TA = (58, 54, 50)
# Recommended team: + 0.5 FTE QA from P3; + mobile dev and a second full-stack dev from P5; + doc-AI engineer in P8.
EXTRA = {"P3": 14, "P4": 14, "P5": 66, "P6": 66, "P7": 66, "P8": 90, "P9": 66}
FACTOR = (1 + QA) * (1 + CONTINGENCY)


def pert(rows):
    """Three-point (PERT) estimate: mean and std dev.
    Std devs are summed, not added in quadrature: estimate errors share causes (same team, same
    prototype, same vendors), and treating 60+ rows as independent would shrink the range to a few percent."""
    mean = sum((lo + 4 * ml + hi) / 6 for _, _, (lo, ml, hi), _ in rows)
    sd = sum((hi - lo) / 6 for _, _, (lo, ml, hi), _ in rows)
    return mean, sd


def phases():
    out = {}
    for r in ROWS:
        out.setdefault(r[0], []).append(r)
    return out


def scenario_hours(rows):
    mean, sd = pert(rows)
    return [(mean + z * sd) * FACTOR for z in Z]


def calendar(extra):
    # Phase percentiles do not add up to a project percentile, so scale each phase by the project ratio.
    mean, _ = pert(ROWS)
    proj = scenario_hours(ROWS)
    weeks, out = [0.0, 0.0, 0.0], {}
    for p, rows in phases().items():
        m, _ = pert(rows)
        for i in range(3):
            hours = m * FACTOR * proj[i] / (mean * FACTOR)
            scale = LEAD_TA[i] / LEAD_TA[1]
            weeks[i] += hours / (LEAD_TA[i] + extra.get(p, 0) * scale) * PTO
        out[p] = list(weeks)
    return out


DEPENDS = {"P0": "Owner grants access", "P1": "P0 gap analysis", "P2": "P1 tenancy + roles",
           "P3": "P2 loads + documents", "P4": "P3; pen test", "P5": "P2; store accounts, 10DLC",
           "P6": "P3; CPA review", "P7": "P0 applications; partner approval", "P8": "P6 doc-AI core; data agreement",
           "P9": "P5, P7; comms provider chosen"}
MILESTONE = {"P0": "M0 gap analysis", "P1": "M1 foundations", "P2": "M2 internal ops", "P3": "M3 internal pilot",
             "P4": "M4 first outside carrier", "P5": "M5 mobile", "P6": "M6 compliance", "P7": "M7 integrations",
             "P8": "M8 back office", "P9": "M9 full platform"}
STAFF = [  # first keyword match wins; default Lead + TA
    ("Load profitability", "Lead"), ("Routing/miles", "Lead"), ("Native driver app", "Mobile dev + Lead"), ("Offline", "Mobile dev"), ("evaluation set", "Doc-AI eng + Lead"),
    ("Rate-con", "Doc-AI eng + Lead"), ("document-AI", "Lead (+ Doc-AI eng)"), ("IFTA", "Lead + CPA"),
    ("Settlements", "Lead + CPA"), ("Accounting depth", "Lead + CPA"), ("Money essentials", "Lead + CPA"),
    ("Public site", "TA + designer"), ("Tenant", "Lead"), ("Auth", "Lead"), ("Cross-tenant", "Lead"),
    ("snapshots", "Lead (+ DevOps)"), ("Monitoring", "Lead (+ DevOps)"), ("Terms/privacy", "Lead + lawyer"),
    ("negotiation", "Lead + lawyer"), ("calls/texts", "Lead + 2nd dev"), ("discovery", "Lead"), ("evaluation", "Lead"),
]


def staff(name):
    return next((who for key, who in STAFF if key.lower() in name.lower()), "Lead + TA")


def workstream_table():
    print("| Phase | Workstream | Hours low / likely / high | Depends on | Staff | Milestone |")
    print("|---|---|---|---|---|---|")
    for p, name, (lo, ml, hi), kind in ROWS:
        tag = " *(discovery)*" if kind == "disc" else ""
        print(f"| {p} | {name}{tag} | {lo} / {ml} / {hi} | {DEPENDS[p]} | {staff(name)} | {MILESTONE[p]} |")


if __name__ == "__main__" and "--workstreams" in __import__("sys").argv:
    workstream_table()
elif __name__ == "__main__":
    print("| Phase | Base low / likely / high | Expected (PERT) | Expected + QA + contingency |")
    print("|---|---|---|---|")
    for p, rows in phases().items():
        lo, ml, hi = (sum(r[2][i] for r in rows) for i in range(3))
        m, _ = pert(rows)
        print(f"| {p} | {lo:,} / {ml:,} / {hi:,} | {m:,.0f} | {m * FACTOR:,.0f} |")
    lo, ml, hi = (sum(r[2][i] for r in ROWS) for i in range(3))
    m, sd = pert(ROWS)
    print(f"| **Total** | {lo:,} / {ml:,} / {hi:,} | {m:,.0f} | **{m * FACTOR:,.0f}** |")
    h = scenario_hours(ROWS)
    print()
    print("Project hours incl. QA + contingency: " + ", ".join(f"{NAMES[i]} {h[i]:,.0f}" for i in range(3)))
    disc = sum((r[2][0] + 4 * r[2][1] + r[2][2]) / 6 for r in ROWS if r[3] == "disc")
    print(f"Discovery (expected, base): {disc:,.0f} h")
    for label, extra in (("Lead + TA only", {}), ("Recommended team", EXTRA)):
        print()
        print(f"Calendar, {label} (cumulative, end of phase):")
        print("| Phase | " + " | ".join(NAMES) + " |")
        print("|---|---|---|---|")
        for p, w in calendar(extra).items():
            print(f"| {p} | " + " | ".join(f"{x / 4.33:.1f} mo ({x:.0f} wk)" for x in w) + " |")
