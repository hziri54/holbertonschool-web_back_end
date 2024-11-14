function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}
function getBudgetForCurrentYear(income, gdp, capita) {
  return {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };
}

export { getBudgetForCurrentYear };
