// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// and set the environment variables. See http://twil.io/secure
import { client, verifySid } from '../../shared/twilio';

export default function verifyHandler(req, res) {
  console.log(req.body);
  const number = req.body.phone;

  if (!number || !/\+\d{10}/.test(number)) {
    console.log('invalid req')
    res.statusCode = 450;
    res.setHeader('Content-Type', 'application/json');
    return res.end(JSON.stringify({
      message: 'Invalid phone number'
    }));
  }

  client.verify.services(verifySid)
    .verifications
    .create({ to: number, channel: 'sms' })
    .then(verification => console.log(verification.status));

  res.status(200).send('Verification received');
}
