function double() {
  let val = document.getElementById("num").value;
  // BUG: string concatenation instead of multiplication
  document.getElementById("result").innerText = val + val;
}
