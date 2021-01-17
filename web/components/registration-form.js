import axios from "axios";
import { useState } from "react";
import firebase from '../shared/firebase'

const db = firebase.firestore();

const StatusMessage = ({ state, verificationCode, handleVerificationCodeChange }) => {
  switch (state.state) {
    case 'awaiting code':
      return <div className="col-6 col-12-mobile">
        <input className="text" type="number" name="verification-code" id="verification-code" value={verificationCode} onChange={handleVerificationCodeChange} placeholder="Verification code" />
      </div>;
    case 'verifying':
      return <div className="col-6 col-12-mobile">Waiting for verification...</div>;
    case 'verified':
      return <div className="col-6 col-12-mobile">Approved!</div>;
    case 'error':
      return <div className="col-12">Error: {state.message}</div>;
    default:
      return null;
  }
}

export default function RegistrationForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [verificationCode, setVerificationCode] = useState('');

  const [state, setState] = useState({
    state: 'initial',
    message: ''
  });

  const handleNameChange = (event) => {
    const val = event.target.value;
    setName(val);
  }

  const handlePhoneChange = (event) => {
    const val = event.target.value;
    setPhone(val);
  }

  const handleEmailChange = (event) => {
    const val = event.target.value;
    setEmail(val);
  }

  const handleVerificationCodeChange = (event) => {
    const val = event.target.value;
    setVerificationCode(val);
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      if (state.state === 'initial' || state.state === 'error') {
        const val = await axios.post('/api/verify', {
          name, email, phone
        });

        if (val.status === 200) {
          setState({
            state: 'awaiting code',
            message: ''
          });

          db.collection('users').doc(phone).set({
            name,
            email,
            phone,
            verified: false
          });
        } else {
          setState({
            state: 'error',
            message: JSON.stringify(val.data)
          });
        }
      } else {
        const val = await axios.post('/api/check-verification', {
          verificationCode, phone
        });

        if (val.status === 200) {
          setState({
            state: 'verified',
            message: ''
          });

          db.collection('users').doc(phone).set({
            verified: true,
            verificationCode
          });
        } else {
          setState({
            state: 'error',
            message: JSON.stringify(val.data)
          });
        }
      }
    } catch (err) {
      console.error(err);
      setState({
        state: 'error',
        message: JSON.stringify(err.response.data)
      });
    }
  }

  return (
    <article className="container box style3" >
      <section>
        <header>
          <h3>Form</h3>
        </header>
        <form onSubmit={handleSubmit}>
          <div className="row">
            <div className="col-6 col-12-mobile">
              <input className="text" type="text" name="name" id="name" value={name} onChange={handleNameChange} placeholder="John Doe" required />
            </div>
            <div className="col-6 col-12-mobile">
              <input className="text" type="text" name="email" id="email" value={email} onChange={handleEmailChange} placeholder="johndoe@domain.tld" required />
            </div>
            <div className="col-6 col-12-mobile">
              <input className="text" type="tel" name="phone" id="phone" value={phone} onChange={handlePhoneChange} placeholder="+12345678900" required />
            </div>

            <StatusMessage
              state={state}
              verificationCode={verificationCode}
              handleVerificationCodeChange={handleVerificationCodeChange} />

            <div className="col-12">
              <ul className="actions">
                <li><input type="submit" value="Submit" /></li>
                <li><input type="reset" className="style3" value="Clear Form" /></li>
              </ul>
            </div>
          </div>
        </form>
      </section>
    </article >
  );
}