// Copyright (c) 2025 - Present. IKWF History. All rights reserved.

const WRESTLER_CHOICES = [
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
  null,
];

function updateWrestlerChoices(wrestlerChoices) {
  document.querySelectorAll("tr.input-row").forEach((row) => {
    const index = Number(row.dataset.participantIndex);
    if (!Number.isInteger(index) || index < 0 || index > 23) {
      throw new Error(`Invalid index: ${row.dataset.participantIndex}`);
    }

    const name = row.querySelector(".input-name")?.value || "";
    const team = row.querySelector(".input-team")?.value || "";

    wrestlerChoices[index] = { name, team };
  });

  return wrestlerChoices;
}

function updateDropdowns(wrestlerChoices) {
  document.querySelectorAll(".participant-select").forEach((select) => {
    for (const option of select.options) {
      if (option.value === "") {
        continue;
      }

      const index = Number(option.value) - 1;
      const wrestler = wrestlerChoices[index];
      if (wrestler === null) {
        option.textContent = "<unset>";
      } else {
        option.textContent = wrestler.name;
      }
    }
  });
}

updateWrestlerChoices(WRESTLER_CHOICES);
updateDropdowns(WRESTLER_CHOICES);
