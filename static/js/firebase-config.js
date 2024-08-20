// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDrUJejH8RYI2HxNK6tEfZsizhE1nImZSQ",
  authDomain: "algorithmsin60days.firebaseapp.com",
  projectId: "algorithmsin60days",
  storageBucket: "algorithmsin60days.appspot.com",
  messagingSenderId: "1034557489379",
  appId: "1:1034557489379:web:efb8c3e280a4a232f305d6",
  measurementId: "G-MLNTEPYWMG"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Verify initialization
if (firebase.apps.length) {
  console.log("Firebase has been initialized correctly");
} else {
  console.error("Firebase initialization error");
}