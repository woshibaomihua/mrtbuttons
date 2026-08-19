# MRT Buttons Daily SEO/GEO Growth Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create one stateful Codex Heartbeat that runs every day at 07:30 Asia/Shanghai, produces an evidence-backed MRT Buttons growth report, and only modifies or deploys the site when approved decision gates are satisfied.

**Architecture:** The automation is attached to the current Codex task so it retains the site's working context and remains the sole recurring writer. Local JSON stores non-sensitive run state, daily Markdown reports provide the user-visible history, and the canonical site repository is only touched after coordination, evidence, validation, and deployment gates pass.

**Tech Stack:** Codex Heartbeat automation, PowerShell 7, Git, static HTML/JSON-LD/XML/JavaScript, Chrome CDP 9230 for authenticated GSC access, Formspree, IndexNow, GitHub and Vercel.

## Global Constraints

- Canonical site source is exactly `E:\Claude\mrtbuttons` on branch `main`.
- Never use obsolete `merittrimssite`, `sitegen.py`, or any `gen_*.py` generator.
- Read `E:\Claude\COORDINATION.md` before any write and stop on overlapping MRT Buttons work.
- Run the Heartbeat at 07:30 in `Asia/Shanghai`, not at 07:30 in the machine's `America/Los_Angeles` timezone.
- P0 and evidence-backed P1 existing-page fixes may be implemented automatically; P2 new content, new factual claims, external publishing, directory submissions, account mutations and paid actions require user confirmation.
- No fresh evidence means No-op: do not edit, commit, deploy, change `lastmod`, submit IndexNow or request Google indexing.
- IndexNow only receives added, materially changed, deleted or moved URLs; HTTP 200 means accepted, not indexed.
- Google Request Indexing is only for a few new or materially changed high-priority URLs and is never repeated to accelerate an unchanged URL.
- All site deployments use `E:\Claude\_lib\deploy.ps1 -Site mrtbuttons`; only literal `DEPLOY_OK` proves success.
- Reports go to `E:\Codex\codex_finish\MRT Buttons每日增长`; machine state goes to `E:\Codex\workspace\mrtbuttons-growth-monitor`.
- Store no passwords, cookies, API tokens, Formspree submissions, customer messages or other customer personal data in the state or reports.
- The approved design is `docs/superpowers/specs/2026-08-19-mrtbuttons-daily-growth-loop-design.md`.

---

## File and Service Map

| Component | Responsibility |
|---|---|
| `E:\Codex\workspace\mrtbuttons-growth-monitor\state.json` | Last successful run, data cutoff, handled opportunities, submission history, unresolved issues and pending approvals; no secrets |
| `E:\Codex\codex_finish\MRT Buttons每日增长\YYYY-MM-DD-MRT-Buttons增长日报.md` | Daily user-facing evidence, actions, results and next target |
| Codex Heartbeat `MRT Buttons 每日SEO/GEO增长闭环` | Schedule and execute the approved decision flow in the current task |
| `E:\Claude\mrtbuttons` | Canonical site source; modified only for approved P0/P1 actions |
| `E:\Claude\COORDINATION.md` | Cross-agent write lock and completion log |
| Chrome CDP 9230 | Reuse authenticated GSC state without bypassing login, CAPTCHA or risk controls |

---

### Task 1: Establish the Non-Sensitive State Contract

**Files:**
- Create: `E:\Codex\workspace\mrtbuttons-growth-monitor\state.json`
- Reference: `docs/superpowers/specs/2026-08-19-mrtbuttons-daily-growth-loop-design.md`

**Interfaces:**
- Consumes: approved paths, schedule and decision gates from the design spec.
- Produces: one JSON object with `schema_version: 1` that every Heartbeat run can read and atomically replace.

- [ ] **Step 1: Verify the state file does not already exist**

Run:

```powershell
$state = 'E:\Codex\workspace\mrtbuttons-growth-monitor\state.json'
if (Test-Path -LiteralPath $state) { throw "State already exists and must be reviewed before overwrite: $state" }
Write-Output 'STATE_ABSENT_OK'
```

Expected: `STATE_ABSENT_OK`. If the file exists, read it and preserve compatible historical fields rather than overwriting it.

- [ ] **Step 2: Create the directory and initial state with apply_patch**

Create exactly this JSON, with JSON `null` representing “no completed run yet” rather than an unresolved placeholder:

```json
{
  "schema_version": 1,
  "site": "mrtbuttons",
  "canonical_root": "E:\\Claude\\mrtbuttons",
  "timezone": "Asia/Shanghai",
  "schedule_local_time": "07:30",
  "last_success_at": null,
  "last_data_cutoff": null,
  "last_gsc_window": null,
  "handled_opportunities": [],
  "recent_google_index_requests": [],
  "recent_indexnow_urls": [],
  "last_deployed_commit": "36f809eeda91cbe40ad1152a2c835b0a6351bfee",
  "unresolved": [],
  "pending_approvals": [],
  "last_report_path": null
}
```

- [ ] **Step 3: Validate JSON shape and secret exclusion**

Run:

```powershell
$state = 'E:\Codex\workspace\mrtbuttons-growth-monitor\state.json'
$obj = Get-Content -LiteralPath $state -Raw -Encoding UTF8 | ConvertFrom-Json
$required = @('schema_version','site','canonical_root','timezone','schedule_local_time','last_success_at','last_data_cutoff','last_gsc_window','handled_opportunities','recent_google_index_requests','recent_indexnow_urls','last_deployed_commit','unresolved','pending_approvals','last_report_path')
$missing = @($required | Where-Object { -not $obj.PSObject.Properties.Name.Contains($_) })
$forbidden = Select-String -LiteralPath $state -Pattern 'password|cookie|token|secret|form_submission|customer_message' -CaseSensitive:$false
if ($obj.schema_version -ne 1 -or $obj.site -ne 'mrtbuttons' -or $obj.timezone -ne 'Asia/Shanghai' -or $missing.Count -or $forbidden) { throw 'STATE_CONTRACT_FAIL' }
Write-Output 'STATE_CONTRACT_OK'
```

Expected: `STATE_CONTRACT_OK`.

---

### Task 2: Produce the Day-Zero Read-Only Baseline

**Files:**
- Create: `E:\Codex\codex_finish\MRT Buttons每日增长\2026-08-19-MRT-Buttons增长日报.md`
- Modify: `E:\Codex\workspace\mrtbuttons-growth-monitor\state.json`
- Read: `E:\Claude\mrtbuttons\robots.txt`
- Read: `E:\Claude\mrtbuttons\sitemap.xml`
- Read: `E:\Claude\mrtbuttons\contact.html`
- Read: `E:\Claude\mrtbuttons\assets\js\main.js`

**Interfaces:**
- Consumes: Task 1 state contract, canonical repository, production URLs and optional authenticated GSC data.
- Produces: one baseline report with fixed headings and an updated `last_success_at`, `last_data_cutoff`, `last_gsc_window`, `unresolved`, `last_report_path` and observed `last_deployed_commit`.

- [ ] **Step 1: Assert that the baseline report is not being silently overwritten**

Run:

```powershell
$report = 'E:\Codex\codex_finish\MRT Buttons每日增长\2026-08-19-MRT-Buttons增长日报.md'
if (Test-Path -LiteralPath $report) { throw "Baseline report already exists and must be reviewed: $report" }
Write-Output 'BASELINE_REPORT_ABSENT_OK'
```

Expected: `BASELINE_REPORT_ABSENT_OK`.

- [ ] **Step 2: Run source and production health checks without mutation**

Run from `E:\Claude\mrtbuttons`:

```powershell
git fetch origin
$local = git rev-parse HEAD
$origin = git rev-parse origin/main
$dirty = @(git status --porcelain)
[xml]$sitemap = Get-Content -LiteralPath sitemap.xml -Raw -Encoding UTF8
$ns = New-Object Xml.XmlNamespaceManager($sitemap.NameTable)
$ns.AddNamespace('sm','http://www.sitemaps.org/schemas/sitemap/0.9')
$urls = @($sitemap.SelectNodes('//sm:loc',$ns) | ForEach-Object { $_.InnerText })
$results = @($urls | ForEach-Object -Parallel {
  try {
    $r = Invoke-WebRequest -Uri $_ -UseBasicParsing -TimeoutSec 60 -Headers @{ 'Cache-Control'='no-cache' }
    [pscustomobject]@{ url=$_; status=[int]$r.StatusCode; old_email=$r.Content.Contains('mrtmaggie0010@gmail.com'); new_email=$r.Content.Contains('maggie@merittrims.com') }
  } catch {
    [pscustomobject]@{ url=$_; status=0; old_email=$false; new_email=$false; error=$_.Exception.Message }
  }
} -ThrottleLimit 8)
$bad = @($results | Where-Object { $_.status -ne 200 -or $_.old_email -or -not $_.new_email })
$robots = (Invoke-WebRequest -Uri 'https://mrtbuttons.com/robots.txt' -UseBasicParsing -TimeoutSec 60).Content
$bots = @('Googlebot','OAI-SearchBot','GPTBot','ClaudeBot','PerplexityBot')
$missingBots = @($bots | Where-Object { -not $robots.Contains($_) })
$formFiles = @('index.html','contact.html','instant-quote.html')
$formCount = 0
foreach ($f in $formFiles) { $formCount += ([regex]::Matches((Get-Content -LiteralPath $f -Raw -Encoding UTF8),'https://formspree\.io/f/xykrervj')).Count }
[pscustomobject]@{
  local=$local
  origin=$origin
  dirty_count=$dirty.Count
  sitemap_urls=$urls.Count
  production_failures=$bad.Count
  missing_bots=$missingBots.Count
  formspree_forms=$formCount
} | ConvertTo-Json
```

Expected baseline gates: local equals origin, or local is ahead only by the approved design/plan commits; `dirty_count=0`, `sitemap_urls=32`, `production_failures=0`, `missing_bots=0`, and `formspree_forms=3`. Record approved documentation-only commits explicitly rather than treating them as foreign work.

- [ ] **Step 3: Check authenticated sources without bypassing login**

1. Query `http://127.0.0.1:9230/json/version` and `/json/list`.
2. Treat a listening port without an active target as unavailable.
3. If GSC is logged in, read `sc-domain:mrtbuttons.com`, record the latest complete data date, 28-day totals, previous 28-day totals, query/page opportunities and indexing coverage.
4. If login is missing, add `GSC_LOGIN_REQUIRED` to `unresolved` and continue.
5. Do not submit indexing requests during the baseline run.
6. Record Formspree recipient verification and GA4 Measurement ID as `EXTERNAL_VERIFICATION_REQUIRED` unless account-side evidence is visible.

- [ ] **Step 4: Create the baseline report from observed values**

Create Markdown with these exact headings and factual output rules:

```markdown
# MRT Buttons 增长日报 · 2026-08-19

## 今日一句话结论
State whether the baseline is healthy, degraded, or blocked, naming the highest-priority issue.

## 数据截止日期
State the GSC cutoff date, or state that authenticated GSC data was unavailable.

## GSC、收录与关键词变化
Record observed totals and opportunities; do not infer changes without comparable periods.

## 生产、表单与AI爬虫健康度
Record the 32-URL production result, Formspree endpoint count, email parity and crawler access.

## 今日自动完成的修改
Write “Day-zero baseline: no site mutation” unless a P0 was actually discovered and separately authorized by the approved gate.

## 提交、部署与生产验证证据
Record commit parity and state that no deployment or indexing submission occurred during the read-only baseline.

## 等待确认的候选或外部动作
List Formspree, GA4, new content and external publication dependencies separately.

## 明日继续观察
List no more than three evidence-based targets.
```

Replace the English instructions with observed Chinese findings; do not leave them in the final report.

- [ ] **Step 5: Update state atomically and validate the report**

Set `last_success_at` to the actual ISO 8601 Beijing timestamp, update observed fields, and set `last_report_path` to the exact report path. Then run:

```powershell
$report = 'E:\Codex\codex_finish\MRT Buttons每日增长\2026-08-19-MRT-Buttons增长日报.md'
$requiredHeadings = @('今日一句话结论','数据截止日期','GSC、收录与关键词变化','生产、表单与AI爬虫健康度','今日自动完成的修改','提交、部署与生产验证证据','等待确认的候选或外部动作','明日继续观察')
$text = Get-Content -LiteralPath $report -Raw -Encoding UTF8
$missing = @($requiredHeadings | Where-Object { -not $text.Contains("## $_") })
$state = Get-Content -LiteralPath 'E:\Codex\workspace\mrtbuttons-growth-monitor\state.json' -Raw -Encoding UTF8 | ConvertFrom-Json
if ($missing.Count -or $state.last_report_path -ne $report -or -not $state.last_success_at) { throw 'BASELINE_REPORT_FAIL' }
Write-Output 'BASELINE_REPORT_OK'
```

Expected: `BASELINE_REPORT_OK`.

---

### Task 3: Create the Single Daily Heartbeat

**Services:**
- Create: Codex Heartbeat named `MRT Buttons 每日SEO/GEO增长闭环`
- Target: current Codex task/thread
- Schedule: daily at 07:30 `Asia/Shanghai`
- Destination: local

**Interfaces:**
- Consumes: Task 1 state file, Task 2 report contract, approved design, canonical repository and authenticated tools when available.
- Produces: one active Heartbeat with no duplicate MRT Buttons automation.

- [ ] **Step 1: Prove no matching active or paused automation exists**

Run:

```powershell
$roots = @('E:\Codex\.codex\automations','C:\Users\Jacken\.codex\automations')
$matches = @()
foreach ($root in $roots) {
  if (Test-Path -LiteralPath $root) {
    $matches += @(rg -l -i 'MRT Buttons 每日SEO/GEO增长闭环|mrtbuttons.*每日.*增长' $root -g 'automation.toml')
  }
}
if ($matches.Count) { $matches; throw 'DUPLICATE_AUTOMATION_FOUND' }
Write-Output 'NO_DUPLICATE_AUTOMATION'
```

Expected: `NO_DUPLICATE_AUTOMATION`.

- [ ] **Step 2: Create one Heartbeat with the exact approved prompt**

Use the Codex automation tool in create mode, kind `heartbeat`, local destination, active status, current task target and a daily 07:30 Asia/Shanghai schedule. Use this prompt verbatim:

```text
你负责 MRT Buttons（https://mrtbuttons.com）的每日 SEO、收录、GEO/AEO、AI 推荐与询盘健康闭环。每天按北京时间运行一次。先读取 E:\Claude\mrtbuttons\docs\superpowers\specs\2026-08-19-mrtbuttons-daily-growth-loop-design.md，再读取 E:\Codex\workspace\mrtbuttons-growth-monitor\state.json；两者是本任务的行为和状态契约。

唯一站点正源是 E:\Claude\mrtbuttons，分支 main。禁止使用旧 merittrimssite，禁止运行 sitegen.py 或任何 gen_*.py。每次先读取 E:\Claude\_lib\sites.json 与 E:\Claude\COORDINATION.md，git fetch 并检查 HEAD、origin/main、工作区和协作冲突。工作区存在不属于本任务的改动、远端领先或有人认领重叠范围时，不写文件、不提交、不部署，只报告冲突。

每天先做只读检查：sitemap 中 canonical URL 的生产 HTTP 与正文、robots、sitemap、canonical、H1、JSON-LD、内链、图片、Formspree xykrervj、maggie@merittrims.com、WhatsApp、电话、main.js 回退，以及 Googlebot、OAI-SearchBot、GPTBot、ClaudeBot、PerplexityBot 的可访问性。检查 Chrome CDP 9230 的 /json/version 和 /json/list；监听端口不等于已登录。仅在现有登录状态有效时读取正确 GSC 属性 sc-domain:mrtbuttons.com，绝不绕过登录、验证码、风控、密码或配额。GSC 延迟时使用最后一个完整日期并明确截止日。

按北京时间星期选择主任务：周一比较最近完整 28 天与上一周期，筛排名 4–20、低 CTR、新查询和索引变化，只保留本周 3 个目标；周二最多优化 1 个已有 GSC 机会页；周三检查实体一致性、可引用答案和有证据的 GEO/AI 推荐差距；周四检查 Formspree、WhatsApp、邮箱、CTA、归因和手机询盘体验；周五治理未收录页、孤立页、重复意图和旧内容；周六研究买家问题、Reddit/SERP 话题，只生成候选和证据清单；周日输出周报与下周 3 个目标，无 P0 不改站。月度首个可用运行日做固定 20 问 AI 提及/引用基线和月度 GSC 对比；平台不可访问时记录限制，不伪造测试结果。

持续跟踪已批准的 30/60/90 天目标：30 天内完成生产/表单/邮箱/robots/sitemap/canonical 健康基线、Formspree 新邮箱验证、获得真实 GA4 ID 后验证五类事件、GSC 有效索引覆盖运营目标不低于 95%，并建立非品牌词、品牌词、询盘来源和 AI 提及基线；60 天内按 GSC 证据优化 4–8 个已有页面、形成至少 4 个经过关键词冲突检查且等待确认的内容候选、保持孤立页/错误 canonical/无效 schema 为 0，并完成两轮一次只改一个变量的询盘路径检查；90 天以非品牌曝光月环比增长 10% 为运营目标，争取 30% 的已选排名 4–20 机会词在 28 天内提升至少 3 位或 CTR 相对提升至少 20%，保持有效索引覆盖 95% 以上，完成每月固定 20 问 AI 测试并争取至少 2 次有效品牌提及或本站引用。所有数字都是运营目标，不是排名或收录承诺；失败时保留基线、外部限制和下一假设，不得改口径制造达成。

决策必须分级：P0 是生产 5xx、关键页不可访问、表单失效、robots/noindex 误封、邮箱或主要询盘入口错误，可做最小修复；P1 是 GSC 或生产证据明确指向的现有页面问题，且不需要新增未经核验事实，可自动优化现有 title/meta、可见答案、内链和 schema 一致性；P2 是新页面、新博客、新数字、认证、客户/产能/价格/交期事实、Reddit/LinkedIn/目录站发布、账号配置和付费动作，只生成候选并等待用户确认。没有新证据就是 No-op：不得为了日报而修改、提交、部署、改 lastmod、推 IndexNow 或请求 Google 索引。

如需改站，先在 COORDINATION.md 认领精确范围，只做与证据直接相关的最小改动。不得编造价格、评分、库存、认证、客户、MOQ、交期、产能或统计。验证 HTML、JSON-LD、sitemap XML、JavaScript、canonical/H1、可见 FAQ 与 schema、内链、图片、CTA、桌面和 390px 手机、控制台、Git diff。只用 E:\Claude\_lib\deploy.ps1 -Site mrtbuttons 部署；只有字面值 DEPLOY_OK 才能报告成功。部署后读取生产正文验证，不只看 HTTP 200。IndexNow 只提交新增、实质更新、删除或迁移 URL；HTTP 200 只表示接收。Google Request Indexing 仅用于少量新增或实质更新的高优先级 URL，同一未变化 URL 不重复请求，加入队列不等于已收录。

每天在当前任务回复中文日报，并保存到 E:\Codex\codex_finish\MRT Buttons每日增长\YYYY-MM-DD-MRT-Buttons增长日报.md。固定八段：今日一句话结论；数据截止日期；GSC、收录与关键词变化；生产、表单与AI爬虫健康度；今日自动完成的修改；提交、部署与生产验证证据；等待确认的候选或外部动作；明日继续观察。当天无高价值动作时明确写“今日不改站”。只保留明日最多 3 个目标。

每次成功后原子更新 E:\Codex\workspace\mrtbuttons-growth-monitor\state.json 的 `last_success_at`、`last_data_cutoff`、`last_gsc_window`、`handled_opportunities`、`recent_google_index_requests`、`recent_indexnow_urls`、`last_deployed_commit`、`unresolved`、`pending_approvals` 和 `last_report_path`。不得写入密码、Cookie、Token、表单提交正文或客户隐私。相同阻塞连续 3 次后升级为醒目阻塞项并请求用户处理必要登录或事实确认。
```

- [ ] **Step 3: Read the created automation back from the automation service**

Use automation view mode with the returned automation ID. Verify all of the following from the tool response rather than assuming creation succeeded:

- kind is Heartbeat;
- status is active;
- target is the current task;
- schedule is daily at 07:30 Asia/Shanghai;
- name exactly equals `MRT Buttons 每日SEO/GEO增长闭环`;
- prompt contains the canonical root, state path, report path, `sc-domain:mrtbuttons.com`, P0/P1/P2/No-op, `DEPLOY_OK`, IndexNow and the no-generator rule.

Expected: one matching active automation and zero duplicates.

---

### Task 4: Synchronize Documentation and Close the Acceptance Loop

**Files:**
- Modify: `E:\Claude\COORDINATION.md`
- Existing commits: `a2a02f4` design commit plus the implementation-plan commit created before execution.
- Production check: `https://mrtbuttons.com/`, `/contact`, `/sitemap.xml`, `/robots.txt`, `/llms.txt`.

**Interfaces:**
- Consumes: Tasks 1–3 artifacts and the canonical repository history.
- Produces: repository/remote alignment, coordination receipt and final evidence that the automation exists without altering indexed page content.

- [ ] **Step 1: Commit this implementation plan before execution**

Run:

```powershell
git add -- docs/superpowers/plans/2026-08-19-mrtbuttons-daily-growth-loop.md
git diff --cached --check
git commit -m 'docs: plan daily SEO growth automation' -m 'Co-Authored-By: Codex <562790186@qq.com>'
```

Expected: one new documentation commit and a clean working tree.

- [ ] **Step 2: Push approved documentation through the unified deployment gate**

Run:

```powershell
$msg = "docs: publish daily growth automation design`n`nCo-Authored-By: Codex <562790186@qq.com>"
& 'E:\Claude\_lib\deploy.ps1' -Site mrtbuttons -Message $msg
```

Expected: all configured production URLs return 200 and the terminal ends with literal `DEPLOY_OK`. Do not change sitemap `lastmod` because no indexed page content changed.

- [ ] **Step 3: Verify production content remained unchanged**

Run:

```powershell
$urls = @(
  'https://mrtbuttons.com/',
  'https://mrtbuttons.com/contact',
  'https://mrtbuttons.com/sitemap.xml',
  'https://mrtbuttons.com/robots.txt',
  'https://mrtbuttons.com/llms.txt'
)
$results = foreach ($url in $urls) {
  $r = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 60 -Headers @{ 'Cache-Control'='no-cache' }
  [pscustomobject]@{ url=$url; status=[int]$r.StatusCode; old_email=$r.Content.Contains('mrtmaggie0010@gmail.com') }
}
$bad = @($results | Where-Object { $_.status -ne 200 -or $_.old_email })
if ($bad.Count) { $bad; throw 'PRODUCTION_REGRESSION' }
Write-Output 'PRODUCTION_UNCHANGED_OK'
```

Expected: `PRODUCTION_UNCHANGED_OK`.

- [ ] **Step 4: Move the coordination row from Active to Done**

Record the two documentation commits, active Heartbeat name/timezone, state/report paths, baseline result, `DEPLOY_OK`, repository parity and the fact that no indexed page content or sitemap date changed.

- [ ] **Step 5: Run final acceptance checks**

Verify:

```powershell
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
Get-Content -LiteralPath 'E:\Codex\workspace\mrtbuttons-growth-monitor\state.json' -Raw -Encoding UTF8 | ConvertFrom-Json | Out-Null
Test-Path -LiteralPath 'E:\Codex\codex_finish\MRT Buttons每日增长\2026-08-19-MRT-Buttons增长日报.md'
```

Then view the automation one final time. Acceptance requires a clean `main`, local/remote commit equality, valid JSON state, existing baseline report, one active Heartbeat, daily 07:30 Asia/Shanghai schedule, current task target and no duplicate MRT Buttons growth automation.

---

## Plan Self-Review Checklist

- [x] Every design section 1–14 maps to a task or Global Constraint.
- [x] No unresolved placeholder or unspecified error-handling instruction remains.
- [x] State field names are identical in Tasks 1, 2 and the Heartbeat prompt.
- [x] Report headings are identical in Task 2 and the Heartbeat prompt.
- [x] Automation name, schedule, timezone, source path, GSC property and deployment command are identical throughout.
- [x] No step authorizes new factual claims, new content publishing, external posting, paid spend or login bypass.
