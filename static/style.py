/* Reset & body */
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #1f1c2c, #928dab);
  color: #f0f0f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
}

/* Hero banner */
.hero {
  text-align: center;
  margin: 2rem 0 1rem;
  animation: fadeInDown 1s ease;
}
.hero h1 {
  font-size: 3rem;
  letter-spacing: 2px;
  color: #ff8a00;
}
.hero p {
  font-size: 1.2rem;
  color: #ddd;
}

/* Chat container */
.chat-container {
  width: 90%;
  max-width: 600px;
  background: rgba(0,0,0,0.6);
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.4);
  overflow: hidden;
  animation: fadeInUp 1s ease;
}
.chat-window {
  height: 350px;
  overflow-y: auto;
  padding: 1rem;
  border-bottom: 1px solid rgba(255,255,255,0.2);
}
.chat-window p {
  margin: 0.5rem 0;
  line-height: 1.4;
}
#form {
  display: flex;
}
#input {
  flex: 1;
  padding: 1rem;
  border: none;
  outline: none;
  font-size: 1rem;
  background: rgba(255,255,255,0.1);
  color: #fff;
}
#input:focus {
  background: rgba(255,255,255,0.2);
}
button {
  padding: 0 1.5rem;
  border: none;
  background: #ff8a00;
  color: #000;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}
button:hover {
  background: #ffa733;
}

/* Footer */
footer {
  margin: 1.5rem 0;
  font-size: 0.9rem;
}
footer a {
  color: #ff8a00;
  text-decoration: none;
}
footer a:hover {
  text-decoration: underline;
}

/* Animations */
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
