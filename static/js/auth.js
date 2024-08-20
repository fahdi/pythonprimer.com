function signUp() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  
  firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      console.log("User signed up:", user);
      window.location.href = '/dashboard';
    })
    .catch((error) => {
      console.error("Error signing up:", error);
      alert(error.message);
    });
}

function signIn() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      console.log("User signed in:", user);
      window.location.href = '/dashboard';
    })
    .catch((error) => {
      console.error("Error signing in:", error);
      alert(error.message);
    });
}

function signOut() {
  firebase.auth().signOut().then(() => {
    console.log("User signed out");
    window.location.href = '/';
  }).catch((error) => {
    console.error("Error signing out:", error);
  });
}

firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    console.log("User is signed in:", user);
    if (window.location.pathname === '/login') {
      window.location.href = '/dashboard';
    }
  } else {
    console.log("User is signed out");
    if (window.location.pathname === '/dashboard') {
      window.location.href = '/login';
    }
  }
});
