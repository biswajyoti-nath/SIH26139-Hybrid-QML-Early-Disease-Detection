#!/usr/bin/env bash
# health_check.sh — Quick project health check for SIH 26139
# Run from project root: ./scripts/health_check.sh
# Exit code 0 = healthy. Non-zero = issues found.

set -uo pipefail

PASS=0
FAIL=0
WARN=0

pass()  { echo "  ✓ $1"; PASS=$((PASS+1)); }
fail()  { echo "  ✗ $1"; FAIL=$((FAIL+1)); }
warn()  { echo "  ⚠ $1"; WARN=$((WARN+1)); }
header(){ echo ""; echo "=== $1 ==="; }

header "MANDATORY FILES"
[ -f "AGENTS.md" ]          && pass "AGENTS.md exists"       || fail "AGENTS.md MISSING"
[ -f "PROJECT_STATE.md" ]   && pass "PROJECT_STATE.md exists" || fail "PROJECT_STATE.md MISSING"
[ -f "TASKS.md" ]           && pass "TASKS.md exists"         || fail "TASKS.md MISSING"
[ -f "DECISIONS.md" ]       && pass "DECISIONS.md exists"     || fail "DECISIONS.md MISSING"
[ -f "EXPERIMENT_LOG.md" ]  && pass "EXPERIMENT_LOG.md exists"|| fail "EXPERIMENT_LOG.md MISSING"
[ -f "README.md" ]          && pass "README.md exists"        || fail "README.md MISSING"
[ -f ".gitignore" ]         && pass ".gitignore exists"       || fail ".gitignore MISSING"

header "AGENT FILES"
[ -f "agents/EVALUATOR.md" ]      && pass "EVALUATOR.md"      || fail "EVALUATOR.md MISSING"
[ -f "agents/RESEARCHER.md" ]     && pass "RESEARCHER.md"     || fail "RESEARCHER.md MISSING"
[ -f "agents/ENGINEER.md" ]       && pass "ENGINEER.md"       || fail "ENGINEER.md MISSING"
[ -f "agents/EXPERIMENTALIST.md" ]&& pass "EXPERIMENTALIST.md"|| fail "EXPERIMENTALIST.md MISSING"
[ -f "agents/JUDGE.md" ]          && pass "JUDGE.md"          || fail "JUDGE.md MISSING"
[ -f "agents/SESSION_PROTOCOL.md" ]&& pass "SESSION_PROTOCOL.md"|| fail "SESSION_PROTOCOL.md MISSING"

header "RESEARCH DOCS"
[ -f "docs/PROJECT_KNOWLEDGE.md" ]    && pass "PROJECT_KNOWLEDGE.md"  || fail "PROJECT_KNOWLEDGE.md MISSING"
[ -f "docs/RESEARCH_LOG.md" ]         && pass "RESEARCH_LOG.md"        || fail "RESEARCH_LOG.md MISSING"
[ -f "docs/CLAIMS_LEDGER.md" ]        && pass "CLAIMS_LEDGER.md"       || fail "CLAIMS_LEDGER.md MISSING"
[ -f "docs/TECH_STACK.md" ]           && pass "TECH_STACK.md"          || fail "TECH_STACK.md MISSING"
[ -f "docs/EXPERIMENT_PROTOCOL.md" ]  && pass "EXPERIMENT_PROTOCOL.md" || fail "EXPERIMENT_PROTOCOL.md MISSING"
[ -f "docs/SOFTWARE_ARCHITECTURE.md" ]&& pass "SOFTWARE_ARCHITECTURE.md"|| fail "SOFTWARE_ARCHITECTURE.md MISSING"
[ -f "docs/DEMO_SPECIFICATION.md" ]   && pass "DEMO_SPECIFICATION.md"  || fail "DEMO_SPECIFICATION.md MISSING"
[ -f "docs/OPEN_QUESTIONS.md" ]       && pass "OPEN_QUESTIONS.md"      || fail "OPEN_QUESTIONS.md MISSING"

header "GIT STATUS"
if git rev-parse --git-dir > /dev/null 2>&1; then
    pass "Git repository initialized"
    COMMIT_COUNT=$(git log --oneline 2>/dev/null | wc -l | tr -d ' ')
    [ "$COMMIT_COUNT" -gt 0 ] && pass "Git has $COMMIT_COUNT commits" || warn "No commits yet"
    UNTRACKED=$(git status --porcelain 2>/dev/null | grep '^?' | wc -l | tr -d ' ')
    [ "$UNTRACKED" -eq 0 ] && pass "No untracked files" || warn "$UNTRACKED untracked file(s)"
    DIRTY=$(git status --porcelain 2>/dev/null | grep -v '^?' | wc -l | tr -d ' ')
    [ "$DIRTY" -eq 0 ] && pass "Working tree clean" || warn "$DIRTY uncommitted change(s)"
else
    fail "Not a git repository"
fi

header "PYTHON ENVIRONMENT"
if [ -d ".venv" ]; then
    pass ".venv directory exists"
    PYTHON_BIN=".venv/bin/python"
    if [ -f "$PYTHON_BIN" ]; then
        PY_VERSION=$("$PYTHON_BIN" --version 2>&1)
        pass "Python: $PY_VERSION"
        # Check key packages
        for pkg in sklearn xgboost shap fastapi uvicorn numpy; do
            "$PYTHON_BIN" -c "import $pkg" 2>/dev/null \
                && pass "$pkg importable" \
                || fail "$pkg NOT importable"
        done
        # Quantum packages
        for pkg in pennylane; do
            "$PYTHON_BIN" -c "import $pkg" 2>/dev/null \
                && pass "$pkg importable" \
                || warn "$pkg not installed (required for quantum experiments)"
        done
    else
        fail ".venv/bin/python not found"
    fi
else
    warn ".venv not created yet (run: python3.12 -m venv .venv)"
fi

header "BACKEND"
if [ -d "backend" ]; then
    pass "backend/ directory exists"
    [ -f "backend/requirements.txt" ] && pass "requirements.txt exists" || warn "requirements.txt not yet created"
    [ -f "backend/__init__.py" ] && pass "backend/__init__.py exists" || warn "backend/__init__.py not yet created"
else
    warn "backend/ not yet created (T-011)"
fi

header "FRONTEND"
if [ -d "frontend" ]; then
    pass "frontend/ directory exists"
    [ -f "frontend/package.json" ] && pass "package.json exists" || warn "package.json not yet created"
    [ -d "frontend/node_modules" ] && pass "node_modules exists" || warn "npm install not run yet"
else
    warn "frontend/ not yet created (T-012)"
fi

header "EXPERIMENT INFRASTRUCTURE"
[ -d "experiments/configs" ]   && pass "experiments/configs exists"   || fail "experiments/configs MISSING"
[ -d "experiments/results" ]   && pass "experiments/results exists"   || fail "experiments/results MISSING"
[ -d "experiments/logs" ]      && pass "experiments/logs exists"      || fail "experiments/logs MISSING"
[ -d "experiments/artifacts" ] && pass "experiments/artifacts exists" || fail "experiments/artifacts MISSING"

echo ""
echo "=============================="
echo "HEALTH CHECK SUMMARY"
echo "  PASS: $PASS"
echo "  WARN: $WARN"
echo "  FAIL: $FAIL"
echo "=============================="

if [ "$FAIL" -gt 0 ]; then
    echo "STATUS: ❌ UNHEALTHY — $FAIL critical issue(s)"
    exit 1
elif [ "$WARN" -gt 0 ]; then
    echo "STATUS: ⚠ PARTIAL — $WARN warning(s) (expected for early phases)"
    exit 0
else
    echo "STATUS: ✓ HEALTHY"
    exit 0
fi
