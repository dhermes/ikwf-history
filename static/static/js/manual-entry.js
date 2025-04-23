// Copyright (c) 2025 - Present. IKWF History. All rights reserved.

const BRACKET_INFO = {
  division: "senior",
  weight: null,
  year: null,
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
  45: { top: 33, bottom: 34 },
  46: { top: 35, bottom: 36 },
  54: { top: 45, bottom: 46 },
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
  45: { match: 54, position: "top" },
  46: { match: 54, position: "bottom" },
  54: null,
});

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
  bracketInfo.division = parsedInputs.division;
  bracketInfo.weight = parsedInputs.weight;
  bracketInfo.year = parsedInputs.year;
  bracketInfo.wrestlerChoices = parsedInputs.wrestlerChoices;
  bracketInfo.matches = parsedInputs.matches;
}

function renderWrestlerInput(bracketInfo, participantID) {
  const wrestler = bracketInfo.wrestlerChoices[participantID];
  const tr = document.querySelector(
    `tr.input-row[data-participant-id="${participantID}"]`
  );
  tr.querySelector(".input-name").value = wrestler.name;
  tr.querySelector(".input-team").value = wrestler.team;
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

function populateParticipantSelect(
  bracketInfo,
  position,
  participantDiv,
  choice,
  choices,
  winner
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
      match.winner
    );
  }
  if (positions.includes("bottom")) {
    populateParticipantSelect(
      bracketInfo,
      "bottom",
      participants[1],
      bottomChoice,
      bottomChoices,
      match.winner
    );
  }
}

function renderBracket(bracketInfo) {
  // Division input
  document.getElementById("division-input").value = bracketInfo.division;

  // Weight input
  if (bracketInfo.year !== null) {
    document.getElementById("year-input").value = bracketInfo.year;
  }

  // Year input
  if (bracketInfo.weight !== null) {
    document.getElementById("weight-input").value = bracketInfo.weight;
  }

  // Wrestler and Team inputs
  for (let participantID = 0; participantID <= 23; participantID++) {
    renderWrestlerInput(bracketInfo, participantID);
  }

  // Read-only match entries
  for (let matchID = 1; matchID <= 16; matchID++) {
    renderMatchReadOnly(bracketInfo, matchID, ["top", "bottom"]);
  }
  for (let matchID = 17; matchID <= 24; matchID++) {
    renderMatchReadOnly(bracketInfo, matchID, ["top"]);
  }

  // <select> match entries
  for (let matchID = 17; matchID <= 24; matchID++) {
    // Round of 16
    renderMatchSelect(bracketInfo, matchID, ["bottom"]);
  }
  for (let matchID = 33; matchID <= 36; matchID++) {
    // Quarterfinal
    renderMatchSelect(bracketInfo, matchID, ["top", "bottom"]);
  }
  renderMatchSelect(bracketInfo, 45, ["top", "bottom"]); // Semifinal
  renderMatchSelect(bracketInfo, 46, ["top", "bottom"]); // Semifinal
  renderMatchSelect(bracketInfo, 54, ["top", "bottom"]); // First place
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

  return withoutPrevious;
}

function handleSelectChange(bracketInfo, event) {
  const select = event.target;
  const participantID = select.value === "" ? null : Number(select.value);
  validateParticipantID(participantID);

  // Current match position (choice)
  const matchID = select.dataset.matchId;
  const position = select.dataset.position;
  const match = bracketInfo.matches[matchID];
  const matchPosition = match[position];
  matchPosition.choice = participantID;

  // Previous match (winner)
  const previousMatchID = PREVIOUS_MATCH_MAP[matchID][position];
  const previousMatch = bracketInfo.matches[previousMatchID];
  setWinner(previousMatch, participantID);

  // Next match (choices / disabled / enabled)
  const nextMatchInfo = WIN_MATCH_MAP[matchID];
  if (nextMatchInfo === null) {
    return;
  }

  const nextMatch = bracketInfo.matches[nextMatchInfo.match];
  const nextMatchPosition = nextMatch[nextMatchInfo.position];
  nextMatchPosition.choices = replaceChoices(
    nextMatchPosition.choices,
    matchPosition.choices,
    participantID
  );
}

function handleHeaderInputChange(bracketInfo, event) {
  const element = event.target;
  if (element.id === "division-input") {
    bracketInfo.division = element.value;
    return;
  }

  const integerInput = Number(element.value);
  if (!Number.isInteger(integerInput) || integerInput <= 0) {
    throw new Error(`Invalid integer input: ${element.value}`);
  }

  if (element.id === "weight-input") {
    bracketInfo.weight = integerInput;
  } else if (element.id === "year-input") {
    bracketInfo.year = integerInput;
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

loadFromStorage(BRACKET_INFO);
renderBracket(BRACKET_INFO);
