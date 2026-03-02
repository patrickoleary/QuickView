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
};
