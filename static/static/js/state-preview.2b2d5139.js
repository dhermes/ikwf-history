/**
 * Copyright (c) 2026 - Present. IKWF History. All rights reserved.
 */

const QUALIFIER_ROWS = document.querySelectorAll("tr.qualifier-row");
const HEAD_TO_HEAD_ROWS = document.querySelectorAll("tr.head-to-head-row");

function filterAllRows(targetAthleteName) {
  QUALIFIER_ROWS.forEach((tr) => {
    const athleteName = tr.dataset.athleteName;

    tr.hidden = athleteName !== targetAthleteName;
  });

  HEAD_TO_HEAD_ROWS.forEach((tr) => {
    const athleteCells = tr.querySelectorAll("td[data-athlete-name]");

    if (athleteCells.length !== 2) {
      tr.hidden = false;
      return;
    }

    const winnerName = athleteCells[0].dataset.athleteName;
    const loserName = athleteCells[1].dataset.athleteName;
    const hidden =
      winnerName !== targetAthleteName && loserName !== targetAthleteName;

    tr.hidden = hidden;
  });
}

function removeFilterAllRows() {
  QUALIFIER_ROWS.forEach((tr) => {
    tr.hidden = false;
  });

  HEAD_TO_HEAD_ROWS.forEach((tr) => {
    tr.hidden = false;
  });
}

function onClickFilter(tr, checked) {
  const athleteName = tr.dataset.athleteName;
  if (checked) {
    filterAllRows(athleteName);
  } else {
    removeFilterAllRows();
  }
}

QUALIFIER_ROWS.forEach((tr) => {
  const td = tr.querySelector("td.filter-chip");
  const input = td.querySelector("input");
  input.addEventListener("change", (event) => {
    const checked = event.target.checked;
    onClickFilter(tr, checked);
  });
});
