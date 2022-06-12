export const humanDate = (date) => {
  const dateObj = new Date(date);
  const month = String(dateObj.getMonth() + 1).padStart(2, "0");
  const day = dateObj.getDate();
  const year = dateObj.getFullYear();
  const dateString = `${day}/${month}/${year}`;
  return dateString;
};

export const humanDateTime = (date) => {
  const dateObj = new Date(date);
  const month = String(dateObj.getMonth() + 1).padStart(2, "0");
  const day = dateObj.getDate();
  const year = dateObj.getFullYear();
  const hour = dateObj.getHours();
  const minute = String(dateObj.getMinutes()).padStart(2, "0");
  const dateString = `${day}/${month}/${year} ${hour}:${minute}`;
  return dateString;
};
