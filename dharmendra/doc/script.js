// generate bubbles
for (var i = 0; i < 50; i++) {
	var bubble = document.createElement("div");
	bubble.className = "bubble";
	bubble.style.top = Math.floor(Math.random() * 100) + "%";
	bubble.style.left = Math.floor(Math.random() * 100) + "%";
	document.body.appendChild(bubble);
}
