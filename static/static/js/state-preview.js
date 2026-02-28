/**
 * Copyright (c) 2026 - Present. IKWF History. All rights reserved.
 */

const FILTERS_CONTAINER = document.querySelector("div.sectional-filters");
const CHECKBOXES = FILTERS_CONTAINER.querySelectorAll('input[type="checkbox"]');
const SECTIONAL_BITS = Object.freeze({
  central: 1,
  central_chicago: 2,
  north: 4,
  north_chicago: 8,
  south: 16,
  south_chicago: 32,
  west: 64,
  west_chicago: 128,
});

/**
 * Encode a set of sectionals into a binary encoding 0-255
 * @param {string[]} sectionals
 * @returns number
 */
function encodeSectionals(sectionals) {
  let result = 0;
  for (const sectional of sectionals) {
    // NOTE: Be lenient if the `sectional` is invalid.
    const currentBit = SECTIONAL_BITS[sectional] || 0;
    result = result | currentBit;
  }

  return result;
}

/**
 * Encode a binary encoding 0-255 into a set of sectionals
 * @param {number} mask
 * @returns string[]
 */
function decodeSectionals(mask) {
  if (!Number.isInteger(mask) || mask < 0 || mask > 255) {
    return decodeSectionals(255);
  }

  /**
   * @type {string[]}
   */
  const result = [];
  for (const [sectional, bits] of Object.entries(SECTIONAL_BITS)) {
    if ((mask & bits) !== 0) {
      result.push(sectional);
    }
  }

  return result;
}

/**
 * Filter rows in `#preview-athletes` and `#preview-head-to-heads` based on the
 * set of allowed sectionals.
 * @param {string[]} allowedSectionals
 */
function onSectionalsChanged(allowedSectionals) {
  const encoded = encodeSectionals(allowedSectionals);

  const url = new URL(window.location.href);
  if (encoded === 255) {
    url.searchParams.delete("filter");
  } else {
    url.searchParams.set("filter", encoded.toString());
  }
  history.replaceState(null, "", url);
}

function handleSectionalChange() {
  const allowedSectionals = Array.from(CHECKBOXES)
    .filter((checkbox) => checkbox.checked)
    .map((checkbox) => checkbox.value);

  onSectionalsChanged(allowedSectionals);
}

CHECKBOXES.forEach((checkbox) => {
  checkbox.addEventListener("change", handleSectionalChange);
});

/**
 * Parse the `filter` mask from the URL.
 * @returns number
 */
function parseMaskFromURL() {
  const params = new URLSearchParams(window.location.search);
  const raw = params.get("filter");

  if (raw === null) {
    return 255;
  }

  const mask = Number(raw);
  if (!Number.isInteger(mask) || mask < 0 || mask > 255) {
    return 255;
  }

  return mask;
}

/**
 * Initialize by calling `onSectionalsChanged()` based on the `filter` query
 * parameter currently on the page.
 */
function initSectionals() {
  const mask = parseMaskFromURL();
  const allowedSectionals = decodeSectionals(mask);
  CHECKBOXES.forEach((checkbox) => {
    checkbox.checked = allowedSectionals.includes(checkbox.value);
  });

  onSectionalsChanged(allowedSectionals);
}

initSectionals();
