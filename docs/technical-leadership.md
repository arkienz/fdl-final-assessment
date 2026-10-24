# Technical Leadership and AI Development Approach

How I would run FDL development day to day as Lead Developer, with one Technical Assistant (TA), the business
owner as the approver, and AI tools in the loop.

## 1. Assigning and reviewing the Technical Assistant's work

**Who owns what**

| Lead Developer owns | Technical Assistant owns (reviewed by the Lead) |
|---|---|
| Architecture, data model, migrations | Screens and forms that use agreed APIs |
| Authentication, roles, tenant isolation | CRUD for well-defined records (trucks, brokers, expense categories) |
| Money: accounting, profitability, invoicing, IFTA logic | Tests: writing the cases the Lead lists, plus regression tests for every bug |
| Third-party integrations, AI pipelines | Test data (synthetic two-company seed), QA passes on staging |
| Code review, releases, production access | Docs: setup steps, user guides, the implemented-vs-simulated list |
| Weekly report to the owner | First-line bug reproduction |

The TA moves into harder areas as they show they can handle them, starting with tests and screens. Security, tenant
scoping and money code always get the Lead's review, whoever writes them.

**How work is assigned**

- **Tickets.** Every task is a GitHub Issue small enough to finish in 1-2 days, with:
  - the user story and acceptance criteria
  - the files or areas it touches
  - which tests must exist
  - what "done" means: deployed to staging, tests green, demo note written

  ChatGPT or Claude can draft a ticket from the master sheet. I edit and approve it before it is assigned.
- **Daily rhythm.** A 15-minute daily check-in (async message or call) covers done, next and blocked. A weekly 1:1 covers
  growth and anything harder to say in a group.

**How work is reviewed**

- **Pull requests.** Every change is a pull request against `main`. I review against a short checklist:
  - tenant filter present on every query
  - role check on the server
  - input validated
  - no secrets
  - money in decimal with explicit rounding
  - migration reversible
  - tests cover the edge cases
  - AI-generated code understood, not just pasted
- **The TA explains their own pull request.** Small PRs (under ~400 lines) get reviewed the same day. For a large or
  AI-heavy change, the TA walks me through it in 10 minutes. If they can't explain a block, it doesn't merge. This is
  also how they learn.
- **Review is teaching.** Repeated review comments become checklist items or lint rules, so the same mistake isn't
  corrected by hand twice.

## 2. GitHub, Replit and AI tools

**GitHub is the source of truth**

- **Owner control.** The repository lives in an organization the **owner controls**. The Lead and TA have named
  accounts with MFA. Nobody shares passwords or verification codes (master sheet B2).
- **Branches.** Feature branches go to pull request, then to `main`, then to tagged releases. Issues and a Projects
  board track the roadmap, and the milestones on the board match the phase plan.
- **CI on every pull request (GitHub Actions):**
  - build, lint and type checks
  - unit tests
  - the tenant-isolation and role-permission suite (a request as Company A for Company B's records must get a 404)
  - a dependency vulnerability audit and a secret scan

  A red check blocks the merge.

**Replit is the development workspace, connected to GitHub**

- **Phase 0 comes first.** I audit the existing "FAMILY DISPATCH" Replit project before changing anything: confirm
  ownership, make a baseline commit and a backup, and classify every feature as working, partial, mock, broken or
  not built.
- **Replit Agent works in a branch.** It is used for scoped tickets, never on `main` and never against the
  production database. Its output is reviewed like anyone else's. Passing a build is not proof of correctness or
  security (master sheet B1).
- **Production is separate.** Replit Deployments can host production if load and cost suit it, with production
  secrets in Replit Secrets. Otherwise production moves to a host such as Render, Fly.io or Neon. That decision comes
  from the Phase 0 audit, not from habit, and any move needs the owner's approval.

**AI tools and how quality is kept**

| Tool | Used for | Guardrail |
|---|---|---|
| Claude Code (Lead) | Implementing tickets, refactors, writing tests, a second-opinion review of PRs | Lead reads every diff; AI review gets the code, not my conclusion, so it doesn't just agree |
| Replit Agent | Scoped tickets inside the existing project | Branch only; reviewed PR; never production |
| ChatGPT (owner already uses it) | Keeping the master requirements current, drafting tickets and acceptance criteria, test checklists | Lead approves before a ticket is assigned |
| GitHub Copilot or Claude (TA) | Autocomplete, explaining unfamiliar code | TA must explain their PR line by line |

**Rules for all AI use**

- No real customer, driver or financial data and no secrets go into any AI tool.
- Every expected value in a money test is calculated independently, not copied from the code's output.
- AI help is noted in the PR description.

The broken-code challenge in this submission shows the workflow: AI drafted, a separate AI pass reviewed the code
cold, and I verified by hand. One AI-written test was wrong and was caught that way.

**Where AI speeds things up, and where it doesn't.** I expect AI to cut roughly 25-35% of pure coding time on CRUD,
screens and tests. It saves little on discovery, integration approvals, security review, accounting rules or user
acceptance. That's why the estimate doesn't take more than about 15-20% off overall.

## 3. Preventing unauthorized changes to production

1. **Branch protection on `main`.** Changes go through a pull request only. They need 1 approving review (the Lead's)
   and green CI to merge. Force-push and branch deletion are off. Admins follow the same rule.
2. **Releases need the owner.** Production deploys only from a tagged release, through the pipeline. The owner approves
   each production release in writing (an issue comment or chat), as the master sheet requires. Nobody deploys from a
   laptop or from Replit Agent.
3. **Separate environments.**
   - Dev, staging and production have separate databases and secrets.
   - Staging uses only synthetic data.
   - The TA has no production database or secrets access.
   - The Lead has break-glass access, with MFA, and every use is logged.
4. **Database safety.** Every migration is reviewed. A verified backup is taken right before it runs. Each migration
   has a written rollback. Nothing destructive goes out without a migration plan and the owner's OK.
5. **Account hygiene.** Named accounts with MFA everywhere (GitHub, Replit, host, Stripe, DNS), least privilege, and an
   offboarding checklist. When anyone leaves, their access is removed the same day.
6. **Detection.** The app keeps an audit log for important changes. The host keeps a deploy log, and Sentry tracks
   errors. Any production change that didn't come from a tagged release is treated as an incident.
7. **Paid and irreversible actions need the owner's explicit approval.** This covers enabling paid integrations,
   changing domains or DNS, migrating real data, and signing vendor agreements.

## 4. Bugs, missed deadlines and technical disagreements

**Bugs**

| Severity | Example | Response |
|---|---|---|
| S1 Critical | Data visible across companies, money wrong, production down | Drop everything. Contain first (feature flag or rollback). Tell the owner within the hour. Hotfix branch, with a regression test. Written post-mortem within 48 h |
| S2 High | A main workflow broken for some users | Fixed in the current week |
| S3 Normal | Something wrong with a workaround available | Scheduled into the next sprint |
| S4 Low | Cosmetic | Backlog |

Every bug gets the same treatment:

1. Reproduce it first.
2. Write a failing test.
3. Fix the root cause.
4. Keep the test, so the bug can't come back.

Bugs are triaged twice a week, and repeat patterns become checklist or CI rules.

**Missed deadlines**

- **Early warning.** A slip is raised as soon as it's visible, never on the due date. Each ticket carries an estimate,
  and actuals are tracked so estimates improve over time.
- **Options, not excuses.** When a milestone is at risk, the owner gets three choices with their trade-offs:
  - cut or defer scope
  - move the date
  - add help (and what it costs)

  The owner decides.
- **Repeated slips get a closer look.** If one area keeps slipping, I look for the cause: unclear requirements, a
  third-party dependency, or skills. Then I fix that cause, for example a discovery spike, pairing, or a specialist.

**Technical disagreements** (with the TA, a contractor or the owner)

1. Separate the facts from preferences. Where possible, settle it with a small spike, a benchmark or a test, not
   debate.
2. Write a one-page decision record: the options, the trade-offs, the cost, a recommendation. Time-box the discussion.
3. **Who decides:** the Lead makes technical decisions. The owner makes business, cost and vendor decisions. Once a
   decision is made, everyone commits to it, and the record notes what would make us revisit it.
4. Security, tenant isolation and financial correctness are not traded away to meet a date. If pressed, I'll offer to
   cut scope instead.

## 5. Progress reports to the business owner

- **Weekly written report** (one page, plain language, every Friday):
  - done this week, with links to the staging demo
  - next week's plan
  - blocked items and decisions needed from the owner
  - risks
  - hours used against plan, and spend against budget
  - the current **implemented / partial / simulated** feature list (master sheet B7)
- **Live demo every two weeks** on staging with synthetic data, about 30 minutes. The owner clicks through it
  themselves.
- **Milestone review** at the end of each phase:
  - acceptance tests walked through
  - test results and tenant-isolation evidence
  - known issues
  - the updated estimate for the remaining phases (re-forecast, never silently stretched)
  - go / no-go for the next phase
- **Immediate notice** of any S1 incident, security issue, or change to cost or timeline over 10%.
