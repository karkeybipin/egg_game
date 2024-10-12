function generateAccountNumber() {
  return "AC" + Math.floor(1000000000 + Math.random() * 9000000000);
}
function saveUserDetails(user) {
  let users = JSON.parse(localStorage.getItem("users")) || [];
  users.push(user);
  localStorage.setItem("users", JSON.stringify(users));
}
document.getElementById("user-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const accountNumber = generateAccountNumber();
  const user = {
    name: name,
    email: email,
    accountNumber: accountNumber,
  };
  saveUserDetails(user);
  document.getElementById(
    "message"
  ).innerHTML = `User created! Account Number: ${accountNumber}`;
  document.getElementById("user-form").reset();
});
