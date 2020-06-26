export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    capita,
    gdp,
    income,
  };
  return budget;
}
