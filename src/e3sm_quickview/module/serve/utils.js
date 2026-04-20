class QueryFilter {
  constructor() {
    this.exacts = [];
    this.regulars = [];
    this.startsWith = [];
    this.endsWith = [];
    this.currentQuery = null;
  }

  updateQuery(query) {
    if (this.currentQuery === query) {
      return;
    }
    this.currentQuery = query;

    const pendingExact = [];
    const exacts = [];
    const regulars = [];
    const startsWith = [];
    const endsWith = [];
    const tokens = query.split(" ");
    for (let i = 0; i < tokens.length; i++) {
      const token = tokens[i];

      // Handle pending exact
      if (pendingExact.length) {
        pendingExact.push(token);

        if (token.endsWith('"')) {
          exacts.push(pendingExact.join(" ").replaceAll('"', ""));
          pendingExact.length = 0;
        }
        continue;
      }

      // Handle exact token
      if (token.startsWith('"')) {
        if (token.endsWith('"')) {
          exacts.push(token.replaceAll('"', ""));
        } else {
          pendingExact.push(token);
        }
        continue;
      }

      // Handle startsWith
      if (token.startsWith("*")) {
        endsWith.push(token.replaceAll("*", "").toLowerCase());
        continue;
      }

      // Handle endsWith
      if (token.endsWith("*")) {
        startsWith.push(token.replaceAll("*", "").toLowerCase());
        continue;
      }

      regulars.push(token.toLowerCase());
    }
    // Clear pending
    if (pendingExact.length) {
      exacts.push(pendingExact.join(" ").replaceAll('"', ""));
    }

    this.exacts = exacts;
    this.regulars = regulars;
    this.startsWith = startsWith;
    this.endsWith = endsWith;
  }

  keepItem({ name, type }) {
    // Filter exact first
    for (let i = 0; i < this.exacts.length; i++) {
      const exact = this.exacts[i];
      if (name !== exact && type !== exact) {
        return false;
      }
    }

    const nameLower = name.toLowerCase();
    const typeLower = type.toLowerCase();

    // startsWith
    for (let i = 0; i < this.startsWith.length; i++) {
      if (!nameLower.startsWith(this.startsWith[i])) {
        return false;
      }
    }

    // endsWith
    for (let i = 0; i < this.endsWith.length; i++) {
      if (!nameLower.endsWith(this.endsWith[i])) {
        return false;
      }
    }

    if (this.regulars.length) {
      return this.regulars.every(
        (v) => nameLower.includes(v) || typeLower.includes(v),
      );
    }
    return true;
  }
}

QUERY_FILTER = new QueryFilter();

window.trame.utils.quickview = {
  formatRange(value, useLog) {
    if (value === null || value === undefined || isNaN(value)) {
      return "Auto";
    }
    if (useLog && value > 0) {
      return `10^(${Math.log10(value).toFixed(1)})`;
    }
    const nSignDigit = Math.log10(Math.abs(value));
    if (Math.abs(nSignDigit) < 6 || value === 0) {
      if (nSignDigit > 0 && nSignDigit < 3) {
        return new Intl.NumberFormat("US", { maximumFractionDigits: 2 }).format(
          value,
        );
      }
      if (nSignDigit > 3) {
        return new Intl.NumberFormat("US", { maximumFractionDigits: 0 }).format(
          value,
        );
      }

      return new Intl.NumberFormat().format(value);
    }
    return value.toExponential(1);
  },
  cols(size) {
    if (size === 1) {
      return 12;
    }
    if (size === 2) {
      return 6;
    }
    if (size === 3) {
      return 4;
    }
    if (size % 3 === 0 || (size + 1) % 3 === 0) {
      return 4;
    }
    if (size % 2 === 0) {
      return 6;
    }
    return 4;
  },
  filter(value, query, item) {
    QUERY_FILTER.updateQuery(query);
    return QUERY_FILTER.keepItem(item.raw);
  },
};
