/**
 * Copyright (c) 2025 - Present. IKWF History. All rights reserved.
 */

/**
 * Set up hover listeners for all the siblings of a given element.
 * @param {HTMLElement} element
 * @param {HTMLElement[]} siblings
 */
function addHoverListeners(element, siblings) {
  element.addEventListener("mouseenter", () => {
    siblings.forEach((el) => el.classList.add("hover"));
  });

  element.addEventListener("mouseleave", () => {
    siblings.forEach((el) => el.classList.remove("hover"));
  });
}

function allParticipantsHoverTogether() {
  // NOTE: Hardcode the participant IDs 1-24
  for (let i = 0; i < 24; i++) {
    const siblings = document.querySelectorAll(
      `div[data-participant-id="${i}"]`
    );
    for (const element of siblings) {
      addHoverListeners(element, siblings);
    }
  }
}

allParticipantsHoverTogether();
