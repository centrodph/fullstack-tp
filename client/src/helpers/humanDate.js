export const humanDate = (date) => {
  const dateObj = new Date(date);
  const month = dateObj.getMonth() + 1;
  const day = dateObj.getDate();
  const year = dateObj.getFullYear();
  const hour = dateObj.getHours();
  const minute = String(dateObj.getMinutes()).padStart(2, "0");
  const dateString = `${day}/${month}/${year} ${hour}:${minute}`;
  return dateString;
};
