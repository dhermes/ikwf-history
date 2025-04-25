// Copyright (c) 2025 - Present. IKWF History. All rights reserved.

const BRACKET_INFO = {
  description: null,
  wrestlerChoices: [
    { id: 0, name: "Wrestler 1", team: "Team 1" },
    { id: 1, name: "Wrestler 2", team: "Team 2" },
    { id: 2, name: "Wrestler 3", team: "Team 3" },
    { id: 3, name: "Wrestler 4", team: "Team 4" },
    { id: 4, name: "Wrestler 5", team: "Team 5" },
    { id: 5, name: "Wrestler 6", team: "Team 6" },
    { id: 6, name: "Wrestler 7", team: "Team 7" },
    { id: 7, name: "Wrestler 8", team: "Team 8" },
    { id: 8, name: "Wrestler 9", team: "Team 9" },
    { id: 9, name: "Wrestler 10", team: "Team 10" },
    { id: 10, name: "Wrestler 11", team: "Team 11" },
    { id: 11, name: "Wrestler 12", team: "Team 12" },
    { id: 12, name: "Wrestler 13", team: "Team 13" },
    { id: 13, name: "Wrestler 14", team: "Team 14" },
    { id: 14, name: "Wrestler 15", team: "Team 15" },
    { id: 15, name: "Wrestler 16", team: "Team 16" },
    { id: 16, name: "Wrestler 17", team: "Team 17" },
    { id: 17, name: "Wrestler 18", team: "Team 18" },
    { id: 18, name: "Wrestler 19", team: "Team 19" },
    { id: 19, name: "Wrestler 20", team: "Team 20" },
    { id: 20, name: "Wrestler 21", team: "Team 21" },
    { id: 21, name: "Wrestler 22", team: "Team 22" },
    { id: 22, name: "Wrestler 23", team: "Team 23" },
    { id: 23, name: "Wrestler 24", team: "Team 24" },
  ],
  matches: {
    1: {
      top: { choice: 0, choices: [0] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    2: {
      top: { choice: 1, choices: [1] },
      bottom: { choice: 2, choices: [2] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    3: {
      top: { choice: 3, choices: [3] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    4: {
      top: { choice: 4, choices: [4] },
      bottom: { choice: 5, choices: [5] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    5: {
      top: { choice: 6, choices: [6] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    6: {
      top: { choice: 7, choices: [7] },
      bottom: { choice: 8, choices: [8] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    7: {
      top: { choice: 9, choices: [9] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    8: {
      top: { choice: 10, choices: [10] },
      bottom: { choice: 11, choices: [11] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    9: {
      top: { choice: 12, choices: [12] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    10: {
      top: { choice: 13, choices: [13] },
      bottom: { choice: 14, choices: [14] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    11: {
      top: { choice: 15, choices: [15] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    12: {
      top: { choice: 16, choices: [16] },
      bottom: { choice: 17, choices: [17] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    13: {
      top: { choice: 18, choices: [18] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    14: {
      top: { choice: 19, choices: [19] },
      bottom: { choice: 20, choices: [20] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    15: {
      top: { choice: 21, choices: [21] },
      bottom: { choice: null, choices: [] },
      winner: "top",
      boutNumber: null,
      result: "",
    },
    16: {
      top: { choice: 22, choices: [22] },
      bottom: { choice: 23, choices: [23] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    17: {
      top: { choice: 0, choices: [0] },
      bottom: { choice: null, choices: [1, 2] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    18: {
      top: { choice: 3, choices: [3] },
      bottom: { choice: null, choices: [4, 5] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    19: {
      top: { choice: 6, choices: [6] },
      bottom: { choice: null, choices: [7, 8] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    20: {
      top: { choice: 9, choices: [9] },
      bottom: { choice: null, choices: [10, 11] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    21: {
      top: { choice: 12, choices: [12] },
      bottom: { choice: null, choices: [13, 14] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    22: {
      top: { choice: 15, choices: [15] },
      bottom: { choice: null, choices: [16, 17] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    23: {
      top: { choice: 18, choices: [18] },
      bottom: { choice: null, choices: [19, 20] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    24: {
      top: { choice: 21, choices: [21] },
      bottom: { choice: null, choices: [22, 23] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    // 25-32 (consolation) absent in earlier years
    33: {
      top: { choice: null, choices: [0] },
      bottom: { choice: null, choices: [3] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    34: {
      top: { choice: null, choices: [6] },
      bottom: { choice: null, choices: [9] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    35: {
      top: { choice: null, choices: [12] },
      bottom: { choice: null, choices: [15] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    36: {
      top: { choice: null, choices: [18] },
      bottom: { choice: null, choices: [21] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    37: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    38: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    39: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    40: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    41: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    42: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    43: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    44: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    45: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    46: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    47: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    48: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    49: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    50: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    // 51 (7th place) absent in earlier years
    52: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    53: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    54: {
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    // Below are "synthetic" match IDs used to select place match winners
    1001: {
      // First place
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    1003: {
      // Third place
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
    1005: {
      // Fifth place
      top: { choice: null, choices: [] },
      bottom: { choice: null, choices: [] },
      winner: null,
      boutNumber: null,
      result: "",
    },
  },
};
const STORAGE_KEY = "manualEntrySerialized.3cd4823b";
const PREVIOUS_MATCH_MAP = Object.freeze({
  17: { bottom: 2 },
  18: { bottom: 4 },
  19: { bottom: 6 },
  20: { bottom: 8 },
  21: { bottom: 10 },
  22: { bottom: 12 },
  23: { bottom: 14 },
  24: { bottom: 16 },
  33: { top: 17, bottom: 18 },
  34: { top: 19, bottom: 20 },
  35: { top: 21, bottom: 22 },
  36: { top: 23, bottom: 24 },
  41: { bottom: 37 },
  42: { top: 38 },
  43: { bottom: 39 },
  44: { top: 40 },
  45: { top: 33, bottom: 34 },
  46: { top: 35, bottom: 36 },
  47: { top: 41, bottom: 42 },
  48: { top: 43, bottom: 44 },
  49: { bottom: 47 },
  50: { top: 48 },
  53: { top: 49, bottom: 50 },
  54: { top: 45, bottom: 46 },
  1001: { top: 54 },
  1003: { top: 53 },
  1005: { top: 52 },
});
const WIN_MATCH_MAP = Object.freeze({
  17: { match: 33, position: "top" },
  18: { match: 33, position: "bottom" },
  19: { match: 34, position: "top" },
  20: { match: 34, position: "bottom" },
  21: { match: 35, position: "top" },
  22: { match: 35, position: "bottom" },
  23: { match: 36, position: "top" },
  24: { match: 36, position: "bottom" },
  33: { match: 45, position: "top" },
  34: { match: 45, position: "bottom" },
  35: { match: 46, position: "top" },
  36: { match: 46, position: "bottom" },
  37: { match: 41, position: "bottom" },
  38: { match: 42, position: "top" },
  39: { match: 43, position: "bottom" },
  40: { match: 44, position: "top" },
  41: { match: 47, position: "top" },
  42: { match: 47, position: "bottom" },
  43: { match: 48, position: "top" },
  44: { match: 48, position: "bottom" },
  45: { match: 54, position: "top" },
  46: { match: 54, position: "bottom" },
  47: { match: 49, position: "bottom" },
  48: { match: 50, position: "top" },
  49: { match: 53, position: "top" },
  50: { match: 53, position: "bottom" },
  52: { match: 1005, position: "top" },
  53: { match: 1003, position: "top" },
  54: { match: 1001, position: "top" },
  //
  1001: null,
  1003: null,
  1005: null,
});
const LOSE_MATCH_MAP = Object.freeze({
  // NOTE: Matches 1-16 (Preliminaries) require special handling based on the
  //       follow-the-leader (to semifinals) format.
  1: null,
  2: null,
  3: null,
  4: null,
  5: null,
  6: null,
  7: null,
  8: null,
  9: null,
  10: null,
  11: null,
  12: null,
  13: null,
  14: null,
  15: null,
  16: null,
  // NOTE: Matches (R16) require special handling based on the follow-the-leader
  //       (to semifinals) format.
  17: null,
  18: null,
  19: null,
  20: null,
  21: null,
  22: null,
  23: null,
  24: null,
  33: { match: 41, position: "top" },
  34: { match: 42, position: "bottom" },
  35: { match: 43, position: "top" },
  36: { match: 44, position: "bottom" },
  37: null,
  38: null,
  39: null,
  40: null,
  41: null,
  42: null,
  43: null,
  44: null,
  45: { match: 49, position: "top" },
  46: { match: 50, position: "bottom" },
  47: null,
  48: null,
  49: { match: 52, position: "top" },
  50: { match: 52, position: "bottom" },
  52: null,
  53: null,
  54: null,
});
const DISABLE_BY_EXTRA = Object.freeze({
  45: { top: [37, 41], bottom: [38, 42] },
  46: { top: [39, 43], bottom: [40, 44] },
  53: { top: [52], bottom: [52] },
  54: { top: [49], bottom: [50] },
});

function numericalSort(a, b) {
  return a - b;
}

function validateParticipantID(participantID) {
  if (participantID === null) {
    return;
  }

  if (
    !Number.isInteger(participantID) ||
    participantID < 0 ||
    participantID > 23
  ) {
    throw new Error(`Invalid participant ID: ${participantID}`);
  }
}

function writeToStorage(bracketInfo) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(bracketInfo));
}

function loadFromStorage(bracketInfo) {
  const serialized = localStorage.getItem(STORAGE_KEY);
  if (serialized === null) {
    // Leave the initial value as-is
    return;
  }

  const parsedInputs = JSON.parse(serialized);
  bracketInfo.description = parsedInputs.description;
  bracketInfo.wrestlerChoices = parsedInputs.wrestlerChoices;
  bracketInfo.matches = parsedInputs.matches;
}

function renderWrestlerInput(bracketInfo, participantID) {
  const wrestler = bracketInfo.wrestlerChoices[participantID];

  const nameInput = document.querySelector(
    `input.input-name[data-participant-id="${participantID}"]`
  );
  nameInput.value = wrestler.name;

  const teamInput = document.querySelector(
    `input.input-team[data-participant-id="${participantID}"]`
  );
  teamInput.value = wrestler.team;
}

function populateNameDiv(position, participantDiv, wrestler, winner) {
  const nameDiv = participantDiv.querySelector("div.name");
  const resultDiv = participantDiv.querySelector("div.result");

  if (winner === null) {
    participantDiv.className = "participant";
    resultDiv.textContent = "";
  } else if (winner === position) {
    participantDiv.className = "participant win";
    resultDiv.textContent = "W";
  } else {
    participantDiv.className = "participant loss";
    resultDiv.textContent = "L";
  }

  nameDiv.textContent = ""; // Clear first

  if (wrestler === null) {
    nameDiv.className = "name bye";
    nameDiv.innerHTML = "&nbsp;";
    return;
  }

  const nameText = document.createTextNode(wrestler.name);
  const teamSpan = document.createElement("span");
  teamSpan.textContent = ` (${wrestler.team})`;

  nameDiv.appendChild(nameText);
  nameDiv.appendChild(teamSpan);
}

function renderMatchReadOnly(bracketInfo, matchID, positions) {
  const match = bracketInfo.matches[matchID];
  const topChoice = match.top.choice;
  const bottomChoice = match.bottom.choice;

  const topWrestler =
    topChoice === null ? null : bracketInfo.wrestlerChoices[topChoice];
  const bottomWrestler =
    bottomChoice === null ? null : bracketInfo.wrestlerChoices[bottomChoice];

  const matchDiv = document.querySelector(
    `div.match[data-match-id="${matchID}"]`
  );
  const participants = matchDiv.querySelectorAll("div.participant");
  if (participants.length !== 2) {
    throw new Error("Invalid DOM (participants)");
  }

  if (positions.includes("top")) {
    populateNameDiv("top", participants[0], topWrestler, match.winner);
  }
  if (positions.includes("bottom")) {
    populateNameDiv("bottom", participants[1], bottomWrestler, match.winner);
  }
}

function matchIsDecided(bracketInfo, matchID) {
  const match = bracketInfo.matches[matchID];
  // Exclude byes
  if (match.top.choice === null || match.bottom.choice === null) {
    return false;
  }

  return match.winner !== null;
}

function populateParticipantSelect(
  bracketInfo,
  position,
  participantDiv,
  choice,
  choices,
  winner,
  matchID
) {
  const participantSelect = participantDiv.querySelector(
    "select.participant-select"
  );
  const resultDiv = participantDiv.querySelector("div.result");

  if (winner === null) {
    participantDiv.className = "participant";
    resultDiv.textContent = "";
  } else if (winner === position) {
    participantDiv.className = "participant win";
    resultDiv.textContent = "W";
  } else {
    participantDiv.className = "participant loss";
    resultDiv.textContent = "L";
  }

  participantSelect.innerHTML = ""; // Clear all existing options

  const emptyOption = document.createElement("option");
  emptyOption.value = "";
  emptyOption.textContent = "Select wrestler";
  participantSelect.appendChild(emptyOption);

  for (const participantID of choices) {
    const wrestler = bracketInfo.wrestlerChoices[participantID];
    const option = document.createElement("option");
    option.value = `${participantID}`;
    option.textContent = wrestler.name;
    participantSelect.appendChild(option);
  }

  if (choice === null) {
    participantSelect.value = "";
  } else {
    if (!choices.includes(choice)) {
      throw new Error("Choice is invalid");
    }
    participantSelect.value = choice;
  }

  // Disabled if (A) we do not have at least 2 choices or (B) the **NEXT** match
  // is finalized
  participantSelect.disabled = choices.length < 2 || winner !== null;

  // NOTE: There are a few special cases where a "top side" select must be
  //       disabled because a "bottom side" match that is already decided
  //       depends on the already selected value.
  const extraDisable = DISABLE_BY_EXTRA[matchID];
  if (extraDisable === undefined) {
    return;
  }

  for (const otherMatchID of extraDisable[position]) {
    if (matchIsDecided(bracketInfo, otherMatchID)) {
      participantSelect.disabled = true;
      return;
    }
  }
}

function renderMatchSelect(bracketInfo, matchID, positions) {
  const match = bracketInfo.matches[matchID];
  const topChoice = match.top.choice;
  const topChoices = match.top.choices;
  const bottomChoice = match.bottom.choice;
  const bottomChoices = match.bottom.choices;

  const matchDiv = document.querySelector(
    `div.match[data-match-id="${matchID}"]`
  );
  const participants = matchDiv.querySelectorAll("div.participant");
  if (participants.length !== 2) {
    throw new Error("Invalid DOM (participants)");
  }

  if (positions.includes("top")) {
    populateParticipantSelect(
      bracketInfo,
      "top",
      participants[0],
      topChoice,
      topChoices,
      match.winner,
      matchID
    );
  }
  if (positions.includes("bottom")) {
    populateParticipantSelect(
      bracketInfo,
      "bottom",
      participants[1],
      bottomChoice,
      bottomChoices,
      match.winner,
      matchID
    );
  }
}

function renderBracket(bracketInfo) {
  // Description input
  if (bracketInfo.description !== null) {
    document.getElementById("description-input").value =
      bracketInfo.description;
  }

  // Wrestler and Team inputs
  for (let participantID = 0; participantID <= 23; participantID++) {
    renderWrestlerInput(bracketInfo, participantID);
  }

  // Read-only match entries
  for (let matchID = 1; matchID <= 16; matchID++) {
    // Preliminaries
    renderMatchReadOnly(bracketInfo, matchID, ["top", "bottom"]);
  }
  for (let matchID = 17; matchID <= 24; matchID++) {
    // R16
    renderMatchReadOnly(bracketInfo, matchID, ["top"]);
  }
  for (let matchID = 37; matchID <= 40; matchID++) {
    // Consolation Round 1
    renderMatchReadOnly(bracketInfo, matchID, ["top", "bottom"]);
  }
  renderMatchReadOnly(bracketInfo, 41, ["top"]); // Consolation Round 2
  renderMatchReadOnly(bracketInfo, 42, ["bottom"]); // Consolation Round 2
  renderMatchReadOnly(bracketInfo, 43, ["top"]); // Consolation Round 2
  renderMatchReadOnly(bracketInfo, 44, ["bottom"]); // Consolation Round 2
  renderMatchReadOnly(bracketInfo, 49, ["top"]); // Consolation Semifinal
  renderMatchReadOnly(bracketInfo, 50, ["bottom"]); // Consolation Semifinal
  renderMatchReadOnly(bracketInfo, 52, ["top", "bottom"]); // Fifth place

  // <select> match entries
  for (let matchID = 17; matchID <= 24; matchID++) {
    // R16
    renderMatchSelect(bracketInfo, matchID, ["bottom"]);
  }
  for (let matchID = 33; matchID <= 36; matchID++) {
    // Quarterfinal
    renderMatchSelect(bracketInfo, matchID, ["top", "bottom"]);
  }
  renderMatchSelect(bracketInfo, 41, ["bottom"]); // Consolation Round 2
  renderMatchSelect(bracketInfo, 42, ["top"]); // Consolation Round 2
  renderMatchSelect(bracketInfo, 43, ["bottom"]); // Consolation Round 2
  renderMatchSelect(bracketInfo, 44, ["top"]); // Consolation Round 2
  renderMatchSelect(bracketInfo, 45, ["top", "bottom"]); // Semifinal
  renderMatchSelect(bracketInfo, 46, ["top", "bottom"]); // Semifinal
  renderMatchSelect(bracketInfo, 47, ["top", "bottom"]); // Consolation Blood Round
  renderMatchSelect(bracketInfo, 48, ["top", "bottom"]); // Consolation Blood Round
  renderMatchSelect(bracketInfo, 49, ["bottom"]); // Consolation Semifinal
  renderMatchSelect(bracketInfo, 50, ["top"]); // Consolation Semifinal
  renderMatchSelect(bracketInfo, 53, ["top", "bottom"]); // Consolation Third Place: 53
  renderMatchSelect(bracketInfo, 54, ["top", "bottom"]); // First place
  renderMatchSelect(bracketInfo, 1001, ["top"]); // Synthetic first place winner
  renderMatchSelect(bracketInfo, 1003, ["top"]); // Synthetic third place winner
  renderMatchSelect(bracketInfo, 1005, ["top"]); // Synthetic fifth place winner
}

function setWinner(match, participantID) {
  if (participantID === null) {
    match.winner = null;
  } else if (match.top.choice === participantID) {
    match.winner = "top";
  } else if (match.bottom.choice === participantID) {
    match.winner = "bottom";
  } else {
    throw new Error("Chosen winner must be top or bottom");
  }
}

function replaceChoices(choices, previousSubset, newChoice) {
  const withoutPrevious = choices.filter(
    (value) => !previousSubset.includes(value)
  );

  if (newChoice !== null) {
    withoutPrevious.push(newChoice);
  }

  withoutPrevious.sort(numericalSort);
  return withoutPrevious;
}

function updateNextMatchChoices(bracketInfo, matchID, matchPosition, winnerID) {
  const nextMatchInfo = WIN_MATCH_MAP[matchID];
  if (nextMatchInfo === null) {
    return;
  }

  const nextMatch = bracketInfo.matches[nextMatchInfo.match];
  const nextMatchPosition = nextMatch[nextMatchInfo.position];
  nextMatchPosition.choices = replaceChoices(
    nextMatchPosition.choices,
    matchPosition.choices,
    winnerID
  );
}

function getLoserID(match, winnerID) {
  if (winnerID === null) {
    return null;
  }

  if (match.top.choice === winnerID) {
    return match.bottom.choice;
  }

  if (match.bottom.choice === winnerID) {
    return match.top.choice;
  }

  throw new Error("Chosen winner must be top or bottom");
}

function setLoser(bracketInfo, matchID, match, winnerID) {
  const nextMatchInfo = LOSE_MATCH_MAP[matchID];
  if (nextMatchInfo === null) {
    return;
  }

  const loserID = getLoserID(match, winnerID);
  const nextMatch = bracketInfo.matches[nextMatchInfo.match];
  const nextMatchPosition = nextMatch[nextMatchInfo.position];

  const previousChoice = nextMatchPosition.choice;
  nextMatchPosition.choice = loserID;
  nextMatchPosition.choices = loserID === null ? [] : [loserID];

  // Update `choices` that comes **after** the match we set
  const choicesMatchInfo = WIN_MATCH_MAP[nextMatchInfo.match];
  const choicesMatch = bracketInfo.matches[choicesMatchInfo.match];
  const choicesMatchPosition = choicesMatch[choicesMatchInfo.position];

  choicesMatchPosition.choices = choicesMatchPosition.choices.filter(
    (value) => value != previousChoice
  );

  if (loserID !== null) {
    choicesMatchPosition.choices.push(loserID);
  }

  choicesMatchPosition.choices.sort(numericalSort);
}

function findLoser(bracketInfo, candidateMatchIDs, winnerID) {
  if (winnerID === null) {
    return null;
  }

  for (const matchID of candidateMatchIDs) {
    const match = bracketInfo.matches[matchID];

    if (match.winner === "top" && match.top.choice === winnerID) {
      return match.bottom.choice;
    }

    if (match.winner === "bottom" && match.bottom.choice === winnerID) {
      return match.top.choice;
    }
  }

  return null;
}

function handleFollowLeader(bracketInfo, matchID, winnerID) {
  if (matchID < 33 || matchID > 36) {
    return;
  }

  const preliminaryMatchIDs = [];
  const r16MatchIDs = [];

  if (matchID === 33) {
    preliminaryMatchIDs.push(1, 2, 3, 4);
    r16MatchIDs.push(17, 18);
  }

  if (matchID === 34) {
    preliminaryMatchIDs.push(5, 6, 7, 8);
    r16MatchIDs.push(19, 20);
  }

  if (matchID === 35) {
    preliminaryMatchIDs.push(9, 10, 11, 12);
    r16MatchIDs.push(21, 22);
  }

  if (matchID === 36) {
    preliminaryMatchIDs.push(13, 14, 15, 16);
    r16MatchIDs.push(23, 24);
  }

  // 33->37, 34->38, 35->39, 36->40
  const round1MatchID = matchID + 4;
  const round1Match = bracketInfo.matches[round1MatchID];
  const position1 = matchID % 2 === 1 ? "top" : "bottom";
  const matchPosition1 = round1Match[position1];
  const position2 = matchID % 2 === 1 ? "bottom" : "top";
  const matchPosition2 = round1Match[position2];

  const preliminaryMatchLoser = findLoser(
    bracketInfo,
    preliminaryMatchIDs,
    winnerID
  );
  const r16MatchLoser = findLoser(bracketInfo, r16MatchIDs, winnerID);

  matchPosition1.choice = preliminaryMatchLoser;
  matchPosition2.choice = r16MatchLoser;

  // 33->41, 34->42, 35->43, 36->44
  const round2MatchID = matchID + 8;
  const round2Match = bracketInfo.matches[round2MatchID];
  const matchPosition3 = round2Match[position2];

  const bloodRoundInfo = WIN_MATCH_MAP[round2MatchID];
  const bloodRoundMatch = bracketInfo.matches[bloodRoundInfo.match];
  const matchPosition4 = bloodRoundMatch[bloodRoundInfo.position];

  matchPosition1.choices = [];
  matchPosition2.choices = [];
  matchPosition3.choices = [];

  if (preliminaryMatchLoser !== null) {
    matchPosition1.choices.push(preliminaryMatchLoser);
    matchPosition3.choices.push(preliminaryMatchLoser);
  }

  if (r16MatchLoser !== null) {
    matchPosition2.choices.push(r16MatchLoser);
    matchPosition3.choices.push(r16MatchLoser);
  }

  matchPosition3.choices.sort(numericalSort);

  matchPosition3.choice = null;
  round1Match.winner = null;
  if (matchPosition3.choices.length === 1) {
    matchPosition3.choice = matchPosition3.choices[0];
    round1Match.winner = position2;

    matchPosition4.choices.push(matchPosition3.choice);
    matchPosition4.choices.sort(numericalSort);
  }
}

function handleSelectChange(bracketInfo, event) {
  const select = event.target;
  const participantID = select.value === "" ? null : Number(select.value);
  validateParticipantID(participantID);

  // Current match position (choice)
  const matchID = Number(select.dataset.matchId);
  const position = select.dataset.position;
  const match = bracketInfo.matches[matchID];
  const matchPosition = match[position];
  matchPosition.choice = participantID;

  // Previous match (winner)
  const previousMatchID = PREVIOUS_MATCH_MAP[matchID][position];
  const previousMatch = bracketInfo.matches[previousMatchID];
  setWinner(previousMatch, participantID);

  // Next match, winner (choices / disabled / enabled)
  updateNextMatchChoices(bracketInfo, matchID, matchPosition, participantID);

  // Next match, loser (choices / disabled / enabled)
  setLoser(bracketInfo, previousMatchID, previousMatch, participantID);

  // Special case for quarterfinal winners
  handleFollowLeader(bracketInfo, previousMatchID, participantID);
}

function handleHeaderInputChange(bracketInfo, event) {
  const element = event.target;
  if (element.id === "description-input") {
    bracketInfo.description = element.value;
    return;
  }

  throw new Error("Invalid input element");
}

function handleParticipantInputChange(bracketInfo, event) {
  const element = event.target;
  const participantID = Number(element.dataset.participantId);
  validateParticipantID(participantID);

  const wrestler = bracketInfo.wrestlerChoices[participantID];

  if (element.className === "input-name") {
    wrestler.name = element.value;
  } else if (element.className === "input-team") {
    wrestler.team = element.value;
  } else {
    throw new Error("Invalid input element");
  }
}

document.querySelectorAll("select.participant-select").forEach((select) => {
  select.addEventListener("change", (event) => {
    handleSelectChange(BRACKET_INFO, event);
    writeToStorage(BRACKET_INFO);
    renderBracket(BRACKET_INFO);
  });
});

document.querySelectorAll(".header-input").forEach((input) => {
  input.addEventListener("input", (event) => {
    handleHeaderInputChange(BRACKET_INFO, event);
    writeToStorage(BRACKET_INFO);
    renderBracket(BRACKET_INFO);
  });
});

document
  .querySelectorAll("input.input-name, input.input-team")
  .forEach((input) => {
    input.addEventListener("input", (event) => {
      handleParticipantInputChange(BRACKET_INFO, event);
      writeToStorage(BRACKET_INFO);
      renderBracket(BRACKET_INFO);
    });
  });

loadFromStorage(BRACKET_INFO);
renderBracket(BRACKET_INFO);
