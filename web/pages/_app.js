import firebase from 'firebase/app'
import 'firebase/analytics'
import 'firebase/auth'
import 'firebase/firestore'

import '../public/assets/sass/main.scss'

if (firebase.apps.length === 0) {
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional

  const firebaseConfig = {
    apiKey: process.env.API_KEY,
    authDomain: process.env.AUTH_DOMAIN,
    projectId: process.env.PROJECT_ID,
    storageBucket: process.env.STORAGE_BUCKET,
    messagingSenderId: process.env.MESSAGING_SENDER_ID,
    appId: process.env.APP_ID,
    measurementId: process.env.MEASUREMENT_ID
  };

  firebase.initializeApp(firebaseConfig);
}

const db = firebase.firestore();

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} db={db} />;
}

export default MyApp;
