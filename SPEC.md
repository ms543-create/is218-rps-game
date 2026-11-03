# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement `determine_winner(player, computer)` for all nine outcomes above, returning results from the player's perspective. Keep the supplied interface and server, with independent rounds and no score or saved history.
- Predicted example: the player chooses Rock and the computer chooses Paper; return `lose` and display **Computer wins**, because Paper covers Rock. This valid losing round is a positive case.
- Add nine explicit unit cases in `tests/test_game.py`, using literal expected results. Add a real request/result integration test that fixes only the computer choice and checks both moves and the result.
- Reuse supplied missing/unsupported-input integration tests. Missing input or an unsupported move such as `lizard` must return HTTP 400 with a helpful explanation, without calling the rules.
- Add a real Chromium round and replay in `tests/e2e/test_round.py`, using the supplied fixtures and real rules. Control only the computer choice and use Playwright waiting assertions.
- Run the full `.venv/bin/python check.py`, fix failures without weakening checks, and review the diff against this spec. Show the Rock-versus-Paper test for student discussion before personal browser review.
- Record actual checks, code/test links, and the student's browser observation in the work record. Preserve the issue link and add real PR/CI links when available. GitHub actions and merging require student approval; merging also requires passing final PR checks.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/ms543-create/is218-rps-game/issues/1).
- Pull request: [RPS-001: Play a round #2](https://github.com/ms543-create/is218-rps-game/pull/2).
- CI: [Python checks for the feature implementation](https://github.com/ms543-create/is218-rps-game/actions/runs/41670998920). Confirm the latest PR commit's Python checks pass before merging.
- Implementation: [game.py](game.py) implements all nine outcomes for one independent round using the supplied interface and server.
- Checks: Full `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium tests. [Rule and request tests](tests/test_game.py) cover all nine literal outcomes and a real Rock-versus-Paper submitted loss. [Browser round and replay](tests/e2e/test_round.py) checks Rock losing to Paper, then Scissors winning against Paper through real HTTP. [Supplied request tests](tests/test_shell.py) retain missing/unsupported-input rejection checks. Only the computer choice is fixed in the new integration/browser tests; the real rules run.
- Review: Compared the diff and both new test files against this spec; `git diff --check` passed. No shared check settings or supplied assertions were weakened.
- Personal browser review of completed rules: the student chose Scissors, the computer chose Scissors, and the site displayed a tie. Automated browser checks do not establish every aspect of usability or performance.
