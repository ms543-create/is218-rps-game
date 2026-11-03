"""Real rule outcomes and submitted-round behavior for RPS-001."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_nine_outcomes(player, computer, expected):
    """Each literal matchup returns the result from the player's perspective."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_submitted_rock_loses_to_paper(monkeypatch):
    """A real submitted round displays the predicted loss and both choices."""
    monkeypatch.setitem(web.app.config, "TESTING", True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'data-outcome="lose"' in page
    assert '<h2 id="game-heading">Computer wins</h2>' in page
    assert '<p class="choice-label">You chose</p><p class="choice-value">Rock ' in page
    assert (
        '<p class="choice-label">Computer chose</p><p class="choice-value">Paper '
        in page
    )
    assert "game rules not built yet" not in page
